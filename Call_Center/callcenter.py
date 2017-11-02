class Call(object):
    
    def __init__(self, uid, name, pnumber, time, reason):
        self.id = uid
        self.name = name
        self.pnumber = pnumber
        self.time = time
        self.reason = reason

    def display(self):
        print self.id
        print self.name
        print self.pnumber
        print self.time

class CallCenter(object):
    
    def __init__(self, calls, queuesize):
        self.calls = calls
        self.queue = queuesize

    def add(self):

    def remove(self):

    def info(self):

    