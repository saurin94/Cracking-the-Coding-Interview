import Traversal


class Node(Traversal.Node):
    def kth_to_last_element(self, k):
        if k < 0:
            return None
        p1 = self
        p2 = self
        i = 0
        while p1:
            p1 = p1.next
            if i < k:
                i += 1
            else:
                p2 = p2.next
        if i == k:
            return p2.val
        else:
            return None


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
    print "\n2nd Last element :", head.kth_to_last_element(2)
    print "3rd Last element :", head.kth_to_last_element(3)

    # head.traversal()
