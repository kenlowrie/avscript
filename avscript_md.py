#!/usr/bin/env python

"""
This script is a BBEdit-compliant Markup Previewer (if that's a thing)... When
invoked from BBEdit, it reads from sys.stdin, which will be the current contents
of the markdown document you are editing, formats it on the fly, writing out
HTML. Using BBEdit's Preview in BBEdit Markup support, you can see your AV
script come to life.

To quickly see how it works, copy "avscript_md.py" and "avscript_md.css":

cp avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters
cp avscript_md.css ~/Library/Application\sSupport\BBEdit\Preview\sCSS

And then open "example.md" in BBEdit, Choose Markup|Preview in BBEdit, and then
in the Preview: example.md window:

Select "avscript_md.css" from the CSS: popdown
Select "avscript_md.py" from the Filter: popdown

BAM! You should see a nicely formatted Audio/Visual script. You'll likely see
error near the top about "Unable to import /.../heading.md". Don't worry, we'll
fix that later.

For now, take a look at userdocs.md (in a BBEdit preview window of course!), and
you should quickly get up and running with the A/V Script Markdown Processor.

Future - aka Wish List
0. Image (both inline and reference-style) would be nice too.


TODO (Punch list):
4. Finish the documentation for this thing
5. Test with Python2 and Python3
6. Make it pass flake8 (mostly)

a. Search for TODO and fix/cleanup
b. Improve markdown parsing to take advantage of group(0) like links does???

CSS Clean Up
1. Reorganize, make consistent.
2. Make it pass lint
3. Add more useful styles
4. Create multiple versions: All, Visuals and Narration only, User Guide
5. Ability to pass requested version to mkavscript_md

"""

import re

from sys import exit
from os.path import isfile

from avs.file import FileHandler
from avs.link import LinkDict
from avs.variable import VariableDict
from avs.bookmark import BookmarkList
from avs.htmlformat import HTMLFormatter
from avs.exception import *


class RegexMD(object):
    """
    This class is used to hold the regular expressions that are used when
    applying markdown to inline formatting codes.
    """
    def __init__(self, regex, ori_repl_str, new_repl_str, flags=0):
        self.regex = re.compile(regex, flags)
        self.ori_str = ori_repl_str
        self.new_str = new_repl_str


class RegexMain(object):
    """
    starts_new_div - signals whether this regex will stop the peekplaintext() from processing new lines
    uses_raw_line - signals whether this regex should process the raw line or the marked_down line
    allows_class_prefix - signals whether this regex can be prefixed with a class override
    test_str - this is the regex string used to detect if the line is a match
    match_str - this is the regex string used when parsing the line into groups. If None, uses test_str
    """
    def __init__(self, starts_new_div, uses_raw_line, allows_class_prefix, test, match):
        self.test_str = re.compile(test)
        self.match_str = None if not match else re.compile(match)
        self.starts_new_div = starts_new_div
        self.uses_raw_line = uses_raw_line
        self.allows_class_prefix = allows_class_prefix

    def test_regex(self):
        return self.test_str

    def match_regex(self):
        return self.match_str if self.match_str else self.test_str


class AVScriptParser(object):
    """Parse a text file written in a markdown-like syntax and output HTML.
    
    Reads a text file (or reads from sys.stdin) and outputs HTML in a format suitable
    for Audio-Visual (AV) scripts. AV Scripts are a type of script format used to describe
    visuals (shots) and the corresponding narrative (voiceover) that would accompany the
    visual when made into a video. 
    """
    def __init__(self):
        """The constructor for the class. Initialize the required member variables."""
        self._line = None                # the current line "marked down"
        self._ori_line = None            # the current line as it was read in
        self._html = HTMLFormatter()     # format HTML output (indent for readability)
        self._lineInCache = False        # if we have a line in the cache
        self._av = FileHandler()         # file handler stack
        self._shotListQ = BookmarkList() # shot list link Q

        self._links = LinkDict()         # dict of links
        self._variables = VariableDict() # dict of document variables

        self._regex_main = {
            #                   NewDiv RawLine Prefix   Test Regex                                        Match Regex
            'shot': RegexMain(True, False, True, r'^[-|\*|\+][ ]*(?![-]{2})', r'^[-|\*|\+][ ]*(?![-]{2})(.*)'),
            'div': RegexMain(True, False, True, r'^[-@]{3}[ ]*([^\s]+)[ ]*([\w\.]+)?[ ]*', r'^[-@]{3}[ ]*([^\s]+)[ ]*([\w\.]+)?[ ]*(.*)'),
            'h#': RegexMain(True, False, True, r'^([#]{1,6})[ ]*', r'^([#]{1,6})[ ]*(.*)'),
            'links': RegexMain(True, True, False, r'^\[([^\]]+)\]:\(?[ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\)?', None),
            'alias': RegexMain(True, True, False, r'^\[([^\]]+)\](?=([\=](.+)))', None),
            'import': RegexMain(True, False, False, r'^[@]import[ ]+[\'|\"](.+[^\'|\"])[\'|\"]', None),
            'anchor': RegexMain(True, True, False, r'^[@]\+\[([^\]]*)\]', None),
            'shotlist': RegexMain(True, False, False, r'^[/]{3}Shotlist[/]{3}', None),
            'variables': RegexMain(True, False, False, r'^[/]{3}Variables[/]{3}', None),
            'dumplinks': RegexMain(True, False, False, r'^[/]{3}Links[/]{3}', None),
            'cover': RegexMain(True, True, False, r'^[\$]{2}cover[\$]{2}:(.*)', r'^[\$]{2}cover[\$]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}'),
            'revision': RegexMain(True, True, False, r'^[\$]{2}revision[\$]{2}:(.*)', r'^[\$]{2}revision[\$]{2}:[\<]{2}(.[^\>]*)[\>]{2}'),
            'contact': RegexMain(True, True, False, r'^[\$]{2}contact[\$]{2}:(.*)', r'^[\$]{2}contact[\$]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}'),
        }

        self._regex_md_list = [
            # Next one is to match LINK & ALIAS substitutions, but NOT DEFs.
            RegexMD(r'\[([^\]]+)\](?!(:(.+))|(\=(.+)))', '[{0}]', None),
            # TODO: Next one kind of complex. Do we need this?
            RegexMD(r'<((?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\[?[A-F0-9]*:[A-F0-9:]+\]?)(?::\d+)?(?:/?|[/?]\S+))>', '<{0}>', '<a href=\"{0}\">{0}</a>', re.IGNORECASE),
            RegexMD(r'\*{2}(?!\*)(.+?)\*{2}', '**{0}**', '<strong>{0}</strong>'),
            RegexMD(r'\*(.+?)\*', '*{0}*', '<em>{0}</em>'),
            RegexMD(r'\+{2}(.+?)\+{2}', '++{0}++', '<ins>{0}</ins>'),
            RegexMD(r'\~{2}(.+?)\~{2}', '~~{0}~~', '<del>{0}</del>')
        ]

    def _regex(self, id):
        if(id in self._regex_main):
            return self._regex_main[id]

        raise RegexError("ERROR: Invalid regex ID: [{0}]".format(id))

    def _unreadLine(self):
        """Mark the current line in the buffer as unread, so it will be returned next time."""
        self._lineInCache = True

    def _markdown(self, s):
        """This method is used to apply markdown to the passed in string."""

        # TODO: nice if we could integrate this into main loop...
        # This handles inline links in this format: [linkID]:(url)
        # Might be able to fix if I can eliminate the extra group... linkID,(url),url
        spec = RegexMD(r'(\[([^\]]+)\]:[ ]*\([ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\))', '', '')

        # This special case handles inline links
        matches = re.findall(spec.regex, s)
        for m in matches:
            optTitle = '' if len(m) < 5 or not m[4] else " title=\"{0}\"".format(m[4])
            s = s.replace(m[0], '<a href=\"{0}\"{2}>{1}</a>'.format(m[2], m[1], optTitle))
            self._links.addLink(m[1], m[2], m[4])
            # print("MD:AL:{0}{1}{2}<br />".format(m[1],m[2],m[3]))

        # TODO: nice if this were also integrated into main loop...
        # This handles inline links to local anchors: @:[anchorID]<<text>>
        # This special case handles links to local anchors
        spec = RegexMD(r'([@]\:\[([^\]]*)\]\<{2}([^\>{2}]*)\>{2})', '', '')

        matches = re.findall(spec.regex, s)
        for m in matches:
            s = s.replace(m[0], '<a href=\"#{0}\">{1}</a>'.format(m[1], m[2]))
            # print("MD:AA:{0}{1}{2}<br />".format(m[0],m[1],m[2]))

        for item in self._regex_md_list:
            matches = re.findall(item.regex, s)
            for m in matches:
                # if item.new_str is None, it means we have a link or a variable
                if item.new_str is None:
                    # If m[0] is an ID for a LINK, then replace apply the link URL to the text
                    if self._links.exists(m[0]):
                        s = s.replace(item.ori_str.format(m[0]), self._links.getLinkMarkup(m[0]))
                    elif self._variables.exists(m[0]):
                        # Get the variable value
                        varValue = self._variables.getText(m[0])
                        # See if there is a link ID by that name
                        if self._links.exists(varValue):
                            s = s.replace(item.ori_str.format(m[0]), self._links.getLinkMarkup(varValue, m[0]))
                        else:
                            s = s.replace(item.ori_str.format(m[0]), self._variables.getText(m[0]))
                    else:
                        pass    # TODO: should we do anything here?
                else:
                    # These are the simple search/replace expressions...
                    s = s.replace(item.ori_str.format(m), item.new_str.format(m))

        return s

    def _readNextLine(self):
        """Read the next line from the buffer, unless something is cached, in which case return that"""
        if(self._lineInCache):
            self._lineInCache = False    # reset the flag since we are returning it
            return self._line
        # read the next line from the file buffer
        while(1):
            self._ori_line = self._av.readline()
            if self._ori_line[0:2] != '//':
                break
            if self._ori_line[0:3] == '///':
                break

        # mark it down
        self._line= self._markdown(self._ori_line)
        # return the marked down version
        return self._line
        
    def _addBookmark(self, link):
        return self._html.formatLine("<a id=\"{0}\"></a>\n".format(self._shotListQ.addBookmark(link)))

    def _makeCSSclass(self, tmpClass):
        # remove all extraneous spaces, then change '.' to ' ' then strip leading blanks
        s = tmpClass.replace(" ", "").replace(".", " ").strip()

        return " class=\"{0}\"".format(s)

    def _stripClass(self, line):
        """Strip the {:.class} prefix off the line, and return the class formatted
           for use as an HTML class ATTR, along with the rest of the line. If no
           class is present, just return the line as-is."""
        if(re.match(r'\{:([\s]?.\w[^\}]*)\}(.*)', line)):
            regex = r'\{:([\s]?.\w[^\}]*)\}(.*)'
            m = re.match(regex, line)

            if(m is not None and len(m.groups()) == 2):
                # format it like this: " class=cls1"
                return self._makeCSSclass(m.group(1)), m.group(2)

        # no class found, so return '' and the line, as-is
        return '', line

    def _peekNextLine(self, element="p", addLinks=False):
        """Read the next line, and if it's got white space at the beginning, then add it to the
           current line as a new <p> or whatever 'element' is. Then keep looking, in case there
           are more indented lines. This allows us to have multiple lines for DIVs that are section
           headers, and it's also used to gather multiple shots when we are processing an AV DIV."""
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF, return ''

        if re.match('[ \t]', self._line):
            # line was indented, strip any leading space, and then indent it at current level
            self._line= self._line.strip()
            cssClass, rest = self._stripClass(self._line)
            # get the link anchor and insert it ahead of the shot
            link = "" if not addLinks else self._addBookmark(rest)
            # return this, but call myself recursively in case there are more indented lines...
            return self._html.formatLine("{3}<{0}{2}>{1}</{0}>\n".format(element, rest.rstrip('\n'), cssClass, link) + self._peekNextLine(element, addLinks))

        # We read 1 too many lines, so mark the cache as dirty so we can process it next time.
        self._unreadLine()
        return ""

    def _peekPlainText(self, element="p"):
        """Gobble up all the normal lines after one or more shot descriptions. "Normal"
           lines are the voiceover or narration that goes along with each shot. It's
           common that there are more "lines" than shots, so we want to read them all,
           and place them within the same DIV section. Each of these narrative lines
           can have it's own class override...
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF return ''

        # This internal API detects if the next line is some type of BREAK.
        # e.g. a section, new shot, heading or link...

        def isNewSection(line, ori_line):
            # Look to see if the current line in the cache is the start of a new section

            for id in self._regex_main:
                obj = self._regex(id)
                # Make sure that this regex obj starts_new_div.
                if(not obj.starts_new_div):
                    continue
                # if this RE allows a class prefix, use the line with the
                # prefix stripped off, otherwise, use the original line.
                if re.match(obj.test_str, line if obj.allows_class_prefix else ori_line):
                    return True

            return False

        # Strip class, check the raw line to see if we should break
        tCls, tRst = self._stripClass(self._ori_line.strip())

        # if the RAW line is empty or if it's not a new section,
        #   keep it and peek at next line
        if not tRst or not isNewSection(tRst, self._ori_line.strip()):
            tmpClass, rest = self._stripClass(self._line.strip())
            # add this line to the current DIV, and keep reading until we hit some
            # type of break element...
            return self._html.formatLine("<{0}{2}>{1}</{0}>\n".format(element, rest, tmpClass) + self._peekPlainText(element))

        # read one too many lines, so cache the current line for the next time around...
        self._unreadLine()
        return ""

    def _printInExtrasDiv(self, str):
        """Print the passed in string inside of a DIV with ID="extras". This allows
           orphaned elements to be kept out of the shot/narrative sections, where
           floats are active."""
        print(self._html.formatLine("<div id=\"extras\">", 1))
        print(self._html.formatLine(str, -1))
        print(self._html.formatLine("</div>"))

    def parse(self):
        def testLine(regex_obj, line_obj):
            line = line_obj.curLine if not regex_obj.uses_raw_line else line_obj.oriLine
            return re.match(regex_obj.test_regex(), line)

        def matchLine(regex_obj, line_obj):
            line = line_obj.curLine if not regex_obj.uses_raw_line else line_obj.oriLine
            return re.match(regex_obj.match_regex(), line)

        rc = 0

        try:
            print(self._html.formatLine("<div id=\"wrapper\">", 1))
            while(self._readNextLine() != ''):
                # DOC this entire method better...
                # Start by stripping any class override from the beginning of the line
                cssClass, curLine = self._stripClass(self._line)

                # TODO: would this (a line class) be better to help doc code below?
                class C_LineObj:
                    def __init__(self, curLine, oriLine):
                        self.curLine = curLine
                        self.oriLine = oriLine

                lineObj = C_LineObj(curLine, self._ori_line)

                if (testLine(self._regex('shot'), lineObj)):
                    m = matchLine(self._regex('shot'), lineObj)

                    if(m is not None):
                        li = "" if len(m.groups()) < 1 else "%s" % m.group(1)
                        divstr = self._html.formatLine("<div id=\"av\">\n", 1)
                        divstr += self._html.formatLine("<ul>\n", 1)
                        divstr += self._addBookmark(li)
                        divstr += self._html.formatLine("<li{1}>{0}</li>\n".format(li, cssClass))
                        divstr += self._peekNextLine("li", True)
                        divstr += self._html.formatLine("</ul>\n", -1, False)
                        divstr += self._peekPlainText()
                        divstr += self._html.formatLine("</div>", -1, False)
                        print(divstr)
                    else:
                        print(curLine)

                elif(testLine(self._regex('div'), lineObj)):
                    m = matchLine(self._regex('div'), lineObj)

                    if(m is not None):
                        divID = "" if len(m.groups()) < 1 else " id=\"{0}\"{1}".format(m.group(1), cssClass)
                        divPcls = "" if len(m.groups()) < 2 or m.group(2) == "." else " class=\"%s\"" % m.group(2)
                        divText = "" if len(m.groups()) < 3 else "%s\n" % m.group(3)
                        divstr = self._html.formatLine("<div%s>\n" % divID, 1)
                        divstr += self._html.formatLine("<p%s>%s</p>\n" % (divPcls, divText.rstrip('\n')))
                        divstr += self._peekNextLine()
                        divstr += self._html.formatLine("</div>", -1, False)

                        print(divstr)

                    else:
                        print(curLine)

                elif(testLine(self._regex('h#'), lineObj)):
                    m = matchLine(self._regex('h#'), lineObj)

                    if(m is not None and len(m.groups()) > 1):
                        hnum = len(m.group(1))
                        self._printInExtrasDiv("<h{0}{2}>{1}</h{0}>".format(hnum, m.group(2).strip(), cssClass))
                    else:
                        print(curLine)

                elif(testLine(self._regex('import'), lineObj)):
                    m = matchLine(self._regex('import'), lineObj)
                    if(m is not None and len(m.groups()) == 1):
                        try:
                            self._av.open(m.group(1))
                        except FileError as fe:
                            print(fe.errmsg)

                    # TODO: Need to handle error here and print if we cannot open the file, etc.

                elif(testLine(self._regex('shotlist'), lineObj)):
                    print(self._html.formatLine("<div class=\"shotlist\">", 1))
                    print(self._html.formatLine("<hr />"))
                    shotnum = 1
                    for shot in self._shotListQ.getBookmarkList():
                        print(self._html.formatLine("<div id=\"shot\">", 1))
                        print(self._html.formatLine("<p>{1}&#160;<a class=\"shotlist-backref\" href=\"#{0}\" rev=\"shotlist\" title=\"Jump back to shot {2} in the script\">&#8617;</a></p>".format(shot[0], shot[1], shotnum), -1))
                        print(self._html.formatLine("</div>"))
                        shotnum += 1

                    print(self._html.formatLine("</div>", -1, False))

                elif(testLine(self._regex('variables'), lineObj)):
                    print(self._html.formatLine("<div class=\"variables\">", 1))
                    print(self._html.formatLine("<hr />"))
                    self._variables.dumpVars(self._html.getIndent())
                    print(self._html.formatLine("</div>", -1, False))

                elif(testLine(self._regex('dumplinks'), lineObj)):
                    print(self._html.formatLine("<div class=\"links\">", 1))
                    print(self._html.formatLine("<hr />"))
                    self._links.dumpLinks(self._html.getIndent())
                    print(self._html.formatLine("</div>", -1, False))

                # links handles the various formats that allow a title to be specified.
                # [linkID]:url "title"
                # [linkID]:(url "title")
                # [linkID]:url
                # [linkID]:(url)
                # This has precedence over the [var]:[value], so we process it first
                elif(testLine(self._regex('links'), lineObj)):
                    m = matchLine(self._regex('links'), lineObj)

                    optTitle = '' if len(m.groups()) < 4 or not m.group(4) else m.group(4)

                    # TODO: Should we markdown the Link Text?? m.group(1)?
                    if(m is not None and len(m.groups()) == 4):
                        self._links.addLink(m.group(1), m.group(2), optTitle)
                        # print("RL:AL:{0}{1}{2}<br />".format(m.group(1),m.group(2),m.group(3)))
                    else:
                        print(self._ori_line)

                elif(testLine(self._regex('alias'), lineObj)):
                    m = matchLine(self._regex('alias'), lineObj)

                    # TODO: Should we markdown the Link Text?? m.group(1)?
                    if(m is not None and len(m.groups()) == 3):
                        self._variables.addVar(m.group(1), m.group(3))
                    else:
                        print(self._ori_line)

                elif(testLine(self._regex('anchor'), lineObj)):
                    # For this case, we just need to drop an anchor.
                    m = matchLine(self._regex('anchor'), lineObj)

                    if(m is not None and len(m.groups()) == 1):
                        print(self._html.formatLine("<a id=\"{0}\"></a>".format(m.group(1))))
                    else:
                        print(self._ori_line)

                # These "special" keywords require that we use the original
                # raw line and not the markdown line in order to parse. Once
                # we parse out these special lines, we'll markdown the individual
                # groups before writing them...
                elif(testLine(self._regex('cover'), lineObj)):
                    m = matchLine(self._regex('cover'), lineObj)

                    if(m is not None):
                        title = "" if len(m.groups()) < 1 or not m.group(1) else self._markdown(m.group(1))
                        author = "" if len(m.groups()) < 2 or not m.group(2) else self._markdown(m.group(2))
                        summary = "" if len(m.groups()) < 3 or not m.group(3) else self._markdown(m.group(3))

                        divstr = self._html.formatLine("<div id=\"cover\">\n", 1)
                        if title:
                            divstr += self._html.formatLine("<h3>%s</h3>\n" % title)
                        if author:
                            divstr += self._html.formatLine("<p>%s</p>\n" % author)
                        if summary:
                            divstr += self._html.formatLine("<p class=\"coverSummary\">%s</p>\n" % summary.rstrip())
                        divstr += self._html.formatLine("</div>", -1, False)

                        print(divstr)
                    else:
                        print(self._ori_line)

                elif(testLine(self._regex('revision'), lineObj)):
                    m = matchLine(self._regex('revision'), lineObj)

                    if(m is not None and len(m.groups()) == 1):
                        from time import strftime
                        revision = self._markdown(m.group(1))

                        divstr = self._html.formatLine("<div id=\"revision\">\n", 1)
                        divstr += self._html.formatLine("<p class=\"revTitle\">Revision: {0} ({1})</p>\n".format(revision.rstrip(), strftime("%Y%m%d @ %H:%M:%S")), -1)
                        divstr += self._html.formatLine("</div>")

                        print(divstr)
                    else:
                        print(self._ori_line)

                elif(testLine(self._regex('contact'), lineObj)):
                    m = matchLine(self._regex('contact'), lineObj)

                    if(m is not None):
                        cName = "" if len(m.groups()) < 1 or not m.group(1) else "{0}<br />".format(self._markdown(m.group(1)))
                        cPhone = "" if len(m.groups()) < 2 or not m.group(2) else "{0}<br />".format(self._markdown(m.group(2)))
                        cEmail = "" if len(m.groups()) < 3 or not m.group(3) else "{0}<br />".format(self._markdown(m.group(3)))
                        cLine1 = "" if len(m.groups()) < 4 or not m.group(4) else "{0}<br />".format(self._markdown(m.group(4)))
                        cLine2 = "" if len(m.groups()) < 5 or not m.group(5) else "{0}<br />".format(self._markdown(m.group(5)))
                        cLine3 = "" if len(m.groups()) < 6 or not m.group(6) else "{0}<br />".format(self._markdown(m.group(6)))

                        divstr = self._html.formatLine("<div id=\"contact\">\n", 1)
                        divstr += self._html.formatLine("<table>\n", 1)
                        divstr += self._html.formatLine("<tr>\n", 1)
                        divstr += self._html.formatLine("<td class=\"left\">{0}{1}{2}</td>\n".format(cLine1, cLine2, cLine3))
                        divstr += self._html.formatLine("<td class=\"right\">{0}{1}{2}</td>\n".format(cName, cPhone, cEmail), -1)
                        divstr += self._html.formatLine("</tr>\n", -1)
                        divstr += self._html.formatLine("</table>\n", -1)
                        divstr += self._html.formatLine("</div>")

                        print(divstr)
                    else:
                        print(self._ori_line)

                else:
                    if curLine.rstrip():
                        self._printInExtrasDiv("<p{1}>{0}</p>".format(curLine.rstrip(), cssClass))

            print(self._html.formatLine("</div>", -1, False))

        except RegexError as regex_error:
            print("{}".format(regex_error.errmsg))
            rc = 3

        return rc

    def load(self, avscript=None):
        """This method is used to open and initiate a parse on an AV format text file.
           If the scriptname is passed in, open it for reading, and invoke the parser.
           Otherwise, invoke the parser with the default input stream, which is stdin."""

        rc = 0

        # Ok, open the file and process each line we find in there.
        try:
            if(avscript is not None):
                # If the file doesn't exist, bail now.
                if not isfile(avscript):
                    return 1

            self._av.open(avscript)

            rc = self.parse()

        except IOError:
            rc = 2

        return rc

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
    args = parser.parse_args()
    
    return AVScriptParser().load(args.filename)
    

if __name__ == '__main__':
    exit(av_parse_file())
