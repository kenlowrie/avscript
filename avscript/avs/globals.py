#!/usr/bin/env python

from os.path import join, abspath, dirname, realpath

def _getBasepath():
    return abspath(dirname(dirname(realpath(__file__))))

def init_globals():
    return [
        '@var _id="sys" basepath="{}" imports="{}"'.format(_getBasepath(), join(_getBasepath(),'import')),
    ]

if __name__ == '__main__':
    print("Library module. Not directly callable.")
