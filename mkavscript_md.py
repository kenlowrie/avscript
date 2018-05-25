#!/usr/bin/env python

"""
This module creates an HTML document suitable for printing of an
AV script written in a specialized markdown that is processed by
avscript_md.py.

usage: 

    mkavscript_md avmarkdownfile
    
where:

    avmarkdownfile - an av script written in avscript_md format
              
example:

    mkavscript_md myavmdfile
"""

import os
import sys
import pylib

def context(varfile=None):
    """returns the context object for this script."""

    try:
        myself = __file__
    except NameError:
        myself = sys.argv[0]

    return pylib.context(myself,varfile)

me = context('mkavscript_md')

class C_FileName:
    def __init__(self,mdfile):
        path,name = os.path.split(mdfile)
        file,ext = os.path.splitext(name)
        
        self.pathname = path
        self.filename = name
        self.rootname = file
        self.file_ext = ext
        
        self.htmlfile = os.path.join(path,"html",file + ".html")
        
    def getPath(self):
        return self.pathname
        
    def getFile(self):
        return self.filename
        
    def getRootName(self):
        return self.rootname
        
    def getExt(self):
        return self.file_ext
        
    def getHTMLFile(self):
        return self.htmlfile
        


def gethead(mdfile,cssFile):
    path,name = os.path.split(mdfile)
    file,ext = os.path.splitext(name)
    
    head = """<!DOCTYPE html>
<html>
<head>
    <title>"""
    head += file
    head += """</title>
    <link rel='stylesheet' href='{0}' />
</head>
<body>
""".format(cssFile)

    return head
    
def gettail():
    return """
</body>
</html>"""

def message(msgstr): print('{0}: {1}'.format(me.alias(),msgstr))

def parse_args(args):

    mdfile = ''    # file name to parse
    
    for arg in args:
        if arg.lower() in ['--help', '-?', '-h', '/h', '/?']: usage()   # be nice, support command line help options
        
        mdfile = arg
            
    if not mdfile:   usage()
    
    return mdfile

def addheader(fileobj,cssFile):
    htmlfile = open(fileobj.getHTMLFile(), "w")
    htmlfile.write(gethead(fileobj.getRootName(),cssFile))
    htmlfile.close()

def addfooter(fileobj):
    htmlfile = open(fileobj.getHTMLFile(), "a")
    htmlfile.write(gettail())
    htmlfile.close()


def mkhtml(mdfile):
    fileobj = C_FileName(mdfile)
    cssFile = 'avscript_md.css'
    cssSrcPath = os.path.join(me.whereami(),"avscript_md.css")
    avscript_md = os.path.join(me.whereami(),"avscript_md.py")
    if not os.path.isdir('./html'):
        os.mkdir('./html')
    os.system("cp \"{0}\" ./html/{1}".format(cssSrcPath,cssFile))
    command = "{0} < \"{1}\" >> \"{2}\"".format(avscript_md,mdfile,fileobj.getHTMLFile())
    message("Creating: " + fileobj.getRootName())
    addheader(fileobj,cssFile)
    os.system(command)
    addfooter(fileobj)
    os.system("open \"{0}\"".format(fileobj.getHTMLFile()))

    return 0



def usage():
    print __doc__   # just print out the modules' docstring
    sys.exit(1)     # bail with non-zero exit code
    
if __name__ == '__main__':
    # assume we have no arguments, but if we do, pass them along
    args = []
    if len(sys.argv) < 2: usage()
    
    args = sys.argv[1:]

    mdfile = parse_args(args)
    
    sys.exit(mkhtml(mdfile))
    
