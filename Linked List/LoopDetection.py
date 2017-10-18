import Traversal


class Node(Traversal.Node):
    def detect_loop(self):
        elements = set()
        node = self
        while node:
            if node.val in elements:
                return True
            else:
                elements.add(node.val)
                node = node.next
        return False


if __name__ == "__main__":
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print "Traversal :\n", head.traversal()

    print "\nLoop Detected: ", head.detect_loop()

    # head.traversal()
