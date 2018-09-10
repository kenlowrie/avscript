#!/usr/bin/env python

# This global is used to hold the interface to Namespaces.
_ns_xface = None

# Called during avscript initialization to save the interface to Namespaces
def _set_ns_xface(ns_ptr):
    global _ns_xface
    _ns_xface = ns_ptr


class HtmlUtils():

    @staticmethod
    def escape_html(s):
        if type(s) != type(''):
            # If we weren't passed a string, convert it to a string before we escape it.
            s = str(s)

        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class CodeHelpers():

    @staticmethod
    def b(i):
        return '{{' if i == 0 else '}}'

    @staticmethod
    def split_as(s):
        from .regex import Regex
        r = Regex(r'\s?([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')

        d = {l[0]: l[1] for l in r.regex.findall(s)}
        news = ''
        for i in d:
            news += '***{}***={}<br />'.format(i, HtmlUtils().escape_html(d[i]))

        return news

    @staticmethod
    def get_ns_var(v=None):
        global _ns_xface
        if not _ns_xface:
            print("interface not initialized")
            return

        if not v:
            print("missing variable name")
        elif _ns_xface.exists(v):
            print(_ns_xface.getValue(v))
        else:
            print("{} is undefined.".format(v))


    @staticmethod
    def default(v=None, default_value=""):
        if not v:
            print("existing variable name is required")
            return

        print("{}".format(default_value if not _ns_xface.exists(v) else _ns_xface.getValue(v)))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
