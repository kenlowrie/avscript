#!/usr/bin/env python

from re import findall, compile, IGNORECASE

from .debug import Debug
from .regex import Regex, RegexMD
from .utility import HtmlUtils
from .exception import LogicError, NestingError


class DummyNamespaces(object):
    def exists(self, s):
        return False


class Markdown(object):
    _max_nesting_level = 25     # arbitrary
    def __init__(self):
        self._current_nesting_level = 0
        # Dictionary of each markdown type that we process on each line
        self._regex_markdown = {
            'vars': RegexMD(r'(\[(\w[^[\]\)]*)([\(](.+?)[\)])?\](?!(\=(.+))))', None),
            'strong': RegexMD(r'(\*{2}(?!\*)(.+?)\*{2})', '<strong>{0}</strong>'),
            'emphasis': RegexMD(r'(\*(.+?)\*)', '<em>{0}</em>'),
            'ins': RegexMD(r'(\+{2}(.+?)\+{2})', '<ins>{0}</ins>'),
            'del': RegexMD(r'(\~{2}(.+?)\~{2})', '<del>{0}</del>')
        }
        #self._special_parameter = Regex(r'([\w]+)\s*=\s*\"(.*?)(?<!\\)\"(?=[,|\s)])') 
        self._special_parameter = Regex(r'([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')
        self._namespaces = DummyNamespaces()
        self._stripClass = self.DummyStripClass
        self.debug = Debug('markdown')

    def _inc_nesting_level(self):
        self._current_nesting_level += 1
        if self._current_nesting_level > Markdown._max_nesting_level:
            raise NestingError('Expansion nested too deeply')

    def _dec_nesting_level(self):
        self._current_nesting_level -= 1
        if self._current_nesting_level < 0:
            raise LogicError('_current_nesting_level fell below zero')

    def _md_value(self, value):
        last_value = value
        # keep processing until no more expansion happens
        while(1):
            value = self.markdown(value)
            if value == last_value:
                return value
            last_value = value

    def setNSxface(self,ns):
        self._namespaces = ns

    def DummyStripClass(self, s):
            return None, s

    def setStripClass(self,stripClass):
        self._stripClass = stripClass

    def markdown(self, s):
        """
        Apply markdown to the passed string.

        As each line is read, it is inspected for markdown tags and those
        tags are processed on the fly. That way, the line is ready to be
        output without additional processing.

        A copy of the unmodified line is also retained in the main loop,
        since certain parse tags require the use of the original line.
        In those cases, the _markdown() method can be invoked later, to
        apply markdown to specific elements of a given parse type. For
        an example, take a look at the contact parse type.

        Arguments:
            s -- the string to process markdown elements in

        Returns:
            A string that has all the markdown elements applied.
        """

        """
        Start with some helper functions to process each markdown type.
        Each markdown element has a method to handle the specifics. Each
        method is passed the following parameters:

        Arguments:
            m -- a list of the elements parsed for the match. m[0] is
                 the full matched substring within s.
            s -- the string to process
            new_str -- the string used to build the replacement string.
                       Generally of the format 'stuff{}stuff', where
                       'stuff' is markdown, and {} is replaced with the
                       text between the markdown tags.

        Returns:
            Modified string with inline markdown element expanded.
        """
        def md_vars(m, s, new_str):
            """
            Handle inline link and vars: [variable_name]

            See docstring in code for argument information.
            """
            def makeJitAttrs(params):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(params)}
                return d

            self.debug.print("mdvars(<strong>m[0])=</strong><em>{}</em>".format(HtmlUtils.escape_html(m[0])))
            self.debug.print("mdvars(<strong>m[1])=</strong><em>{}</em>".format(HtmlUtils.escape_html(m[1])))
            self.debug.print("mdvars(<strong>s)=</strong><em>{}</em>".format(HtmlUtils.escape_html(s)))
            jit_attrs = None if not m[3] else makeJitAttrs(m[3])
            if self._namespaces.exists(m[1]):
                # Substitute the variable name with the value
                c, v = self._stripClass(self._namespaces.getValue(m[1], jit_attrs))
                v = self._md_value(v)
                if(not c):
                    # print("OLD: {}<br />\nNEW: {}<br />".format(m[0], v))
                    s = s.replace(m[0], v)
                else:
                    s = s.replace(m[0], '<{0}{1}>{2}</{0}>'.format('span', c, v))
            else:
                # No need to do anything here, just leave the unknown link/variable alone
                pass

            return s

        def md_plain(m, s, new_str):
            """
            Handle simple replacement markdown. e.g. *foo* or **bar**, etc.

            See docstring in code for argument information.
            """
            return s.replace(m[0], new_str.format(m[1]))

        # A map linking markdown keys to processor functions
        markdownTypes = [
            ('vars', md_vars),
            ('strong', md_plain),
            ('emphasis', md_plain),
            ('ins', md_plain),
            ('del', md_plain),
        ]

        self._inc_nesting_level()
        self.debug.print("markdown({})".format(HtmlUtils.escape_html(s)))
        # For each type of markdown
        for key, md_func in markdownTypes:
            md_obj = self._regex_markdown[key]
            matches = findall(md_obj.regex, s)    # find all the matches
            for m in matches:
                # for each match, process it
                s = md_func(m, s, md_obj.new_str)

        #print("RETURN: {}".format(s))
        self._dec_nesting_level()
        return s    # return the processed string


if __name__ == '__main__':
    print(Markdown().markdown('++***this is a test***++'))
