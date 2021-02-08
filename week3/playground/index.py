# class testItem():
#     def __init__(self, test):
#         self.test = test

#     def printTest(self):
#         return self.test
    
#     def add(self):
#         return int(self.test) + int(self.test)

# item = testItem()
# print(item)


class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval