__author__ = 'amit'

import csv
import re


def processFile(csvfile):

    f = open(csvfile)
    fieldnames = ['path', 'datetime_accessed', 'browser', 'status', 'size']
    fcsv = csv.DictReader(f, fieldnames)

    rows = list()
    for row in fcsv:
        #print row
        rows.append(row)
    return rows

def searchImages(csvdata):

    total = 0
    images = 0

    for row in csvdata:
        total += 1
        image_regex = "\.(jpg|JPG|jpeg|JPEG|png|PNG|gif|GIF)$"
        #print row['path']
        if re.search(image_regex, row['path']) is not None:
            images += 1

    pct_images = images * 1.0 / total
    print "Image requests account for %f of all requests" % pct_images
    return pct_images

def popularBrowser(csvdata):

    # list of browsers
    browsers = ['Firefox', 'Chrome', 'Safari', 'MSIE']
    # initialize counters
    browser_count = { x:0 for x in browsers}

    for row in csvdata:
        print row['browser']
        for bb in browsers:
            browser_regex = bb

            if re.search(browser_regex, row['browser']) is not None:
                browser_count[bb] += 1
    print browser_count



if __name__ == "__main__":
    csvdata = processFile('weblog.csv')
    pct_images = searchImages(csvdata)
    popularBrowser(csvdata)