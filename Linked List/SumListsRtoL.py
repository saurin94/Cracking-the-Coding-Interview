import Traversal


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


head1 = Node(1)
p = head1
l = [4, 3]
for i in l:
    p.next = Node(i)
    p = p.next

head2 = Node(9)
p = head2
l = [5, 9]
for i in l:
    p.next = Node(i)
    p = p.next

head3 = Node(9)
p = head3
l = [9]
for i in l:
    p.next = Node(i)
    p = p.next


def sum_lists(head1, head2):
    head = Node(0)
    carry = 0
    pointer = head

    while head1 and head2:
        total = head1.val + head2.val + carry
        pointer.next = Node(total % 10)
        pointer = pointer.next
        carry = total / 10
        head1 = head1.next
        head2 = head2.next

    if head1 is None:
        while head2:
            total = head2.val + carry
            pointer.next = Node(total % 10)
            pointer = pointer.next
            carry = total / 10
            head2 = head2.next

    if head2 is None:
        while head1:
            total = head1.val + carry
            pointer.next = Node(total % 10)
            pointer = pointer.next
            carry = total / 10
            head1 = head1.next

    if carry > 0:
        pointer.next = Node(carry)
    return head.next


sum1 = sum_lists(head1, head2)
while sum1:
    print sum1.val
    sum1 = sum1.next
print "______"
sum2 = sum_lists(head1, head3)
while sum2:
    print sum2.val
    sum2 = sum2.next
