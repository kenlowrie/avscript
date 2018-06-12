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
        from sys import stdin, stdout, stderr
        from avs.stream import StreamHandler
        self._stdinput = StreamHandler()
        self._stdoutput = stdout
        self._stderror = stderr

    def _raise_wrong_type(self, which):
        raise IOError("{} must be of type file".format(which))

    def _raise_wrong_mode(self, file, mode):
        raise IOError("{} file mode must be {}".format(which, mode))

    # TODO: The setter for stdinput is wrong. Need to decide how to
    #       handle it correctly, since it is no longer a simple stream,
    #       but an instance of a StreamHandler(). Maybe allow a file
    #       to be passed in to pushed onto the stack? Not sure. Need to
    #       think about how it should behave and implement it.
    @property
    def stdinput(self):
        return self._stdinput

    @stdinput.setter
    def stdinput(self,new_input_file):
        if(not isinstance(new_input_file,IOBase)):
            self._raise_wrong_type('new_input_file')

        elif(new_input_file.mode not in ['r','rb']):
            self._raise_wrong_mode(new_input_file.name,'r')

        self._stdinput = new_input_file

    def iopen(self,filename):
        self.stdinput.open(filename)

    def ireadline(self):
        return self.stdinput.readline()

    @property
    def stdoutput(self):
        return self.stdoutput

    @stdoutput.setter
    def stdoutput(self,new_output_file):
        if(not isinstance(new_output_file, IOBase)):
            self._throw_wrong_type('new_output_file')

        elif(new_output_file.mode not in ['w','wb']):
            self._raise_wrong_mode(new_output_file.name,'w')

        self._stdoutput = new_output_file

    def owrite(self,msg,end='\n'):
        return self._stdoutput.write("{}{}".format(msg,end))

    def oprint(self,msg):
        return self.owrite(msg)

    @property
    def stderror(self):
        return self._stderror

    @stderror.setter
    def stderror(self,new_error_file):
        if(not isinstance(new_error_file,IOBase)):
            self._throw_wrong_type('new_error_file')

        elif(new_error_file.mode not in ['w','wb']):
            self._raise_wrong_mode(new_error_file.name,'w')

        self._stderror = new_error_file

    def ewrite(self,msg,end='\n'):
        self._stderror.write("{}{}".format(msg,end))

    def eprint(self,msg):
        self.ewrite(msg)


if __name__ == '__main__':
    print("Library module. Not directly callable.")
