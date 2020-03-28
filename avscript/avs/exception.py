#!/usr/bin/env python

# The class implementation for the exception handling in the underlying classes


class _Error(Exception):
    """Base exception class for this module."""
    pass


class FileError(_Error):
    """File IO exceptions raised by this module."""
    def __init__(self, errno, errmsg):
        self.errno = errno
        self.errmsg = errmsg


class RegexError(_Error):
    """Regex exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


class LogicError(_Error):
    """Logic exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


class NestingError(_Error):
    """Regex exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


if __name__ == '__main__':
    print("Library module. Not directly callable.")
