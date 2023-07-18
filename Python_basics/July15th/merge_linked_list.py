class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	def insert(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode

def mergeSortedLists(head1, head2):
  
    temp = None
  
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
  
    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeSortedLists(head1.next, head2)
          
    else:
        temp = head2
        temp.next = mergeSortedLists(head1, head2.next)
  
    # return the temp list.
    return temp

def mergeSortedList(node1 , node2):
	final_list = None
	if (node1 is None):
		return node1
	if(node2 is None):
		return node2
	if node1.data <= node2.data:
	    final_list = node1
	    final_list.next = mergeSortedList(node1.next, node2)
	else:
	    final_list = node2
	    final_list.next = mergeSortedList(node1, node2.next)
	return final_list

def point_of_intersection(node1 , node2):
	# node1 = LinkedList()
	# node2 = LinkedList()
    if  (node1.next is  node2.next):
        print(node1.head.data)
	    print(node2.head.data)
        print('\n')
        node1 = node1.head.next 
        node2 = node2.head.next
	
def find_common_values(head1, head2):
    common_values = []

    # Traverse the first linked list
    current1 = head1
    while current1:
        # Compare with every node in the second linked list
        current2 = head2
        while current2:
            # If values match, add to common values list
            if current1.val == current2.val:
                common_values.append(current1.val)
                break  # Move to next node in the first linked list
            current2 = current2.next
        current1 = current1.next

    return common_values

    def find_common_values(ll1, ll2):
        common_values = []
        current1 = head1
        while current1:
            current2 = head2
            while current2:
                if current1.val == current2.val:
                    common_values.append(current1.val)
                    break 
                current2 = current2.next
            current1 = current1.next
        return common_values
	
	


# Create 2 lists
head1 = LinkedList()
head2 = LinkedList()

head1.insert(1)
head1.insert(2)
head1.insert(4)
head1.insert(6)
head1.insert(9)

head1.printList()
print('\n')

head2.insert(3)
head2.insert(4)
head2.insert(7)
head2.insert(8)
head2.printList()
print('\n')


head1.head = mergeSortedLists(head1.head, head2.head)

head1.printList()

#final_list = LinkedList()
#final_list.head = mergeSortedList(head1.head, head2.head)

#final_list.printList()

print(point_of_intersection(head1.head , head2.head))


