import Traversal


class Node(Traversal.Node):
    def delete_given_node(self, elem):
        node = self
        if elem.val == node.val:
            node.val = node.next.val
            node.next = node.next.next
        else:
            prev = None
            while node:
                if node.val == elem.val:
                    prev.next = node.next
                prev = node
                node = node.next

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
    val = Node(5)
    print "Traversal :\n", head.traversal()
    print "\nRemove element :", val.val
    head.delete_given_node(val)
    print "Traversal after Deletion :\n", head.traversal()

