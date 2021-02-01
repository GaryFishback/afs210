# list1 = [[1,2,3], [4,5,6]]

# [i* j for i in list1[0] for j in list[1]]

# words = 'here is a sentence'.split()

# print([[word, len(word) + 5] for word in words])


# words = str.split('the longest word in this sentence')
# print(sorted(words,key=len,reverse=True))

# def recurTest(low,high):
#     if low <= high:
#         print(low)
#         recurTest(low+1,high)

# recurTest(1,200)

# class Employee(object): 
#         numEmployee = 0 
#         def __init__(self, name, rate): 
#             self.owed = 0         
#             self.name = name 
#             self.rate=rate 
#             Employee.numEmployee += 1 

#         def __del__(self): 
#             Employee.numEmployee -= 1 

#         def hours(self, numHours): 
#             self.owed += numHours * self.rate 
#             return("%.2f hours worked" % numHours) 

#         def pay(self):                 
#             self.owed = 0 
#             return("payed %s " % self.name) 
# emp1 = Employee("Jill", 18.50)
# emp2 = Employee("Jack", 15.50)
# emp1.hours(20)
# print(emp1.owed)

# class my_class(): 
#         def __init__(self, greet): 
#             self.greet = greet 
#         def __repr__(self): 
#             return 'a custom object (%r)' % (self.greet) 
# a=my_class('giday').self

# print(a)