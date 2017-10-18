class Node:
	def __init__(self,val,next):
		self.val = val
		self.next = next

node4 = Node(4, None)
node3 = Node(3, node4)
node2 = Node(2, node3)		
head = Node(1, node2)

def reverse(head):
	new_head = None  # this is where we build the reversed list (reusing the existing nodes)
	while head is not None:
		temp = head  # temp is a reference to a node we're moving from one list to the other
		head = temp.next  # the first two assignments pop the node off the front of the list
		temp.next = new_head  # the next two make it the new head of the reversed list
		new_head = temp
	return new_head

def print_list(head):
	while head:
		print head.val
		head = head.next

print("Before Reversal : ")
print_list(head)
print("\n")
h = reverse(head)
print("\nAfter Reversal : ")
print_list(h)

		
	