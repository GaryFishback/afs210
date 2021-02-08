import heapq

listItems = [25, 35, 22, 85, 14, 65, 75, 22, 58]

sortedList = heapq.nlargest(3, listItems)
print(sortedList)