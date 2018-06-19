#!/usr/bin/env python3

import io
import sys
from unittest import TestCase, TestLoader, TextTestRunner

import avscript_md


def decode(html_string):
    try:
        from HTMLParser import HTMLParser
    except ImportError:
        from html.parser import HTMLParser

    h = HTMLParser()
    return h.unescape(html_string)


class TestAVScriptClass(TestCase):
    def setUp(self):
        self.avscript_md = avscript_md.AVScriptParser()
        self.capturedOutput = io.StringIO()     # Create StringIO object
        self.avscript_md.stdoutput = (self.capturedOutput, False)   # and redirect stdout.

    def tearDown(self):
        self.avscript_md.stdoutput = sys.__stdout__     # Reset redirect.
        del self.avscript_md
        self.avscript_md = None
        del self.capturedOutput

    def process(self, which, checkEqual=True):
        self.avscript_md.open_and_parse("tests/in/{}.md".format(which))
        with open('tests/run/{}.out'.format(which), 'w') as mf2:
            mf2.write(self.capturedOutput.getvalue())

        if(checkEqual):
            with open('tests/out/{}.html'.format(which), 'r') as myfile:
                data = myfile.read()
            self.assertEqual(self.capturedOutput.getvalue(), data)

    def test_markdown(self):
        self.process('markdown')

    def test_variables(self):
        self.process('variables')

    def test_divs(self):
        self.process('divs')

    def test_specials(self):
        self.process('specials')

    def test_import(self):
        self.process('import')

    def test_script1(self):
        self.process('script1')

    def test_transitions(self):
        self.process('transitions')

    def test_revision(self):
        """
        Validate Revision keyword output with date/time stamps

        We can't use the standard way of comparing the output to a known
        data set, since the date/time stamp changes on each execution.
        So, we gotta look at each one and make sure it's in the right format,
        and length, etc., etc.
        """
        self.process('revision', False)
        g1 = r'<p class\=\"revTitle\">Revision:([^\(]*)([^<]*)</p>'
        g2 = r'\(([0-9]{8})\s@\s([0-9]{2}:[0-9]{2}:[0-9]{2})\)'
        from re import findall, match
        from time import strftime
        ts_date = "{}".format(strftime("%Y%m%d"))
        ts_time = "{}".format(strftime("%H:%M:%S"))

        # Find all the <p class="revTitle">Revision: n (date @ time)</p> lines
        m = findall(g1, self.capturedOutput.getvalue())
        self.assertEqual(len(m), 3)
        for rev_set in m:
            # extract the revision and timestamp from a match
            r, ts = rev_set
            # extract the date and time
            m2 = match(g2, ts)
            self.assertEqual(len(m2.groups()), 2)    # should be a date and a time
            self.assertEqual(m2.group(0)[0:1], '(')  # should start with (
            self.assertEqual(m2.group(0)[-1], ')')   # should end with )
            self.assertEqual(len(m2.group(1)), 8)    # date length is 8
            self.assertEqual(m2.group(1),ts_date)
            self.assertEqual(len(m2.group(2)), 8)    # time length is 8
            self.assertEqual(m2.group(2)[0:3],ts_time[0:3])

    def test_mailto(self):
        """
        Validate a mailto: link

        We can't use the standard way of comparing the output to a known
        data set, since mailto: links are encoded as HTML entities to help
        foil spambots. As such, each time we render the HTML file, the output
        is different. So, we need to parse the output and find the encoded
        entities, decode them, and compare them to what they were originally.
        """
        self.process('mailto', False)
        g1 = r'<a href=\"(.*)\">([\w]*)</a>'
        from re import findall

        d = {
            "me": "mailto:myemail@mydomain.com",
            "you": "mailto:your.email_address@your-domain.com",
            "feedback": "mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"
        }

        # Find all the <a href="encoded_mailto_link">varname</a> lines
        m = findall(g1, self.capturedOutput.getvalue())
        self.assertEqual(len(m), 3)
        for mailto_set in m:
            # extract the mailto link and the variable name from a match
            mailto, var_name = mailto_set

            self.assertEqual(decode(mailto), d.get(var_name))


if __name__ == '__main__':
    suite3 = TestLoader().loadTestsFromTestCase(TestAVScriptClass)
    TextTestRunner(verbosity=2).run(suite3)
