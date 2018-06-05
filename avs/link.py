#!/usr/bin/env python


class _Link(object):
    """Class to abstract a reference link. Keep track of the URL (url) and
    the optional title (title). We don't track the name here, that is done
    in the C_Links class."""
    def __init__(self, url, title=None):
        self.url = url.replace(" ","%20")
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

    def dumpLinks(self, indent=''):
        """Dumps the links list, names, urls and titles."""
        for link in self.links:
            print("{3}<strong>{0}:</strong>{1}<em>:{2}</em><br />".format(link, self.links[link].url, self.links[link].title, indent))

if __name__ == '__main__':
    print("Library module. Not directly callable.")
