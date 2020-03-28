#!/usr/bin/env python3

"""
This module creates an HTML document suitable for printing.

It uses avscript_md.py, which reads an AV script written in a specialized
Markdown-syntax, and outputs HTML format. Since avscript_md is designed to
be used by intermediate processors, it doesn't output the HTML header and
footer tags; instead, it just writes everything between the <body></body>
tags. mkavscript_md fills the gap by creating a properly formatted HTML
document ready to be loaded into a browser (usually so you can save it as
a PDF or <gasp> print it).

usage:

    mkavscript_md -h

    mkavscript_md.py uses argparse, so just run it with -h for the syntax.
"""

from os import system, mkdir
from os.path import split, splitext, join, isdir, isfile

from sys import argv, exit

import kenl380.pylib as pylib


def context():
    """returns the context object for this script."""

    try:
        myself = __file__
    except NameError:
        myself = argv[0]

    return pylib.context(myself)


me = context()


class FileName(object):
    def __init__(self, mdfile, htmldir):
        path, name = split(mdfile)
        file, ext = splitext(name)

        self._pathname = path
        self._filename = name
        self._rootname = file
        self._file_ext = ext

        self._htmlfile = join(path, htmldir, file + ".html")

    @property
    def path(self):
        return self._pathname

    @property
    def filename(self):
        return self._filename

    @property
    def rootname(self):
        return self._rootname

    @property
    def extension(self):
        return self._file_ext

    @property
    def HTML_filename(self):
        return self._htmlfile


def get_head(mdfile, cssFile):
    path, name = split(mdfile)
    file, ext = splitext(name)

    head = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>"""
    head += file
    head += """</title>
    <meta charset="UTF-8">
    <link rel='stylesheet' href='{0}' />
</head>
<body>
""".format(cssFile)

    return head


def get_tail():
    return """
</body>
</html>
"""


def message(msgstr):
    print('{0}: {1}'.format(me.alias(), msgstr))


def add_header(htmlfile, fileobj, cssFile):
    htmlfile.write(get_head(fileobj.rootname, cssFile))


def add_footer(htmlfile):
    htmlfile.write(get_tail())


"""
TODO:
Need to make it so if you specify a path on cssfile, we strip it off since
it will be copied to the destination folder. We only need the path when
doing the transfer.

outpath should also be handled better so that we can use relative or absolute
and it will do the right thing with either.

"""


def _mkhtml(mdfile, cssfile, outpath, open_output_file):
    """
    Process 'mdfile'

    Arguments:
        mdfile -- the markdown file to process
        cssfile -- the CSS file to use for styling. Default is avscript_md.css
        outpath -- the location for the HTML output. Relative to mdfile path.
        open_output_file -- Whether to open the created HTML file
    """
    fileobj = FileName(mdfile, outpath)

    cssSrcPath, basename = split(cssfile)
    if(not cssSrcPath):
        # no path specified on the cssfile; assume it's where the Python script is
        cssSrcPath = join(me.whereami(), cssfile)
    else:
        cssSrcPath = cssfile

    if not isfile(cssSrcPath):
        print("Can't find [{}] or [{}]. Giving up.".format(cssfile, cssSrcPath))
        return 1

    if not isdir(outpath):
        mkdir(outpath)
    from shutil import copy2
    try:
        copy2(cssSrcPath, outpath)
    except OSError as why:
        print("Error copying CSS file: [{}]".format(str(why)))

    htmlfile = open(fileobj.HTML_filename, "w")

    from avscript.avscript_md import AVScriptParser

    message("Creating: " + fileobj.rootname)
    add_header(htmlfile, fileobj, cssfile)

    avscript_obj = AVScriptParser()
    avscript_obj.stdoutput = htmlfile
    avscript_obj.open_and_parse(mdfile)
    # avscript_obj.stdinput = open(mdfile,'r')
    # avscript_obj.parse()

    add_footer(htmlfile)
    htmlfile.close()
    if(open_output_file):
        system("open \"{0}\"".format(fileobj.HTML_filename))

    return 0


def mkavscript_md(arguments=None):
    """Make an Audio-Visual Script from a text file written in a Markdown-like syntax.

    Creates an HTML output file from the input file.

    if arguments is None, uses sys.argv - via argparse
    if no filename is specified, parses sys.stdin -- TODO: IS THIS TRUE?

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Create an HTML file in Audio-Visual script format from a text file.',
                            epilog='If filename is not specified, program reads from stdin.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='?', const='avscript_md.css', default='avscript_md.css', help='the CSS file you want used for the styling. Default is avscript_md.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to')
    parser.add_argument('-o', '--open', nargs='?', const=True, default=False, help='whether or not to open the resulting HTML output file with the default system app')

    args = parser.parse_args(None if arguments is None else arguments)

    return _mkhtml(args.filename, args.cssfile, args.path, args.open)


if __name__ == '__main__':
    exit(mkavscript_md())
