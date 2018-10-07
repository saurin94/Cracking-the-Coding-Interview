'''
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree.
You may assume that each node has a link to its parent.
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative inOrder traversal and storing in in arr
def inOrderSuccessorArr(root):
    current = root
    s = []
    allNodes = []
    isStackFull = 0
    while not isStackFull:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if (len(s) > 0):
                current = s.pop()
                allNodes.append(current.data)
                current = current.right
            else:
                isStackFull = 1

    return allNodes

def findOrderSuccessorFromArr(arr, node):
    for i in range(0, len(arr)):
        if arr[i] == node:
            if(i+1<len(arr)):
                return arr[i+1]
            else:
                return None

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
searchInOrderSuccessorOf = 8
print(findOrderSuccessorFromArr(inOrderSuccessorArr(root), searchInOrderSuccessorOf))


'''
Time Complexity: O(n)
Space Complexity : O(n)
'''
