import LinkedList


class Node(LinkedList.Node):
    def traversal(self):
        node = self
        while node:
            print node.val
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

    head.traversal()

