class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


def sortedBST(arr):
    if not arr:
        return None
    mid = (len(arr)) // 2

    root = Node(arr[mid])

    root.left = sortedBST(arr[:mid])

    root.right = sortedBST(arr[mid+1:])
    return root

def sorted(items):
    if not items:
        return
    print(items.data)
    sorted(items.left)
    sorted(items.right)

result = sortedBST([1,2,3,4,5,6,7])

sorted(result)