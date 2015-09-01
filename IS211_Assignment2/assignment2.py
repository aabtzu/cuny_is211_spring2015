__author__ = 'amit'


import urllib2
import datetime
import logging
import argparse


LOG_FILENAME = "error.log"

logging.basicConfig(filename=LOG_FILENAME,
                    filemode='w')
logger = logging.getLogger('assignment2')


def downloadData(url):
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)

    datafile = "birthday_data.csv"
    fout = open( datafile, "wb")

    fout.write(f.read())
    fout.close()

    return datafile

def parseDate(d):

    dd = datetime.datetime.strptime(d,"%d/%m/%Y")
    return dd.date()


def processData(datafile):

    # open the data file for reading
    f = open(datafile)

    # remove the header and initialize
    bday_dict = dict()
    line = 1
    header = f.next()

    # loop over all remaining rows
    for row in f:
        line += 1
        #print row.strip()
        fields = row.strip().split(',') # split into fields for CSV file

        id = int(fields[0])  # save id as int
        name = fields[1]
        try:
            bday = parseDate(fields[2]) # parse the date
        except:
            err_msg = "Error processing line #%d for ID #%d" % (line, id)
            #print err_msg
            #print fields
            #logger = logging.getLogger(logname)
            logger.error(err_msg)

        value = (name, bday)
        bday_dict[id] = value



    return bday_dict

def displayPerson(id, personData):

    try:
        person = personData[id]
        name = person[0]
        bday = person[1]
        print "Person #%d is %s with a birthday of %s" % (id, name, bday)

    except:
        print "No user found with that id"


def testMain():

    logger.debug("starting .. ")
    url = "https://s3.amazonaws.com/cuny-is211-spring2015/bdays.csv"
    #fname = downloadData(url)
    #print fname

    ftest = "birthdays100.csv"
    personData = processData(ftest)
    #print bdays
    #

    displayPerson(2, personData)
    displayPerson(20000, personData)



if __name__ == "__main__":
    logging.debug("this is foo")
    testMain()
