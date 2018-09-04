#!/usr/bin/env python

from re import compile, match, error


class Regex(object):
    """Wrapper class for regular expressions."""
    def __init__(self, regex, flags=0):
        """Regex class constructor.

        Compiles the regex string with any required flags for efficiency.
        """
        self.regex = compile(regex, flags)

    def is_match(self, str):
        return match(self.regex, str)


class RegexSafe(Regex):
    def __init__(self, regex, flags=0):
        try:
            super(RegexSafe, self).__init__(regex, flags)
            self.is_valid = True
        except error:
            self.is_valid = False

    def is_match(self, str):
        if self.is_valid:
            return super(RegexSafe, self).is_match(str)

        return None
        
class RegexMD(Regex):
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
        super(RegexMD, self).__init__(regex, flags)
        self.new_str = new_repl_str


class RegexMain(object):
    """This class holds the regular expressions used for the main parsing loop."""
    def __init__(self, starts_new_div, uses_raw_line, allows_class_prefix, test_str, match_str, test_flags=0, match_flags=0):
        """Constructor for the RegexMain class.

        Arguments:
        starts_new_div -- signals whether this regex will stop the peekplaintext() from processing new lines
        uses_raw_line -- signals whether this regex should be applied to the raw line or the marked_down line
        allows_class_prefix -- signals whether this regex can be prefixed with a class override
        test_str -- this is the regex string used to detect if the line is a match
        match_str -- this is the regex string used when parsing the line into groups. If None, uses test_str
        test_flags -- re flags to use when compiling test_str
        match_flags -- re flags to use when compiling match_str
        """
        self.test_str = Regex(test_str, test_flags)
        self.match_str = None if not match_str else Regex(match_str, match_flags)
        self.starts_new_div = starts_new_div
        self.uses_raw_line = uses_raw_line
        self.allows_class_prefix = allows_class_prefix

    def test_regex(self):
        """Return the regex used to test if the current line matches a parse type."""
        return self.test_str.regex

    def match_regex(self):
        """Return the regex used to match a parse type and breakdown the elements.

        If their is no match regex defined, this method returns the regex for
        testing if the line matches a specific parse type."""
        return self.match_str.regex if self.match_str else self.test_str.regex


if __name__ == '__main__':
    print("Library module. Not directly callable.")
