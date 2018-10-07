class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def printAllPaths(self, root, total):
        paths = []
        self.printTotalPathUtil(root, paths, total)

    def printTotalPathUtil(self, root, paths, total):

        if root is not None:
            paths.append(root)

        if root.left:
            self.printTotalPathUtil(root.left, paths, total)
        if root.right:
            self.printTotalPathUtil(root.right, paths, total)

        subTotal = 0
        for i in range(len(paths)-1, -1, -1):
            subTotal += paths[i].data
            if subTotal == total:
                print self.sumPaths(paths, i)

        paths.pop()

    def sumPaths(self, paths, k):
        s = ""
        for i in range(k, len(paths)):
            s += str(paths[i].data) + " "
        print s


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(-4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)

Solution().printAllPaths(root, 9)
