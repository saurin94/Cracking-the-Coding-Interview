###  O(n) ###
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


head = Node(1)
p = head
l = [9, 5, 3, 6, 5, 4, 7, 5, 8, 2]
for i in l:
    p.next = Node(i)
    p = p.next

x = 5


def sort(head, x):
    p = head
    if not head:
        return None

    while p.next:
        if p.next.val < x:
            temp_head = head
            cur = p.next
            temp_next = cur.next
            head = cur
            cur.next = temp_head
            p.next = temp_next
        else:
            p = p.next
    return head


head = sort(head, x)
while head:
    print head.val,
    head = head.next
