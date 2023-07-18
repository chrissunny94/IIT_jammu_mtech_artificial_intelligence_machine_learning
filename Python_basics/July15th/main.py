class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = Node(None)

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def delete_first_node(self):
        delNode = self.head.next
        self.head = None
        self.head = delNode

    def deletefirst(self):
        if self.head is None:
            return
        
        ref = self.head.next
        self.head = None
        self.head = ref

    def deleteLast(self):
        currentval = self.headval
        while currentval is not None:
            if self.headval.nextval.nextval is None:
                self.headval.nextval = None
            currentval = self.headval.nextval
            
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headval.nextval = e2
e2.nextval = e3

list.Inbetween(list.headval.nextval,"Fri")

#list.listprint()

#list.delete_first_node()

list.deleteLast()
list.listprint()


