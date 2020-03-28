#!/usr/bin/env python

from .debug import Debug
from .utility import HtmlUtils


class BookmarkList(object):
    """This class keeps track of bookmarks in the document being processed by AVScript.

    Bookmarks are automatically created for each new shot added in a document.
    If the ///Shotlist/// keyword is later used, then the bookmark list in this
    object is used to create a list of the shots with a link back to the location
    in the document where it was defined.
    """
    def __init__(self):
        self.bookmarks = []
        self.linkIDnum = 0
        self.debug = Debug('bookmarks')

    def addBookmarkUsingID(self, id, text):
        """Add a bookmark to the list of bookmarks.

        Arguments:
            id - the id of the bookmark.
            text - the text to associate with this bookmark.

        Returns:
            id
        """
        curItem = len(self.bookmarks)
        self.bookmarks.append((id, text))
        self.linkIDnum += 1
        self.debug.print('addBookmarkUsingID(<strong>id=<em>"{}"</em>, text=<em>"{}"</em></strong>)'.format(id, HtmlUtils.escape_html(text)))
        return self.bookmarks[curItem][0]

    def addBookmark(self, text):
        """Add a bookmark to the list of bookmarks.

        Generates a unique ID and then adds a bookmark to the list with
        that ID.

        Arguments:
            text can be associated with the ID if needed.

        Returns:
            The generated ID for the added bookmark.
        """
        return self.addBookmarkUsingID("fnref:{0}".format(self.linkIDnum), text)

    def getBookmarkList(self):
        """Return the list of bookmarks currently defined."""
        return self.bookmarks

    def dumpBookmarks(self):
        """Dump the list of bookmarks currently defined.

        This is a debug feature which isn't currently used.
        """
        for bookmark in self.bookmarks:
            print("{0}-{1}".format(bookmark, self.bookmarks[bookmark][1]))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
