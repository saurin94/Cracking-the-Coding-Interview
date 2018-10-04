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