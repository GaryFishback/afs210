

class Node:
    # Singly linked node
    def __init__(self, data):
        self.data = data
        self.next = None
# class SinglyLinkedList:
#         def __init__(self):
#              self.tail = None 
#         def append(self, data):
#              # Encapsulate the data in a Node
#              node = Node(data)

#              if self.tail == None:
#                  self.tail = node
#              else:
#                  current = self.tail
#                  while current.next:
#                      current = current.next
#                  current.next = node

# words = SinglyLinkedList()
# words.append('egg')
# words.append('ham')
# words.append('spam')

# current = words.tail
# while current:
#         print(current.data)

# class MyList:
#     def __init__(self):
#         self.tail = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#     def append_item(self, data):
#         node = Node(data)
#         if self.tail:
#             self.tail.next = node
#             self.tail = node
#         else:
#             self.head = node
#             self.tail = node

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next
#     def removeItem(self):
#         print('test')
# llist = LinkedList()

# llist.head = Node("PHP")
# second = Node("Python")
# third = Node("C#")
# fourth = Node("C++")
# fifth = Node("Java")

# llist.head.next = second

# second.next = third

# third.next = fourth

# fourth.next = fifth

# # llist.printList()
# print(llist.head)


class LinkedList:
    def __init__(self):
        # List starts empty, so this is required.
        # head tells it where to start.
        self.head = None
    
    def newItem(self, item):
        # Whatever is passed as an argument is represented by item, which is then assigned to package. The current package takes the empty head(None), and replaces it with the package. The next time newItem is called in this file execution, self.head is now equal to package.
 
        package = Node(item)
        package.next = self.head
        self.head = package


    def delItem(self, key):
        # This stores the last passed item.
        temp = self.head

        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                
                return print(f'{key} been removed from head')
        # if(temp == None):
        #     return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next

        temp = None
        print(f'{key} has been removed')



    def printItems(self):
        temp = self.head
        while(temp):
            print (" %s" %(temp.data)),
            temp = temp.next

llist = LinkedList()
llist.newItem("PHP")
llist.newItem("Python")
llist.newItem("C#")
llist.newItem("C++")
llist.newItem("Java")

llist.printItems()
print("break here")
llist.delItem("Java")
# # AttributeError: 'NoneType' object has no attribute 'next'
# # llist.delItem("Java3")
llist.printItems()