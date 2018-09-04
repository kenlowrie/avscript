#!/usr/bin/env python

"""
This script is a BBEdit-compliant Markup Previewer

Copyright (c) 2018 Ken Lowrie

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

------------------------------------------------------------------------------

When invoked from BBEdit, it reads from sys.stdin, which will be the current
contents of the AV markdown document you are editing, formats it on the fly,
writing out HTML. Using BBEdit's Preview in BBEdit Markup support, you can see
your AV script come to life.

To quickly see how it works, copy "avscript_md.py" and "avscript_md.css":

.. code-block:: rest

    cp avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters
    cp avscript_md.css ~/Library/Application\sSupport\BBEdit\Preview\sCSS

.. note::

    Alternatively, create a symbolic link to these files in your
    forked repository:

.. code-block:: rest

    ln -s /yourpathrepopath/avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters/avscript_md.py
    ln -s /yourpathrepopath/avscript_md.css ~/Library/Application\sSupport\BBEdit\Preview\sCSS/avscript_md.css

And then open "docs/example.md" in BBEdit, Choose Markup|Preview in BBEdit,
and then in the Preview: example.md window:

Select "avscript_md.css" from the CSS: popdown
Select "avscript_md.py" from the Filter: popdown

BAM! You should see a nicely formatted Audio/Visual script. You'll likely see an
error near the top about "Unable to import /.../heading.md". Don't worry, we'll
fix that later.

For now, take a look at userdocs.md (in a BBEdit preview window of course!), and
you'll quickly get up and running with the A/V Script Markdown Processor.

Future - aka Wish List
0. Image (both inline and reference-style) would be nice too.

"""

from re import IGNORECASE, findall, match
from sys import exit
from os.path import isfile

from .avs.line import Line
from .avs.link import LinkDict
from .avs.regex import Regex, RegexMD, RegexMain
from .avs.stdio import StdioWrapper
from .avs.variable import VariableDict, VariableV2Dict, ImageDict
from .avs.variable import Namespaces
from .avs.bookmark import BookmarkList
from .avs.markdown import Markdown
from .avs.htmlformat import HTMLFormatter
from .avs.exception import RegexError, LogicError, FileError


class AVScriptParser(StdioWrapper):
    """
    Parse a text file written in a markdown-like syntax and output HTML.

    Reads a text file (or reads from sys.stdin) and outputs HTML in a format
    suitable for Audio-Visual (AV) scripts. AV Scripts are a type of script
    format used to describe visuals (shots) and the corresponding narrative
    (voiceover) that would accompany the visual when made into a video.
    """
    def __init__(self):
        """
        Initialize the required instance variables for this class.
        """
        super(AVScriptParser, self).__init__()  # Initialize the base class(es)
        self._debug = False
        self._line = Line()             # current line of input
        self._html = HTMLFormatter()    # format HTML output (indent for readability)
        self._lineInCache = False       # if we have a line in the cache
        self._shotListQ = BookmarkList()    # shot list link Q

        self._links = LinkDict()            # dict of links
        self._variables = VariableDict()    # dict of document variables
        self._images = ImageDict()          # dict of image dictionaries
        self._varV2 = VariableV2Dict()      # dict of varv2 dictionaries
        
        self._md = Markdown()               # New markdown support in separate class
        self._ns = Namespaces(self._md.markdown, self._md.setNSxface, oprint=self.oprint)
        #TODO: Clean this up. _stripClass needs to be handled better than this...
        self._md.setStripClass(self._stripClass)

        self._css_class_prefix = Regex(r'\{:([\s]?.\w[^\}]*)\}(.*)')
        self._special_parameter = Regex(r'\s([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')

        # Dictionary of each line type that we can process
        self._regex_main = {
            #                   NewDiv RawLine Prefix   Test Regex                                        Match Regex
            'shot': RegexMain(True, False, True, r'^[-|\*|\+][ ]*(?![-]{2})', r'^[-|\*|\+][ ]*(?![-]{2})(.*)'),
            'div': RegexMain(True, False, True, r'^[-@]{3}[ ]*([\w\.]+)?[ ]*', r'^[-@]{3}[ ]*([\w\.]+)?[ ]*(.*)'),
            'header': RegexMain(True, False, True, r'^([#]{1,6})[ ]*', r'^([#]{1,6})[ ]*(.*)'),
            'alias': RegexMain(True, True, False, r'^\[([^\]]+)\](?=([\=](.+)))', None),
            'import': RegexMain(True, False, False, r'^[@]import[ ]+[\'|\"](.+[^\'|\"])[\'|\"]', None),
            'image': RegexMain(True, True, False, r'^(@image(\s*([\w]+)\s*=\s*\"(.*?)\")+)', None),
            'var': RegexMain(True, True, False, r'^(@var(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None), 
            'set': RegexMain(True, True, False, r'^(@set(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None),
            'code': RegexMain(True, True, False, r'^(@code(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None), 
            'link': RegexMain(True, True, False, r'^(@link(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None), 
            'html': RegexMain(True, True, False, r'^(@html(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None), 
            'dump': RegexMain(True, True, False, r'^(@dump(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)', None),
            'break': RegexMain(True, False, False, r'^[@](break|exit)$', None),
            'raw': RegexMain(True, False, False, r'^@(@|raw)[ ]+(.*)', None),
            'debug': RegexMain(True, False, False, r'^@debug$', None),
            'shotlist': RegexMain(True, False, False, r'^[/]{3}Shotlist[/]{3}', None),
            'variables': RegexMain(True, False, False, r'^[/]{3}Variables[/]{3}', None),
            'dumplinks': RegexMain(True, False, False, r'^[/]{3}Links[/]{3}', None),
 
            'anchor': RegexMain(True, True, False, r'^[@]\+\[([^\]]*)\]', None),
            'links': RegexMain(True, True, False, r'^\[([^\]]+)\]:\(?[ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\)?', None),
            'cover': RegexMain(True, True, False, r'^(@cover(\s+([\w]+)\s*=\s*\"(.*?)\"){0,3})', None),
            'revision': RegexMain(True, True, False, r'^(@revision(\s*([\w]+)\s*=\s*\"(.*?)\"){0,2})', None),
        }

        # Dictionary of each markdown type that we process on each line
        self.____regex_markdown = {
            'inline_links': RegexMD(r'(\[([^\]]+)\]:[ ]*\([ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\))', None),
            'link_to_bookmark': RegexMD(r'([@]\:\[([^\]]*)\]\<{2}([^\>{2}]*)\>{2})', None),
            'links_and_vars': RegexMD(r'(\[([^[\]]+)\](?!(:(.+))|(\=(.+))))', None),
            'automatic_link': RegexMD(r'(<((?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\[?[A-F0-9]*:[A-F0-9:]+\]?)(?::\d+)?(?:/?|[/?]\S+))>)', '<a href=\"{0}\">{0}</a>', IGNORECASE),
            'strong': RegexMD(r'(\*{2}(?!\*)(.+?)\*{2})', '<strong>{0}</strong>'),
            'emphasis': RegexMD(r'(\*(.+?)\*)', '<em>{0}</em>'),
            'ins': RegexMD(r'(\+{2}(.+?)\+{2})', '<ins>{0}</ins>'),
            'del': RegexMD(r'(\~{2}(.+?)\~{2})', '<del>{0}</del>')
        }

    def _regex(self, id):
        """
        Returns the RegexMain object for a specific parse type.

        Arguments:
            id -- the parse type identifier that you want.

        Returns:
            RegexMain Object for parse type if defined.

        Throws exception RegexError() if invalid ID is passed.
        """
        if(id in self._regex_main):
            return self._regex_main[id]

        raise RegexError("ERROR: Invalid regex ID: [{0}]".format(id))

    def _unreadLine(self):
        """
        Mark the current line in the buffer as unread

        This will cause it to be returned on the next call to readline.
        """
        if(self._lineInCache is True):
            raise LogicError("ERROR: _unreadLine called with line in cache.")

        self._lineInCache = True

    def _reprocessLine(self):
        """Reparse the current line if it had markdown
        
        If the processed line and the raw line are different, then some
        type of markdown was applied. Cache the processed line as the
        new 'raw' line, and try again.
        """
        if self._line.original_line.strip() != self._line.current_line.strip():
            #print('reprocess line 0<br />\n{}<br />\n{}<br />'.format(self._line.original_line,self._line.current_line))
            # Save the current css_prefix, cause we'll lose it in _setLineAttrs()
            saved_css_prefix = self._line.css_prefix
            self._setLineAttrs(self._line.current_line)
            # If we had a css prefix on the original line, then put it back.
            # The original css prefix should have precedence, since it was explicit on the
            # outermost line. I hope this is right!
            if saved_css_prefix:
                self._line.css_prefix = saved_css_prefix
            self._unreadLine()
            #print('reprocess line 1<br />\n{}<br />\n{}<br />'.format(self._line.original_line,self._line.current_line))
            return True

        #print('reprocess line failing...<br />')
        return False
            
    def _md_value(self, value):
        i = 25  # shouldn't have more than 25 levels of nesting, right?
        last_value = value
        for i in range(25):
            value = self._markdown(value)
            if value == last_value:
                return value
            last_value = value

        return 'Expansion nested too deeply {}'.format(value)

    def _markdown(self, s):
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

        def md_inline_links(m, s, new_str):
            """
            Handle inline links: [linkname]:(url [optional_title])

            See docstring in code for argument information.
            """
            optTitle = '' if len(m) < 5 or not m[4] else " title=\"{0}\"".format(m[4])
            s = s.replace(m[0], '<a href=\"{0}\"{2}>{1}</a>'.format(m[2], m[1], optTitle))
            self._links.addLink(m[1], m[2], m[4])
            return s

        def md_link_to_bookmark(m, s, new_str):
            """
            Handle converting inline link to bookmark: @:[linkname]<<link_text>>

            See docstring in code for argument information.
            """
            s = s.replace(m[0], '<a href=\"#{0}\">{1}</a>'.format(m[1], m[2]))
            return s

        def md_links_and_vars(m, s, new_str):
            """
            Handle inline link and vars: [link_or_variable_name]

            See docstring in code for argument information.
            """
            if self._links.exists(m[1]):
                # m[0] is an ID for a LINK, apply the link URL to the text
                s = s.replace(m[0], self._links.getLinkMarkup(m[1]))
            elif self._variables.exists(m[1]):
                # m[0] is a variable name; get the variable value
                varValue = self._variables.getText(m[1])
                if self._links.exists(varValue):
                    # There is a link ID by that name, wrap the text with hyperlink
                    s = s.replace(m[0], self._links.getLinkMarkup(varValue, m[1]))
                else:
                    # Substitute the variable name with the value
                    c, v = self._stripClass(self._variables.getText(m[1]))
                    v = self._md_value(v)
                    if(not c):
                        s = s.replace(m[0], v)
                    else:
                        s = s.replace(m[0], '<{0}{1}>{2}</{0}>'.format('span', c, v))
            elif self._images.exists(m[1]):
                s = s.replace(m[0],self._images.getImage(m[1], self._md_value))
            elif self._varV2.exists(m[1]):
                s = s.replace(m[0],self._varV2.getVarV2(m[1], self._md_value))
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
            ('inline_links', md_inline_links),
            ('link_to_bookmark', md_link_to_bookmark),
            ('links_and_vars', md_links_and_vars),
            ('automatic_link', md_plain),
            ('strong', md_plain),
            ('emphasis', md_plain),
            ('ins', md_plain),
            ('del', md_plain),
        ]

        # For each type of markdown
        for key, md_func in markdownTypes:
            md_obj = self._regex_markdown[key]
            matches = findall(md_obj.regex, s)    # find all the matches
            for m in matches:
                # for each match, process it
                s = md_func(m, s, md_obj.new_str)

        return s    # return the processed string

    def _setLineAttrs(self, line):
        """Initialize the data members of the Line() object
        
        In order to properly implement the reprocessLine() method, we need
        to set all the attributes of the Line() as if the marked down line
        was just read from the file. This logic has been placed in a class
        method so it can be used in both places.
        """
        # remember if this line was indented...
        self._line.was_indented = True if match('[ \t]', line) else False

        # save a copy of the original line...
        self._line.original_line = line

        # strip the class, if any, and initialize css_prefix
        self._line.css_prefix, stripped_line = self._stripClass(line.strip())

        # process any markdown
        #self._line.current_line = self._markdown(stripped_line)
        self._line.current_line = self._md.markdown(stripped_line)
        
        # here's a hack! - Causes tests to fail, but didn't look if it's an issue
        # or a side affect of how the test script was using the tags...
        # this seems like a more generic way to handle adding classes via
        # markdown variable substitution, but for now it's being handled inside
        # peekPlainText()
        #new_css_prefix, stripped_line = self._stripClass(line.strip())
        #if new_css_prefix:
        #    self._line.current_line = stripped_line
        #    self._line.css_prefix = new_css_prefix

    def _readNextLine(self):
        """
        Read next line from the current file (or whatever is cached)

        If something is in the cache, return that instead
        """
        if(self._lineInCache):
            self._lineInCache = False    # reset the flag since we are returning it
            return self._line.current_line

        # read the next line from the file buffer
        while(1):
            line = self.ireadline()
            if not line:
                break
            if not line.strip():
                continue
            if line[0:2] != '//':
                break
            if line[0:3] == '///':
                break

        self._setLineAttrs(line)
        #self._line.reprocessed = False

        # return the marked down version
        return self._line.original_line

    def _addBookmark(self, linktext):
        """
        Generate unique HTML bookmark and return the inline <a> tag to define it.

        Arguments:
            linktext -- optional text to wrap the <a> element around.

        Returns:
            HTML <a> element as string: <a id="GENERATED UNIQUE_ID">linktext</a>
        """
        return self._html.formatLine("<a id=\"{0}\"></a>\n".format(self._shotListQ.addBookmark(linktext)))

    def _stripClass(self, line):
        """
        Strip the {:.class} prefix off line, and return tuple of (class, line)

        The class is formatted for use as an HTML class ATTR, along with the
        rest of the line. If no class is present, just return the line as-is.
        """

        def make_CSS_class(tmpClass):
            """Create a proper class="class1 class2" string from .class1.class2 notation.

            Arguments:
                The class(es) specified in the {:.class1.class2} wrapper

            Returns:
                String in proper class attribute format. e.g.:
                    {:.ignore.red} would become ' class="ignore red"'
            """
            # remove all extraneous spaces, then change '.' to ' ' then strip leading blanks
            s = tmpClass.replace(" ", "").replace(".", " ").strip()

            return " class=\"{0}\"".format(s)

        if(match(self._css_class_prefix.regex, line)):
            m = match(self._css_class_prefix.regex, line)

            if(m is not None and len(m.groups()) == 2):
                # format it like this: " class=cls1"
                return make_CSS_class(m.group(1)), m.group(2)

        # no class found, so return '' and the line, as-is
        return '', line

    def _peekNextLine(self, element="p", addLinks=False):
        """
        Read next line, and if indented, add it as a new <element>

        If the next line has white space at the beginning, then add it to the
        current line as a new <p> or whatever 'element' is. Then keep looking,
        in case there are more indented lines. This allows us to have multiple
        lines for DIVs that are section headers, and it's also used to gather
        multiple shots when we are processing an AV DIV.
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF, return ''

        # if line was indented, it's part of the previous element
        if self._line.was_indented:
            # get the link anchor and insert it ahead of the shot
            link = "" if not addLinks else self._addBookmark(self._line.current_line)
            # return this, but call myself recursively in case there are more indented lines...
            return self._html.formatLine("{3}<{0}{2}>{1}</{0}>\n".format(element, self._line.current_line.rstrip('\n'), self._line.css_prefix, link) + self._peekNextLine(element, addLinks))

        # We read 1 too many lines, so mark the cache as dirty so we can process it next time.
        self._unreadLine()
        return ""

    def _peekPlainText(self, element="p"):
        """
        Gobble up all the normal lines after one or more shot descriptions.

        "Normal" lines are the voiceover (VO) or narration that goes along with
        each shot. Usually, there are more "VO lines" than shots, so we want to
        read them all, and place them within the same DIV section. Each of these
        narrative lines can have it's own class override...
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF return ''

        # This internal API detects if the next line is some type of BREAK.
        # e.g. a section, new shot, heading or link...
        def isNewSection(lineObj):
            """Determines if the current line is the start of a new section.

            Arguments:
                lineObj -- a Line() instance

            Returns:
                True -- if the current line should start a new section
                False -- if the current line is part of the current section
            """
            # Look to see if the current line in the cache is the start of a new section

            for id in self._regex_main:
                obj = self._regex(id)
                # Make sure that this regex obj starts_new_div.
                if(not obj.starts_new_div):
                    continue
                # if this RE allows a class prefix, use the line with the
                # prefix stripped off, otherwise, use the original line.
                if match(obj.test_str.regex, lineObj.current_line if obj.allows_class_prefix else lineObj.original_line):
                    return True

            return False

        # if it's not a new section, keep it and peek at next line
        if not isNewSection(self._line):
            # add this line to the current DIV, and keep reading until we hit some
            # type of break element...
            if not self._line.css_prefix:
                # if there isn't a css_prefix inline, check to see if one was added
                # via markdown processing...
                new_prefix, new_line = self._stripClass(self._line.current_line)
                if new_prefix:
                    # if the markdown added a css prefix, then adjust the _line object
                    # so the css_prefix and current_line are updated before we format
                    # the element.
                    self._line.css_prefix = new_prefix
                    self._line.current_line = new_line

            return self._html.formatLine("<{0}{2}>{1}</{0}>\n".format(element, self._line.current_line, self._line.css_prefix) + self._peekPlainText(element))

        # read one too many lines, so cache the current line for the next time around...
        self._unreadLine()
        return ""

    def _printInExtrasDiv(self, str):
        """
        Print the string argument inside an HTML DIV Element with class="extras"

        This allows orphaned elements to be kept out of the shot/narrative
        sections, where floats are active.
        """
        self.oprint(self._html.formatLine("<div class=\"extras\">", 1))
        self.oprint(self._html.formatLine(str, -1))
        self.oprint(self._html.formatLine("</div>"))

    def parse(self):
        """Parse an A/V Script File in text format and emit HTML code."""

        """
        Following are the helper functions for the parse() method.

        testLine() and matchLine() are used in the main loop below, and
        then each line parse type has a method that can process it and
        output the HTML that goes with it.
        """
        def testLine(regex_obj, line_obj):
            """See if the current line matches the test_regex() expression."""
            line = line_obj.current_line if not regex_obj.uses_raw_line else line_obj.original_line
            return match(regex_obj.test_regex(), line)

        def matchLine(regex_obj, line_obj):
            """See if the current line matches the match_regex() expression."""
            line = line_obj.current_line if not regex_obj.uses_raw_line else line_obj.original_line
            return match(regex_obj.match_regex(), line)

        def handle_shot(m, lineObj):
            """Handle a shot parse line"""
            if(m is not None):
                li = "" if len(m.groups()) < 1 else "%s" % m.group(1)
                divstr = self._html.formatLine("<div class=\"av\">\n", 1)
                divstr += self._addBookmark(li)
                divstr += self._html.formatLine("<ul>\n", 1)
                divstr += self._html.formatLine("<li{1}>{0}</li>\n".format(li, lineObj.css_prefix))
                divstr += self._peekNextLine("li", True)
                divstr += self._html.formatLine("</ul>\n", -1, False)
                divstr += self._peekPlainText()
                divstr += self._html.formatLine("</div>", -1, False)
                self.oprint(divstr)
            else:
                self.oprint(lineObj.current_line)

        def handle_div(m, lineObj):
            """handle a DIV parse line"""
            if(m is not None):
                divClas = "" if not lineObj.css_prefix else lineObj.css_prefix
                divPcls = "" if len(m.groups()) < 1 or m.group(1) == "." else " class=\"%s\"" % m.group(1)
                divText = "" if len(m.groups()) < 2 else "%s\n" % m.group(2)
                divstr = self._html.formatLine("<div%s>\n" % divClas, 1)
                divstr += self._html.formatLine("<p%s>%s</p>\n" % (divPcls, divText.rstrip('\n')))
                divstr += self._peekNextLine()
                divstr += self._html.formatLine("</div>", -1, False)

                self.oprint(divstr)

            else:
                self.oprint(lineObj.current_line)

        def handle_header(m, lineObj):
            """Handle a header parse line"""
            if(m is not None and len(m.groups()) > 1):
                hnum = len(m.group(1))
                self._printInExtrasDiv("<h{0}{2}>{1}</h{0}>".format(hnum, m.group(2).strip(), lineObj.css_prefix))
            else:
                self.oprint(lineObj.current_line)

        def handle_import(m, lineObj):
            """Handle an import parse line"""
            if(m is not None and len(m.groups()) == 1):
                try:
                    self.iopen(m.group(1))
                except FileError as fe:
                    self.oprint(fe.errmsg)

        def handle_break(m, lineObj):
            """Handle a break parse line"""
            pass    # don't do anything with @break or @exit

        def handle_raw(m, lineObj):
            """Handle a raw line"""
            #TODO: Make this available everywhere...
            def esc_html(x):
                return x.replace('<','&lt;').replace('>','&gt;').replace('&','&amp;')
            if(m is not None):
                if self._debug:
                    self.oprint('&nbsp;&nbsp;lineObj.current_line=<br />{}<br />&nbsp;&nbsp;m.group(2)=<br />{}'.format(esc_html(lineObj.current_line),esc_html(m.group(2))))
                self.oprint(self._html.formatLine(self._md.markdown(m.group(2))))
            else:
                self.oprint(lineObj.current_line)

        def handle_debug(m, lineObj):
            """Handle a debug line"""
            self.oprint("Entering Debug Mode<br />")
            self._debug = True

        def handle_shotlist(m, lineObj):
            """Handle a shotlist parse line."""
            self.oprint(self._html.formatLine("<div class=\"shotlist\">", 1))
            self.oprint(self._html.formatLine("<hr />"))
            self.oprint(self._html.formatLine("<p>Shotlist</p>"))
            self.oprint(self._html.formatLine("<code>", 1))
            shotnum = 1
            for shot in self._shotListQ.getBookmarkList():
                self.oprint(self._html.formatLine("<div class=\"shot\">", 1))
                self.oprint(self._html.formatLine("<p>{1}&#160;<a class=\"shotlist-backref\" href=\"#{0}\" rel=\"tag\" title=\"Jump back to shot {2} in the script\">&#8617;</a></p>".format(shot[0], shot[1], shotnum), -1))
                self.oprint(self._html.formatLine("</div>"))
                shotnum += 1

            self.oprint(self._html.formatLine("</code>", -1, False))
            self.oprint(self._html.formatLine("</div>", -1, False))

        def handle_variables(m, lineObj):
            """Handle the variables parse line"""
            self.oprint(self._html.formatLine("<div class=\"variables\">", 1))
            self.oprint(self._html.formatLine("<code>", 1))
            self._ns.dumpVars()
            self.oprint(self._html.formatLine("</code>", -1, False))
            self.oprint(self._html.formatLine("</div>", -1, False))

        def handle_dumplinks(m, lineObj):
            """Handle the dumplinks parse line"""
            self.oprint(self._html.formatLine("<div class=\"links\">", 1))
            self.oprint(self._html.formatLine("<hr />"))
            self.oprint(self._html.formatLine("<p>External Links</p>"))
            self.oprint(self._html.formatLine("<code>", 1))
            self._links.dumpLinks(self._html.getIndent(), self.oprint)
            self.oprint(self._html.formatLine("</code>", -1, False))
            self.oprint(self._html.formatLine("</div>", -1, False))

        def handle_links(m, lineObj):
            """Handle the links parse line"""
            optTitle = '' if len(m.groups()) < 4 or not m.group(4) else m.group(4)

            if(m is not None and len(m.groups()) == 4):
                self._links.addLink(m.group(1), self._md.markdown(m.group(2)), optTitle)
                # self.oprint("RL:AL:{0}{1}{2}<br />".format(m.group(1),m.group(2),m.group(3)))
            else:
                self.oprint(lineObj.original_line)

        def handle_alias(m, lineObj):
            """Handle the alias parse line type"""
            if(m is not None and len(m.groups()) == 3):
                #self._variables.addVar(m.group(1), self._markdown(m.group(3)))
                #TODO: Should m.group(3) be self._md.markdown(m.group(3))?
                self._ns.addVariable(self._md.markdown(m.group(3)), name=m.group(1), ns="basic")
            else:
                self.oprint(lineObj.original_line)

        def handle_anchor(m, lineObj):
            """Handle an anchor parse line type"""
            # For this case, we just need to drop an anchor.
            if(m is not None and len(m.groups()) == 1):
                self.oprint(self._html.formatLine("<a id=\"{0}\"></a>".format(m.group(1))))
            else:
                self.oprint(lineObj.original_line)

        def handle_cover(m, lineObj):
            """Handle the cover parse line type"""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                fmt = lambda x: "{0}".format(self._md.markdown(d.get(x))) if d.get(x) else ""

                divstr = self._html.formatLine("<div class=\"cover\">\n", 1)
                divstr += self._html.formatLine("<h3>{}</h3>\n".format(fmt("title")))
                divstr += self._html.formatLine("<p>{}</p>\n".format(fmt("author")))
                divstr += self._html.formatLine("<p class=\"coverSummary\">{}</p>\n".format(fmt("logline")))
                divstr += self._html.formatLine("</div>", -1, False)

                self.oprint(divstr)
            else:
                self.oprint(lineObj.original_line)

        def handle_revision(m, lineObj):
            """Handle the revision parse line type"""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                fmt = lambda x: "{0}".format(self._md.markdown(d.get(x))) if d.get(x) else ""

                ts_key = "timestamp"

                if d.get(ts_key) and d.get(ts_key).lower() in ['false', 'no', 'off', '0']:
                    ts_str = ""
                else:
                    from time import strftime
                    ts_str = " ({})".format(strftime("%Y%m%d @ %H:%M:%S"))

                divstr = self._html.formatLine("<div class=\"revision\">\n", 1)
                divstr += self._html.formatLine("<p class=\"revTitle\">Revision: {0}{1}</p>\n".format(fmt("v").rstrip(), ts_str), -1)
                divstr += self._html.formatLine("</div>")

                self.oprint(divstr)
            else:
                self.oprint(lineObj.original_line)

        def handle_dump(m, lineObj):
            """Handle the dump parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                fmt = lambda x: "{0}<br />".format(self._md.markdown(d.get(x))) if d.get(x) else ""

                self.oprint(self._html.formatLine("<div class=\"variables\">", 1))
                self.oprint(self._html.formatLine("<code>", 1))
                if d.get('all') and d.get('all').lower() in ['*', '1', 'y', 'yes', 't', 'true']:
                    self._ns.dumpVars()
                else:
                    self._ns.dumpNamespaces(d)
                self.oprint(self._html.formatLine("</code>", -1, False))
                self.oprint(self._html.formatLine("</div>", -1, False))
            else:
                self.oprint(lineObj.original_line)

        def handle_varv2(m, lineObj):
            """Handle the @var parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                #self._varV2.addVarV2(d.copy(), self.oprint)
                self._ns.addVariable(d, ns="var")

            else:
                self.oprint(lineObj.original_line)

        def handle_setv2(m, lineObj):
            """Handle the @set parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                #self._varV2.updateVarV2(d.copy(), self.oprint)
                #TODO: This needs to have an option for "finding namespace"
                self._ns.updateVariable(d, ns="var")

            else:
                self.oprint(lineObj.original_line)

        def handle_image(m, lineObj):
            """Handle the @image parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                #self._images.addImage(d.copy(), self.oprint)
                self._ns.addVariable(d, ns="image")

            else:
                self.oprint(lineObj.original_line)

        def handle_link(m, lineObj):
            """Handle the @link parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                self._ns.addVariable(d, ns="link")

            else:
                self.oprint(lineObj.original_line)

        def handle_html(m, lineObj):
            """Handle the @html parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                self._ns.addVariable(d, ns="html")

            else:
                self.oprint(lineObj.original_line)

        def handle_code(m, lineObj):
            """Handle the @code parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #fmt = lambda x: "{0}<br />".format(self._markdown(d.get(x))) if d.get(x) else ""
                # TODO: What about self.oprint()? Doesn't that need to be passed to NS?
                self._ns.addVariable(d, ns="code")

            else:
                self.oprint(lineObj.original_line)

        # --------------------------------------------------------------------
        # This is the ENTRY point to the parse() method!
        rc = 0

        # A map linking line parse types to processor functions
        parseTypes = [
            ('shot', handle_shot),
            ('div', handle_div),
            ('header', handle_header),
            ('import', handle_import),
            ('image', handle_image),
            ('var', handle_varv2),
            ('set', handle_setv2),
            ('code', handle_code),
            ('link', handle_link),
            ('html', handle_html),
            ('break', handle_break),
            ('raw', handle_raw),
            ('shotlist', handle_shotlist),
            ('variables', handle_variables),
            ('dumplinks', handle_dumplinks),
            ('alias', handle_alias),
            ('debug', handle_debug),
            ('dump', handle_dump),

            ('links', handle_links),
            ('anchor', handle_anchor),
            ('cover', handle_cover),
            ('revision', handle_revision),
        ]
        
        try:
            # Print the outer DIV header
            self.oprint(self._html.formatLine("<div class=\"wrapper\">", 1))

            # Read the file until EOF and parse each line
            while(self._readNextLine() != ''):
                # For each parse type
                matched = False
                for key, parse_func in parseTypes:
                    parse_obj = self._regex_main[key]
                    if(testLine(parse_obj, self._line)):
                        m = matchLine(parse_obj, self._line)
                        parse_func(m, self._line)
                        matched = True
                        break

                # if no parse type was matched, then handle this as a
                # line that should be printed in an extras DIV...
                if not matched and self._line.current_line.rstrip() and not self._reprocessLine():
                    divstr = self._line.current_line
                    # divstr += self._peekPlainText("span")
                    self._printInExtrasDiv("<p{1}>{0}</p>".format(divstr, self._line.css_prefix))

            # Now close off the outer DIV from above.
            self.oprint(self._html.formatLine("</div>", -1, False))

        except RegexError as regex_error:
            self.oprint("{}".format(regex_error.errmsg))
            rc = 3

        return rc

    def open_and_parse(self, avscript=None):
        """Open an A/V Script File in text format and emit HTML code.

        Arguments:
        avscript -- the script to parse or None to parse sys.stdin
        """
        # Ok, open the specified file (or sys.stdin if avscript is None)
        try:
            if(avscript is not None):
                # If the file doesn't exist, bail now.
                if not isfile(avscript):
                    return 1

            self.iopen(avscript)

        except IOError:
            return 2

        # Set the flags saying whether we started with stdin or a file
        self.isetio(True if avscript is None else False)
        return self.parse()


def av_parse_file(args=None):
    """Parse specified input file as AV Script Format text file.

    if args is None, uses sys.argv - via argparse
    if no filename is specified, parses sys.stdin

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Parse AV Format text files into HTML format.',
                            epilog='If filename is not specified, program reads from stdin.')
    parser.add_argument('-f', '--filename', help='the file that you want to parse')
    args = parser.parse_args(args)

    return AVScriptParser().open_and_parse(args.filename)


if __name__ == '__main__':
    exit(av_parse_file())
