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

    @staticmethod
    def str_to_html_entity_mix(string):
        """
        Encodes a string using decimal or hexadecimal HTML character entities

        Encodes each character of the given string as either a decimal
        or hexadecimal entity, in the hopes of foiling most email address
        harvesting bots.

        Note that running the same string through this function produces
        different results (intentionally). That's good, but it makes testing
        a little more challenging.

        Based on aea_encode_str() PHP function in Till Kruss's WordPress
        Plugin; URI: http://wordpress.org/plugins/email-address-encoder/
        Which is based on Michel Fortin's PHP Markdown:
        http://michelf.com/projects/php-markdown/
        Which is based on John Gruber's original Markdown:
        http://daringfireball.net/projects/markdown/
        Whose code is based on a filter by Matthew Wickline, posted to
        the BBEdit-Talk with some optimizations by Milian Wolff.
        """
        chars = list(string)        # convert string to a list

        from random import randint
        from binascii import crc32
        # generate a pseudo-random seed
        seed = randint(0, int(abs(crc32(str.encode(string)) / len(string))))

        # for each character in the string
        for key in range(len(chars)):
            char = chars[key]
            ordc = ord(char)

            # ascii only
            if ordc < 128:

                r = (seed * (1 + key)) % 100

                if(r > 75 and char not in ['@', '.', ':', ' ']):
                    # if r > 75 and char is not [@.: ], leave it intact
                    pass
                elif (r < 42):
                    # r < 42 encode the character in hex format
                    chars[key] = '&#{};'.format(hex(ordc)[1:])
                else:
                    # otherwise encode it as a decimal number
                    chars[key] = '&#{};'.format(ordc)

        return ''.join(chars)   # return the new encoded string
    @staticmethod
    def encodeURL(url):
        if url.startswith('mailto:'):
            return HtmlUtils.str_to_html_entity_mix(url.replace(" ", "%20"))
        else:
            return url.replace(" ", "%20")




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
