import Traversal


class Node(Traversal.Node):
    def remove_duplicates(self):
        node = self
        dups = set()
        prev = None
        while node:
            val = node.val
            if val in dups:
                prev.next = node.next
            else:
                dups.add(val)
            prev = node
            node = node.next


if __name__ == "__main__":
    head = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    node5 = Node(1)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print "Before removing duplicates :\n", head.traversal()
    head.remove_duplicates()
    print "\nAfter removing duplicates :\n", head.traversal()