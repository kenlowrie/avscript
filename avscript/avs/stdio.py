#!/usr/bin/env python

"""
This module contains the code for the stdio class.

The purpose of this module is to provide an abstraction to the stdio
streams so they can be overridden easily (think redirection). This
class is intended to be a base class for others.

Next feature:

"""
from io import IOBase


class StdioWrapper(object):
    def __init__(self):
        """
        Wraps the standard IO streams

        Initialize the variables that we need to have in order
        for the class to operate
        """
        from sys import stdout, stderr
        from .stream import StreamHandler
        self._stdinput = StreamHandler()
        self._stdoutput = stdout
        self._stderror = stderr

    def _raise_wrong_type(self, which):
        raise IOError("{} must be of type file".format(which))

    def _raise_wrong_mode(self, file, mode):
        raise IOError("{} file mode must be {}".format(file, mode))

    @property
    def stdinput(self):
        return self._stdinput

    @stdinput.setter
    def stdinput(self, args):
        """
        Set the standard input stream to new_input_file

        This method will push the passed open file onto the stdinput
        file stack. The passed file must be open in 'r' or 'rb', and
        must be an instance of IOBase.
        """
        try:
            new_input_file, validate = args
        except ValueError:
            new_input_file = args
            validate = True

        if(validate and not isinstance(new_input_file, IOBase)):
            self._raise_wrong_type('new_input_file')

        elif(validate and new_input_file.mode not in ['r', 'rb']):
            self._raise_wrong_mode(new_input_file.name, 'r')

        self._stdinput.push(new_input_file)

    def isetio(self, use_stdin=True):
        self._stdinput._started_with_stdin = use_stdin
        self._stdinput._started_with_file = not use_stdin

    def iopen(self, filename):
        self.stdinput.open(filename)

    def ireadline(self):
        return self.stdinput.readline()

    @property
    def stdoutput(self):
        return self.stdoutput

    @stdoutput.setter
    def stdoutput(self, args):
        try:
            new_output_file, validate = args
        except ValueError:
            new_output_file = args
            validate = True

        if(validate and not isinstance(new_output_file, IOBase)):
            self._raise_wrong_type('new_output_file')

        elif(validate and new_output_file.mode not in ['w', 'wb']):
            self._raise_wrong_mode(new_output_file.name, 'w')

        self._stdoutput = new_output_file

    def owrite(self, msg, end='\n'):
        return self._stdoutput.write("{}{}".format(msg, end))

    def oprint(self, msg):
        return self.owrite(msg)

    @property
    def stderror(self):
        return self._stderror

    @stderror.setter
    def stderror(self, args):
        try:
            new_error_file, validate = args
        except ValueError:
            new_error_file = args
            validate = True

        if(validate and not isinstance(new_error_file, IOBase)):
            self._raise_wrong_type('new_error_file')

        elif(validate and new_error_file.mode not in ['w', 'wb']):
            self._raise_wrong_mode(new_error_file.name, 'w')

        self._stderror = new_error_file

    def ewrite(self, msg, end='\n'):
        self._stderror.write("{}{}".format(msg, end))

    def eprint(self, msg):
        self.ewrite(msg)


if __name__ == '__main__':
    print("Library module. Not directly callable.")
