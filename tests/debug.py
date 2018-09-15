#!/usr/bin/env python

"""
from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'avscript')
path.insert(0, lib_path)
"""

import avscript

#from avscript_md import av_parse_file

#avscript.avscript_md.av_parse_file(['-f', 'test.md'])

avscript.avscript_md.av_parse_file(['-f', '/Users/ken/Dropbox/clp/projects/2018/buddyvargas/video/forgiveme/forgiveme-musicvideo.md'])
