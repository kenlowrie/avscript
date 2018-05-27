#!/usr/bin/env python

class BookmarkList(object):
    def __init__(self):
        self.bookmarks = []
        self.linkIDnum = 0

    def addBookmarkUsingID(self, id, link):
        curItem = len(self.bookmarks)
        self.bookmarks.append((id, link))
        self.linkIDnum += 1
        return self.bookmarks[curItem][0]

    def addBookmark(self, link):
        return self.addBookmarkUsingID("fnref:{0}".format(self.linkIDnum), link)
        #
        curItem = len(self.bookmarks)
        self.bookmarks.append(("fnref:{0}".format(self.linkIDnum), link))
        self.linkIDnum += 1
        return self.bookmarks[curItem][0]

    def getBookmarkList(self):
        return self.bookmarks

    def dumpBookmarks(self):
        for bookmark in self.bookmarks:
            print("{0}-{1}".format(bookmark, self.bookmarks[bookmark][1]))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
