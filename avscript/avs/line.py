#!/usr/bin/env python


class Line(object):
    """A wrapper class for a line of input."""
    def __init__(self, cssPrefix=None, curLine=None, oriLine=None, was_indented=False, md_func=None):
        self._cssPrefix = cssPrefix
        self._curLine = curLine
        self._oriLine = oriLine
        self._strippedLine = None
        self._marked_down = False
        self._md_ptr = md_func
        self._was_indented = was_indented

    @property
    def current_line(self):
        if not self._marked_down:
            self._curLine = self._md_ptr(self._strippedLine)
            self._marked_down = True
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
        self._marked_down = False

    @property
    def css_prefix(self):
        return self._cssPrefix

    @css_prefix.setter
    def css_prefix(self, prefix):
        self._cssPrefix = prefix

    @property
    def stripped_line(self):
        return self._strippedLine

    @stripped_line.setter
    def stripped_line(self, stripped):
        self._strippedLine = stripped

    @property
    def was_indented(self):
        return self._was_indented

    @was_indented.setter
    def was_indented(self, value):
        self._was_indented = value


if __name__ == '__main__':
    print("Library module. Not directly callable.")
