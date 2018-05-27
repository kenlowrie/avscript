#!/usr/bin/env python

from sys import stdin
from os.path import join, split, abspath, isfile

from exception import FileError

class _OpenFile(object):
    """A simple file class to keep track of files I am using."""
    def __init__(self, f, should_i_open_file=True, name=None):
        self.file = f
        self.i_opened = should_i_open_file
        self.name = name


class FileHandler(object):
    """This class abstracts the readline() built-in API so it can support
    having multiple files open, ala the @import keyword. When a new file
    is opened, the current file object is saved on a stack, and the file
    becomes the current file until EOF. At that point, it's closed, and
    the previous file is then popped off the stack, and we resume reading
    from it until EOF."""
    def __init__(self):
        self.filestack = []
        self.idx = -1
        self.line = ''

    def open(self, filename):
        """Open a file.
        
        Arguments:
        filename -- name of the file to open, or None to process sys.stdin
        """

        if(filename is None):
            """sys.stdin can only be opened as the first file."""
            if(self.idx is not -1):
                raise FileError(2,"ERROR: sys.stdin cannot only be opened at start")

            # set current file to sys.stdin
            self.filestack.append(_OpenFile(stdin, False))
            self.idx += 1

        else:
            # If name is prefixed with '$', prefix the filename with the path of
            # current file being read.

            if(filename[0] == '$'):
                # Make sure this isn't the first file we are opening
                if(self.idx >= 0 and self.filestack[self.idx].name is not None):
                    filename = join(split(abspath(self.filestack[self.idx].name))[0], filename[1:])

            if isfile(filename):
                name = abspath(filename)
                file = open(filename, "r")
                self.filestack.append(_OpenFile(file, True, name))
                self.idx += 1

            else:
                raise FileError(1, "ERROR: Unable to import '{}'. File does not exist.".format(filename))

    def readline(self):
        """Read the next line of input and return it. If we are at EOF and
        there's a file object on the stack, close the current file and then
        pop the prior off the stack and return the next line from it."""
        self.line = self.filestack[self.idx].file.readline()
        if(self.line == ''):
            if(len(self.filestack)):
                f = self.filestack.pop()
                if (f.i_opened):
                    f.file.close()
                self.idx -= 1

                if (self.idx >= 0):
                    return self.readline()

        return self.line

if __name__ == '__main__':
    print("Library module. Not directly callable.")
    