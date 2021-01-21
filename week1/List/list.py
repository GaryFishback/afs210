# import bisect
# originalList =  [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

# sortedList = originalList.sort()

# # print(sortedList)
# li = [1, 3, 4, 4, 4, 6, 7] 
# print(bisect.insort(li,5))
# print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
# print (bisect.bisect(li, 4)) 

# # initializing list 
# li1 = [1, 3, 4, 4, 4, 6, 7] 
  
# # initializing list 
# li2 = [1, 3, 4, 4, 4, 6, 7] 
  
# # initializing list 
# li3 = [1, 3, 4, 4, 4, 6, 7] 
  
# # using insort() to insert 5 at appropriate position 
# # inserts at 6th position 
# bisect.insort(li1, ()) 

# print ("The list after inserting new element using insort() is : ") 
# for i in range(0, 7): 
#     print(li1[i], end=" ") 
  

#   Original List: [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

li = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]

# def sortMe():
#     newLi = []
#     for x in li:
#         if x < max(li):
#             if len(newLi) == 0:
                
#             # if x < max(newLi):
#             #     newLi.append(x)
#             #     print(newLi)
# sortMe()
newLi = []
while len(li) > 0:
    item = min(li)
    newLi.append(item)
    li.remove(item)
    print(newLi)
