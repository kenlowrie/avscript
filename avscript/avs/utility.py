#!/usr/bin/env python

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

if __name__ == '__main__':
    print("Library module. Not directly callable.")
