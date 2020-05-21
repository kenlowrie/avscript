#!/usr/bin/env python

"""
from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'avscript')
path.insert(0, lib_path)
"""

import avscript.avs.defaults as defaults

#from avscript_md import av_parse_file

mydefs = defaults.Defaults()
mydefs.setDefault('import2', 'some cool value for import 2')
mydefs.dumpDefaults()
print( mydefs.getDefault('import2'))
mydefs.getDefault('import2')
mydefs.removeDefault('import2')
mydefs.setDefault('imports', '/Users/ken/Dropbox/filestor/docs/script_templates')
mydefs.dumpDefaults()
