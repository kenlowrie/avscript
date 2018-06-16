#!/usr/bin/env python3


from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch, mock_open

import avscript_md

class TestAVScriptClass(TestCase):
    def setUp(self):
        self.avscript_md = avscript_md.AVScriptParser()
        self.capturedOutput = io.StringIO()               # Create StringIO object
        self.avscript_md.stdoutput = (self.capturedOutput, False)                   #  and redirect stdout.

    def tearDown(self):
        self.avscript_md.stdoutput = sys.__stdout__         # Reset redirect.
        print ('Captured\n{}'.format(self.capturedOutput.getvalue()))  # Now works as before.
        del self.avscript_md
        self.avscript_md = None

    def test_markdown(self):
        self.avscript_md.open_and_parse("tests/inputs/markdown.md")
        # Now assert that the string output matches the tests/outputs/markdown.md
        pass


class TestStringMethods(TestCase):
    def setUp(self):
        self.avscript_md = avscript_md.AVScriptParser()

    def tearDown(self):
        del self.avscript_md
        self.avscript_md = None

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

from textwrap import dedent
import io
import sys

class OpenTest(TestCase):
    #DATA = dedent("""
    #    a,b,c
    #    x,y,z
    #    """).strip()
    DATA = """a,b,c
x,y,z
"""

    def setUp(self):
        self.avscript_md = avscript_md.AVScriptParser()
        self.capturedOutput = io.StringIO()               # Create StringIO object
        self.avscript_md.stdoutput = (self.capturedOutput, False)                   #  and redirect stdout.

    def tearDown(self):
        self.avscript_md.stdoutput = sys.__stdout__                     # Reset redirect.
        print ("Captured\n", self.capturedOutput.getvalue())   # Now works as before.
        del self.avscript_md
        self.avscript_md = None

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_open(self):

        # Due to how the patching is done, any module accessing `open' for the 
        # duration of this test get access to a mock instead (not just the test 
        # module).
        #with open("filename", "r") as f:
        #    result = f.readline()
        #    result2 = f.readline()

        #self.assertEqual('a,b,c\n', result)
        #self.assertEqual('x,y,z\n', result2)
        #self.assertEqual("a,b,c\nx,y,z", result)
        self.avscript_md.stdinput = (open("filename","r"),False)
        open.assert_called_once_with("filename", "r")
        self.avscript_md.parse()


if __name__ == '__main__':
    #unittest.main()
    suite = TestLoader().loadTestsFromTestCase(TestStringMethods)
    TextTestRunner(verbosity=2).run(suite)
    suite2 = TestLoader().loadTestsFromTestCase(OpenTest)
    TextTestRunner(verbosity=2).run(suite2)
    suite3 = TestLoader().loadTestsFromTestCase(TestAVScriptClass)
    TextTestRunner(verbosity=2).run(suite3)
