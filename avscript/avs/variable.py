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
        from .regex import Regex
        self.delayedExpansion = Regex(r'(\[{{([^}]+)}}\])')

    def addVar(self, id, text):
        """Add a variable called 'id' to the list and set its value to 'text'."""
        if type(text) is str:
            from re import findall
            matches = findall(self.delayedExpansion.regex, text)
            for m in matches:
                # for each delayed expansion variable, strip the {{}} from the name
                text = text.replace(m[0],'[{}]'.format(m[1]))

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


class ImageDict(VariableDict):
    """Class to abstract a dictionary of images"""
    def __init__(self):
        super(ImageDict, self).__init__()  # Initialize the base class(es)

    def addImage(self, dict):
        imageID = dict["_id"]
        del dict["_id"]
        self.addVar(imageID, dict)

    def getImage(self, id, _markdown):
        if self.exists(id):
            imageTag = '<img'
            for item in sorted(self.vars[id].text):
                attrText = _markdown(self.vars[id].text[item])
                imageTag += ' {}="{}"'.format(item, attrText)
            imageTag += '/>'
            return imageTag

        return '<img src="undefined image {}"/>'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].text:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.vars[var].text[d_item])
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, dict_str, indent))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
