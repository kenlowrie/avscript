#!/usr/bin/env python

from __future__ import print_function


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


class _Link(object):
    """Class to abstract a reference link. Keep track of the URL (url) and
    the optional title (title). We don't track the name here, that is done
    in the C_Links class."""
    def __init__(self, url, title=None):
        if(url[0:7] == 'mailto:'):
            self.url = str_to_html_entity_mix(url.replace(" ", "%20"))
        else:
            self.url = url.replace(" ", "%20")
        self.title = title


class LinkDict(object):
    """Class to abstract a dictionary of reference links"""
    def __init__(self):
        self.links = {}

    def addLink(self, id, url, title=None):
        """Add a link called 'id' to the list and set its url to 'url'
        and its title to 'title'."""
        # print("addLink()-->{0}-{1}-{2}<br />".format(id,url,title))
        self.links[id] = _Link(url, title)

    def exists(self, id):
        """Returns true if the link named 'id' exists."""
        return id in self.links

    def getLinkUrl(self, id):
        """Gets the link object named 'id', unless it doesn't exist, in
        which case it returns 'id'."""
        if(self.exists(id)):
            return self.links[id].url

        # This seems best to just return what we were given. If it doesn't
        # expand, it should be obvious, right?
        return id

    def getLinkMarkup(self, id, altText=None):
        """Returns the HTML markup for the link named 'id' if it exists.
        Otherwise, return an empty string. If altText is passed, wrap that with
        the link markup, otherwise, just wrap the 'id'."""
        title = "" if not self.exists(id) or not self.links[id].title else " title=\"{0}\"".format(self.links[id].title)
        linkText = "{0}".format(altText if altText else id)

        return '<a href=\"{0}\"{2}>{1}</a>'.format(self.getLinkUrl(id), linkText, title)

    def dumpLinks(self, indent='', output=print):
        """Dumps the links list, names, urls and titles."""
        for link in sorted(self.links):
            output("{3}<strong>{0}:</strong>{1}<em>:{2}</em><br />".format(link, self.links[link].url, self.links[link].title, indent))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
