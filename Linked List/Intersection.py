class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
	def __repr__(self):
		print str(self.val)
		
arr = [1, 2, 4]

head1 = Node(arr[0])
p = head1
for i in arr[1:]:
	p.next = Node(i)
	p = p.next

arr2 = [3, 4]
head2 = Node(arr2[0])
p = head2
for i in arr2[1:]:
	p.next = Node(i)
	p = p.next

	
def goAhead(head, n):
	for i in range(n):
		head = head.next
	return head

def intersection(head1, head2):
	h1 = 1
	h2 = 1
	n1 = head1
	n2 = head2
	while n1.next:
		h1 += 1
		n1 = n1.next
	while n2.next:
		h2 += 1
		n2 = n2.next
	
	if h1 > h2:
		head1 = goAhead(head1,h1-h2)
	elif h2 > h1:
		head2 = goAhead(head2,h2-h1)
	
	while head1 != head2:
		if head1.val == head2.val:
			return head1.val
		head1 = head1.next
		head2 = head2.next
	return None

print intersection(head1, head2)
