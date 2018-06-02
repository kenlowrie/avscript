#!/usr/bin/env python

from re import compile


class RegexMD(object):
    """This class holds the regular expressions used when applying markdown
    to inline formatting syntax."""
    def __init__(self, regex, new_repl_str, flags=0):
        """Constructor for the RegexMD class.
        
        Arguments:
        regex -- the regex string used to detect markdown in the line
        new_repl_str -- the string that will be used to insert the markdown into 
            the line. If this is None, then the handler for the regex markdown type
            is responsible for constructing the replacement text.
        flags -- flags to re.compile()
        """
        self.regex = compile(regex, flags)
        self.new_str = new_repl_str


class RegexMain(object):
    """This class holds the regular expressions used for the main parsing loop."""
    def __init__(self, starts_new_div, uses_raw_line, allows_class_prefix, test, match):
        """Constructor for the RegexMain class.
        
        Arguments:
        starts_new_div -- signals whether this regex will stop the peekplaintext() from processing new lines
        uses_raw_line -- signals whether this regex should be applied to the raw line or the marked_down line
        allows_class_prefix -- signals whether this regex can be prefixed with a class override
        test_str -- this is the regex string used to detect if the line is a match
        match_str -- this is the regex string used when parsing the line into groups. If None, uses test_str
        """
        self.test_str = compile(test)
        self.match_str = None if not match else compile(match)
        self.starts_new_div = starts_new_div
        self.uses_raw_line = uses_raw_line
        self.allows_class_prefix = allows_class_prefix

    def test_regex(self):
        """Return the regex used to test if the current line matches a parse type."""
        return self.test_str

    def match_regex(self):
        """Return the regex used to match a parse type and breakdown the elements.
        
        If their is no match regex defined, this method returns the regex for
        testing if the line matches a specific parse type."""
        return self.match_str if self.match_str else self.test_str


if __name__ == '__main__':
    print("Library module. Not directly callable.")
