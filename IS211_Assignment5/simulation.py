__author__ = 'amit'


from Queue import Queue
import csv
import os


class Request(object):

    def __init__(self, request_time, request_url, request_len):
        # initialize a request
        self.time = request_time
        self.url = request_url
        self.len = request_len

    def waittime(self, currenttime):
        return currenttime - self.time


class Server(object):

    def __init__(self):
        # create a server to process requests
        self.current_request = None
        self.time_left = 0

    def new_request(self, R):
        # add new request to end of queue
        self.current_request = R
        self.time_left = R.len

    def tick(self):
        if self.current_request is not None:
            self.time_left += -1  # take one sec off current task
            if self.time_left <= 0:
                self.current_request = None # done w/ current task

    def bisy(self):
        if self.current_request != None:
            return True # current task done
        else:
            return False  # current task still running



def simulateOneServer(requests,max_time=100):
    # requests is queue of request objects

    # initialize server and server queue
    server_queue = Queue()
    server = Server()

    # loop over all time
    waitingtimes = list()
    new_request = requests.get(False)
    for t in range(max_time):
        #print t, server.bisy(), server.time_left
        # check to see if new request should get added to Queue

        if new_request is not None:
            while new_request.time == t:
                server_queue.put(new_request)
                #print t, "putting something on the grill"
                try:
                    new_request = requests.get(False) # get the next one
                except:
                    new_request = None
                    break

        # check to see what is coming on/off queue
        if (not server.bisy()) & (not server_queue.empty()):
            #print t, "taking something off the grill"
            next_request = server_queue.get()
            waitingtimes.append(next_request.waittime(t))
            server.new_request(next_request)

        server.tick()

    #print waitingtimes
    averageWait = sum(waitingtimes)*1.0/len(waitingtimes)
    print averageWait, server_queue.qsize()


def main():


    f = open('requests.csv')
    reader = csv.reader(f)
    request_queue = Queue()

    # read all requests from data file into list of requests
    allR = list()
    for r in reader:
        #print r
        request_time = int(r[0])
        request_url = r[1]
        request_len = int(r[2])

        R = Request(request_time, request_url, request_len)
        request_queue.put(R)
    max_time = R.time + 1
    print max_time

    print "num requests", request_queue.qsize()

    simulateOneServer(request_queue, max_time)


if __name__ == '__main__':
    main()

