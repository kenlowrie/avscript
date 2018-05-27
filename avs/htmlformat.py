#!/usr/bin/env python

class HTMLFormatter(object):
    _current_level = 0
    
    def getIndent(self, dedent_after=True):
        """Create a string of blanks for indenting a line to keep things aligned properly."""
        howmany = self._current_level if dedent_after else self._current_level - 1
        return " " * (howmany * 4)

    def formatLine(self, str, indent_level=0, dedent_after=True):
        """Prefix the string passed in so it will align properly in the HTML output file.
        
        Arguments:
        str -- the string to indent
        indent_same_level -- -1 to decrease, 0 to retain, 1 to increase the indent level
        dedent_after -- True to decrease indent after or False to decrease indent before
        """
        s = self.getIndent(dedent_after)

        # in_out_same = 1, increase indent for next time
        # in_out_same = -1, decrease indent for next time
        # if 0, leave indent alone

        if(indent_level > 0):
            self._current_level += 1
        elif(indent_level < 0):
            self._current_level -= 1

        return "{0}{1}".format(s, str)


if __name__ == '__main__':
    print("Library module. Not directly callable.")
