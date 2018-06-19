#!/usr/bin/env python3

import io
import sys
from unittest import TestCase, TestLoader, TextTestRunner

import avscript_md


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
        self.process('revision',False)
        g1 = r'<p class\=\"revTitle\">Revision:([^\(]*)([^<]*)</p>'
        g2 = r'\(([0-9]{8})\s@\s([0-9]{2}:[0-9]{2}:[0-9]{2})\)'
        from re import findall, match

        # Find all the <p class="revTitle">Revision: n (date @ time)</p> lines
        m = findall(g1,self.capturedOutput.getvalue())
        self.assertEqual(len(m),2)
        for rev_set in m:
            # extract the revision and timestamp from a match
            r,ts = rev_set
            # extract the date and time
            m2 = match(g2,ts)
            self.assertEqual(len(m2.groups()),2)    # should be a date and a time
            self.assertEqual(m2.group(0)[0:1],'(')  # should start with (
            self.assertEqual(m2.group(0)[-1],')')   # should end with )
            self.assertEqual(len(m2.group(1)),8)    # date length is 8
            self.assertEqual(len(m2.group(2)),8)    # time length is 8
    

if __name__ == '__main__':
    suite3 = TestLoader().loadTestsFromTestCase(TestAVScriptClass)
    TextTestRunner(verbosity=2).run(suite3)
