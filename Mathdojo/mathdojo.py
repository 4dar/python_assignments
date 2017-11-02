class Mathdojo(object):
    def __init__(self, num):
        self.num = num

    def add(self, *num):
        self.num += sum(num)
        return self

    def subtract(self, *num):
        self.num -= sum(num)
        return self
    def result(self):
        print self.num
        return self
    
    

md = Mathdojo(0)

md.add(2).add(2,5).subtract(3,2).result()

class Mathdojo(object):
    def __init__(self, num):
        self.num = num

    def add(self, *num):
        self.num += sum(num)
        for i in num:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.num += k
            else:
                self.num += i
        return self

    def subtract(self, *num):
        self.num -= sum(num)
        return self
    def result(self):
        print self.num
        return self
    
    

md = Mathdojo(0)

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
