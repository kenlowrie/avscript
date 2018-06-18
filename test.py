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

    def process(self, which):
        self.avscript_md.open_and_parse("tests/in/{}.md".format(which))
        with open('tests/out/{}.html'.format(which), 'r') as myfile:
            data = myfile.read()
        with open('tests/run/{}.out'.format(which), 'w') as mf2:
            mf2.write(self.capturedOutput.getvalue())

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


if __name__ == '__main__':
    suite3 = TestLoader().loadTestsFromTestCase(TestAVScriptClass)
    TextTestRunner(verbosity=2).run(suite3)
