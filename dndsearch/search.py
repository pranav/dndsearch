#!/usr/bin/env python
    
import sys
import sql
from sql import Page


if __name__ == '__main__':
    searchterm = ' '.join(sys.argv[1:])
    print "Searching for %s" % searchterm

    book_pages = Page.search(searchterm)

    i = 0
    for v in book_pages:
        if i < 6:
            print ('%s: %s,' % (v[0], v[1]))
            i = i + 1
        else:
            break
