'''
4.10 Check Subtree: T l and T2 are two very large binary trees,
with T l much bigger than T2. Create an algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree ofT i if there exists a node n in T
i such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
'''


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def checkBothTrees(t1, t2):
    if t1 and t2 and t1.data == t2.data:
        if checkBothTrees(t1.left, t2.left) and checkBothTrees(t1.right, t2.right):
            return True

    if t1 is None and t2 is None:
        return True


def isSubTree(s, t):
    stack = [s]
    while stack:
        node = stack.pop()
        # check root of big tree matches with other root, if yes, check both trees
        if node.data == t.data and checkBothTrees(node, t):
            return True
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False


root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)

print "are the two trees subtrees of each other ? \nAnswer: ", isSubTree(root1, root2)
