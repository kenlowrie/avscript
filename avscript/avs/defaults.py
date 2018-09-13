#!/usr/bin/env python

import kenl380.pylib as pylib

def context():
    """returns the context object for this script."""

    try:
        myself = __file__
    except NameError:
        from sys import argv
        myself = argv[0]

    return pylib.context(myself)

me = context()

class Defaults(object):
    DEF_JSON_STORE = "defaults.json"

    def __init__(self, defaultsPath=None, defaultsName=None):
        from os.path import isfile, isdir, join

        dp =  defaultsPath if defaultsPath is not None and isdir(defaultsPath) else me.whereami()
        fn = defaultsName if defaultsName is not None and isfile(defaultsName) else Defaults.DEF_JSON_STORE
        self.defaults_basefilename = join(dp,fn)
        self.defaults = self._loadDefaults()

    def _loadJSON(self, base_filename):
        from json import load
        dict = {}
        try:
            with open(base_filename, 'r') as fp:
                dict = load(fp)
                fp.close()
        except IOError:
            dict = {}

        return dict

    def _saveJSON(self, base_filename, data):
        from json import dump
        try:
            with open(base_filename, 'w') as fp:
                dump(data, fp, indent=4)
                fp.close()
        except IOError:
            return -1
            
        return 0

    def _loadDefaults(self):
        return self._loadJSON(self.defaults_basefilename)

    def _saveDefaults(self):
        return self._saveJSON(self.defaults_basefilename, self.defaults)

    def getDefault(self, key):
        if key in self.defaults:
            return self.defaults[key]
        return None

    def setDefault(self, key, value):
        self.defaults[key] = value
        return self._saveDefaults()

    def removeDefault(self, key):
        if key in self.defaults:
            del self.defaults[key]
        return self._saveDefaults()

    def dumpDefaults(self):
        print("\nCurrent defaults set in {}\n".format(self.defaults_basefilename))
        for item in self.defaults:
            print("\t{}: {}".format(item, self.defaults[item]))

        print("")
        return 0



if __name__ == '__main__':
    print("Library module. Not directly callable.")
