'''
Check Balanced: Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree such that
the heights of the two subtrees of any node never differ by more than one.

'''




'''To find if a tree of size n nodes is balanced:

1- Solve the same problem for the right subtree

2- Solve the same problem for the left subtree

3- Get the heights of the left and right subtrees
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def balanced_tree_helper(node):

    if not node:
        return 0

    left_level = balanced_tree_helper(node.left)
    if left_level == -1:
        return left_level

    right_level = balanced_tree_helper(node.right)
    if right_level == -1:
        return right_level

    if ( abs(left_level - right_level) > 1) :
        return -1
    else:
        return max(left_level, right_level) + 1


def is_balanced(root):
    return balanced_tree_helper(root) > -1


# tree
root = Node(5)
root.left = Node(2)
root.right = Node(1)
root.left.left = Node(5)
root.left.right = Node(6)
root.left.left.left = Node(7)


print "Is the tree balanced ? \nAnswer is : ", is_balanced(root)


#Time complexity :
#T(n) = 2 * T(n / 2) + o(n) => O(n)