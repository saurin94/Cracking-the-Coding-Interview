class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
		
	def __repr__(self):
		return str(self.val)
		
arr = [7,8,4,5,1,6,3,2]

head = Node(arr[0])
p = head
for i in arr[1:]:
	p.next = Node(i)
	p = p.next


def partition(head, val):
	small = []
	large = []
	while head:
		if head.val < val.val:
			small.append(head)
		else:
			large.append(head)
		head = head.next
	final = small + large
	new_head = Node(final[0])
	t = new_head
	for i in final[1:]:
		t.next = Node(i)
		t = t.next
	return new_head


def print_list(head):
	while head:
		print head.val
		head = head.next


		
val = Node(5)
print_list(head)
node = partition(head,val)
print("\n")
print_list(node)
