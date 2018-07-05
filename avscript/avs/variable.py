#!/usr/bin/env python

from __future__ import print_function


class _Variable(object):
    """Class to abstract a variable (alias). Keep track of the ID (name) and
    the value (text)."""
    def __init__(self, id, text):
        self.id = id
        self.text = text


class VariableDict(object):
    """Class to abstract a dictionary of variables (aliases)"""
    def __init__(self):
        self.vars = {}

    def addVar(self, id, text):
        """Add a variable called 'id' to the list and set its value to 'text'."""
        self.vars[id] = _Variable(id, text)

    def exists(self, id):
        """Returns true if the variable 'id' exists."""
        return id in self.vars

    def getText(self, id):
        """Gets the value of the variable 'id', unless it doesn't exist, in
        which case it returns (undefined).

        TODO: Should this just return an empty string if undefined?"""
        return "(undefined)" if not self.exists(id) else self.vars[id].text

    def dumpVars(self, indent='', output=print):
        """Dumps the variable list, names and values."""
        def escape_html(s):
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        for var in sorted(self.vars):
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, escape_html(self.vars[var].text), indent))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
