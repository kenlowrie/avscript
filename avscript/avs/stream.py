#!/usr/bin/env python
"""Abstraction for input stream handling in stdio class.

These classes support the implementation of @import; that is, the
ability to import a new file while processing the current one. When a new
file is imported, it is read until EOF, and then the class will fall back
to processing the prior file. @imports can be nested to allow even more
flexibility.
"""

from sys import stdin
from os.path import join, split, abspath, isfile

from .exception import FileError


class _OpenFile(object):
    """A simple class to keep track of files that are opened."""
    def __init__(self, f, name):
        self.file = f
        self.name = name


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
        self._started_with_stdin = None
        self._started_with_file = None

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
                file = open(filename, "r")
                self.push(file, name)

            else:
                raise FileError(1, "ERROR: Unable to import '{}'. File does not exist.".format(filename))

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
        self.line = ''
        if self.idx < 0:
            # Once we've read from sys.stdin, we need to remember that,
            # so that if we've imported a file, we will fall back to
            # reading from sys.stdin after we hit EOF on the imported file.
            if self._started_with_stdin:
                # If we started with stdin, fall back to reading from sys.stdin
                self.line = stdin.readline()
        else:
            # we are reading from a file, read the next line
            self.line = self.filestack[self.idx].file.readline()

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
