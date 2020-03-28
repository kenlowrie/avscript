#!/usr/bin/env python
"""Abstraction for input stream handling in stdio class.

These classes support the implementation of @import; that is, the
ability to import a new file while processing the current one. When a new
file is imported, it is read until EOF, and then the class will fall back
to processing the prior file. @imports can be nested to allow even more
flexibility.
"""

from sys import stdin
from os.path import join, split, abspath, isfile, realpath, dirname

from .exception import FileError, LogicError
from .globals import init_globals
from .debug import Debug
from .utility import HtmlUtils

class _OpenFile(object):
    """A simple class to keep track of files that are opened."""
    def __init__(self, f, name):
        self.file = f
        self.name = name

class Cache(object):
    """A class to abstract a line cache.
    
    Initially, this is used to process the built-ins that are part of avscript. However,
    it can also be used to cache lines in the middle of processing normal files.
    """
    def __init__(self):
        builtins = join(abspath(dirname(realpath(__file__))), 'builtins.md')
        with open(builtins) as f:
            builtins = [line for line in f]

        # Reverse the list (make this a stack)
        self._cache = builtins[::-1]

        # add the globals onto the stack
        for line in init_globals():
            self._cache.append(line)

    def initDebug(self):
            self.debug = Debug('cache')

    def pushline(self, s):
        self._cache.append(s)

    def readline(self):
        line = ''
        while self.gotCachedLine():
            line += self._cache.pop().strip()
            if line.endswith('\\'):
                # Remove the \ and add a space
                line = line[:-1] + ' '
                # Only continue if there are more lines, in case they put a \ on the last line
                if self._cache:
                    continue

            # If the line we have is blank, then it only has white space.
            if not line.strip():
                if self._cache:
                    # if there's more lines, then by all means, keep reading, ignore blanks
                    continue
                else:
                    # This is an odd spot. We don't want to make it difficult to add built-ins,
                    # so we need to handle this gracefully. Let's pretend the line was a comment
                    line = "// Blank line in the cache..."

            # Return the line
            self.debug.print('Returning: <em>{}</em>'.format(HtmlUtils.escape_html(line)))
            return line

        raise LogicError("Cache().readline() failed while processing cache.")

    def gotCachedLine(self):
        return self._cache      # self._builtIn < len(self._builtIns)
        

class StreamHandler(object):
    """
    Abstract open() and readline() to implement @import support

    This class abstracts the open() & readline() APIs so they can support
    having multiple files open, ala the @import keyword. When a new file
    is opened, the current file object is saved on a stack, and the file
    becomes the current file until EOF. At that point, it's closed, and
    the previous file is then popped off the stack, and we resume reading
    from it until EOF.
    """
    def __init__(self):
        self.filestack = []
        self.idx = -1
        self.line = ''
        self.imported = []
        self._started_with_stdin = None
        self._started_with_file = None
        self._cache = Cache()

        # Easy way to force EOF no matter what we're doing
        self._fake_eof = False

    def cache(self):
        return self._cache

    def initDebug(self):
            self.debug = Debug('stdinput')
            self._cache.initDebug()

    @property
    def fake_eof(self):
        return self._fake_eof

    @fake_eof.setter
    def fake_eof(self, flag):
        self._fake_eof = flag

    def force_eof(self):
        self.fake_eof = True

    def push(self, fh, name=None):
        """
        Push an open file onto the stack for readline()

        This method can be used to push an open file onto the filestack,
        as an alternative to passing in a filename (open() method).
        """
        self.filestack.append(_OpenFile(fh, name))
        self.idx += 1

    def open(self, filename):
        """
        Open a file and place the handle on the stack for readline()

        Once a file has been opened, subsequent calls to readline() use
        that handle to return data.

        None can be passed to signify that sys.stdin should be used, however
        it's not required, since that's the default behavior of this class.
        This is done primarily as a convenience for the consumer of the class.

        Arguments:
        filename -- name of the file to open, or None to process sys.stdin
        """

        if(filename is None):
            """sys.stdin can only be opened as the first file."""
            if(self.idx is not -1):
                raise FileError(2, "ERROR: sys.stdin can only be opened at start")

        else:
            # If name is prefixed with '$', prefix the filename with the path of
            # CURRENT open file. This is not supported on the 1st open...
            if(filename[0] == '$'):
                # Make sure this isn't the first file we are opening
                if(self.idx >= 0 and self.filestack[self.idx].name is not None):
                    from os import sep
                    path, whocares = split(abspath(self.filestack[self.idx].name))
                    filename = join(path, filename[1:] if filename[1] != sep else filename[2:])
            # Make sure the specified file exists, and then open it
            if isfile(filename):
                name = abspath(filename)
                # Check if we've already imported this file
                if name in self.imported:
                    self.debug.print('File <strong><em>{}</em></strong> has already been imported'.format(name))
                    return
                file = open(filename, "r")
                self.push(file, name)
                self.imported.append(name)

            else:
                raise FileError(1, "ERROR: Unable to import '{}'. File does not exist.<br />".format(filename))

    def readline(self):
        """
        Read the next line of input and return it.

        If no file is currently opened, reads from sys.stdin. Once you hit
        EOF, return an empty string ''. This is the basic (default) behavior.

        If you open a file (via the open method of this class), the behaviour
        changes as follows. Read the next line until you hit EOF, and then,
        fall back to reading from sys.stdin until EOF.

        If another file is opened (via open() method) while reading from the
        current file, we read from the new file until EOF, and then close it,
        and fall back to the previous file.
        """
        if self.fake_eof:
            self.debug.print("<strong><em>Forced EOF</em></strong>")
            return ''

        # Process the builtIns first.
        self.line = ''
        if self._cache.gotCachedLine():
            return self._cache.readline()

        while 1:
            if self.idx < 0:
                # Once we've read from sys.stdin, we need to remember that,
                # so that if we've imported a file, we will fall back to
                # reading from sys.stdin after we hit EOF on the imported file.
                if self._started_with_stdin:
                    # If we started with stdin, fall back to reading from sys.stdin
                    self.line += stdin.readline()
                else:
                    break       # can't continue if we didn't start with stdin...
            else:
                # we are reading from a file, read the next line
                self.line += self.filestack[self.idx].file.readline()

            if not self.line or not self.line.rstrip():
                break
            elif not self.line.rstrip().endswith('\\'):
                break
            self.line = self.line.rstrip()[:-1]

        if(self.line == ''):
            # We hit EOF. Do we have any other files opened?
            if(len(self.filestack)):
                # Pop the current file from the stack
                f = self.filestack.pop()
                f.file.close()
                # set the index back 1, so future reads will use prior file
                self.idx -= 1

                if (self.idx >= 0 or self._started_with_stdin):
                    return self.readline()

        return self.line


if __name__ == '__main__':
    print("Library module. Not directly callable.")
