class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
	def __repr__(self):
		print str(self.val)

arr = [1, 2, 4, 2, 1]

head = Node(arr[0])
p = head
for i in arr[1:]:
	p.next = Node(i)
	p = p.next

	
def palindrome(head):
	s = ""
	while head:
		s += str(head.val)
		head = head.next
	return s == s[::-1]

def print_list(head):
	s = ""
	while head:
		s += str(head.val)
		head = head.next
		s += "->"
	print s[:-2]

print_list(head)
print palindrome(head)