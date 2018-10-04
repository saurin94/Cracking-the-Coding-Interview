'''
4.2 Minimal Tree:
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
'''


class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None



def sortedArrayToBst(arr):
    if not arr:
        return None
    mid = len(arr)/2

    root = Node(arr[mid])
    root.left = sortedArrayToBst(arr[:mid])
    root.right= sortedArrayToBst(arr[mid+1:])

    return root


def preOrderPrettyPrint(root):
    if not root:
        return None
    print(root.info)
    preOrderPrettyPrint(root.left)
    preOrderPrettyPrint(root.right)


root = sortedArrayToBst([1,2,3,4,5])
preOrderPrettyPrint(root)



