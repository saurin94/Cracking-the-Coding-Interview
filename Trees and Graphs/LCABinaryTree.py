class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findLCA(root, n1, n2):
    # Base Case
    if root is None:
        return None
    else:
        # If either n1 or n2 matches with root's data, report
        #  the presence by returning root (Note that if a key is
        #  ancestor of other, then the ancestor key becomes LCA )
        if root.data == n1 or root.data == n2:
            return root


        # Look for keys in left and right subtrees
        left_lca = findLCA(root.left, n1, n2)
        right_lca = findLCA(root.right, n1, n2)

        # If both of the above calls return Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        if left_lca and right_lca:
            return root

            # Otherwise check if left subtree or right subtree is LCA
        return left_lca if left_lca is not None else right_lca

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print "LCA(5,3) = ", findLCA(root, 5, 3).data
print "LCA(3,4) = ", findLCA(root, 3, 4).data
print "LCA(8,6) = ", findLCA(root, 8, 6).data
print "LCA(1,9) = ", findLCA(root, 1, 9).data