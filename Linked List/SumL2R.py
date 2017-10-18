class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
		
	def __repr__(self):
		return str(self.val)

arr = [1, 1, 1]

head = Node(arr[0])
p = head
for i in arr[1:]:
	p.next = Node(i)
	p = p.next

arr2 = [2, 8, 9]
head2 = Node(arr2[0])
p = head2
for i in arr2[1:]:
	p.next = Node(i)
	p = p.next

def sum_R_L(head1,head2):
	num1 = get_num(head1)
	num2 = get_num(head2)
	total = str(num1 + num2)
	print "Total :", total
	total = total[::-1]
	head_final = Node(total[0])
	p = head_final
	for i in total[1:]:
		p.next = Node(i)
		p = p.next
	return head_final
	
def get_num(head):
	count = 0
	num = 0
	while head:
		#print head.val, 10**count
		num += 10**count*head.val
		head = head.next
		count += 1
	return num
	
def printList(head):
	while head:
		print head.val
		head = head.next

h = sum_R_L(head,head2)
printList(h)
		
