'''
Validate BST: Implement a function to check if a binary tree is a binary search tree.
'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# This function traverses down the tree keeping track of the narrowing min and max allowed values as it goes
# looking at each node only once.
# Initial values on max and min is infinity and then narrowing it down.
def isValidBST(root, minimum, maximum):
    if root is None:
        return True
    if root.data < minimum or root.data > maximum:
        return False
    return isValidBST(root.left, minimum, root.data-1) and isValidBST(root.right, root.data+1, maximum)


def validateBST(root):
    return isValidBST(root, -float('inf'), float('inf'))


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print "Is the given tree valid ? \nAnswer:", validateBST(root)



'''
Time Complexity: O(n)
Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
'''