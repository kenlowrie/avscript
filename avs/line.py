#!/usr/bin/env python


class Line(object):
    """A wrapper class for a line of input."""
    def __init__(self, cssPrefix=None, curLine=None, oriLine=None, was_indented=False):
        self._cssPrefix = cssPrefix
        self._curLine = curLine
        self._oriLine = oriLine
        self._was_indented = was_indented

    @property
    def current_line(self):
        return self._curLine

    @current_line.setter
    def current_line(self, line):
        self._curLine = line

    @property
    def original_line(self):
        return self._oriLine

    @original_line.setter
    def original_line(self, ori_line):
        self._oriLine = ori_line

    @property
    def css_prefix(self):
        return self._cssPrefix

    @css_prefix.setter
    def css_prefix(self, prefix):
        self._cssPrefix = prefix

    @property
    def was_indented(self):
        return self._was_indented

    @was_indented.setter
    def was_indented(self, value):
        self._was_indented = value


if __name__ == '__main__':
    print("Library module. Not directly callable.")
