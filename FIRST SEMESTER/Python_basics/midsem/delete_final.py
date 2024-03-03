# Python3 program to implement optimized delete in BST.

import collections
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)
 
def insert(node, key):
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    return node
 
def deleteNode(root, k):
    if root is None:
        return root
 
    if root.key > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.key < k:
        root.right = deleteNode(root.right, k)
        return root
 
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
 
    else:
 
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
 
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
 
        root.key = succ.key
 
        del succ
        return root
    

def printLevelOrder(root):
    h = height(root)
    output=[]
    for i in range(1, h+1):
        #  print(i)
        #  func_output =printCurrentLevel(root, i)
        #  print(func_output)
        #  if (func_output is not None):
        #     output =func_output  + output
        output.append(printCurrentLevel(root,i))
    # print(output)
    return output


def printCurrentLevel(root, level):
    if root is None:
        return 
    if level == 1:
        print(root.key, end=",")
        # return root.key
        # return str(str(root.key)+" ") 
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


def height(node):
	if node is None:
		return 0
	else:

		lheight = height(node.left)
		rheight = height(node.right)
		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1
                
# Function for level Order Traversal
def levelOrderTraversal(root):
    ans = []
 
    # Return Null if the tree is empty
    if root is None:
        return ans
    
    # Initialize queue 
    queue = collections.deque()
    queue.append(root)
 
    # Iterate over the queue until it's empty
    while queue:
        # Check the length of queue
        currSize = len(queue)
        currList = []
 
        while currSize > 0:
            # Dequeue element
            currNode = queue.popleft()
            currList.append(currNode.key)
            currSize -= 1
 
            # Check for left child
            if currNode.left is not None:
                queue.append(currNode.left)
            # Check for right child
            if currNode.right is not None:
                queue.append(currNode.right)
        
        # Append the currList to answer after each iteration
        ans.append(currList)
 
    # Return answer list
    return ans

def Level_Order_Traversal(root):
  traversed = []
  traversed.append(root)
  if root is None:
    return traversed
  while traversed != []:
    print(traversed[0].key)
    x = traversed.pop(0) 
    if x.left:
      traversed.append(x.left)
    if x.right:
      traversed.append(x.right)

def levelorder(root):
    if not root:
        return []
    ret = []
    from collections import deque
    queue = deque([root])
    while queue:
        ret_row = []
        # fixed size for current level
        for _ in range(len(queue)):
            node = queue.popleft()
            ret_row.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ret.append(ret_row)
    return ret

 
if __name__ == '__main__':

    input_string = input()
    element_to_delete = int(input())

    list_of_input = input_string.split(', ')

    root = Node(int(list_of_input[0]))
    
    list_of_input.remove(list_of_input[0])
    #print(list_of_input)

    for element in list_of_input:
        root = insert(root, int(element))
    
    root = deleteNode(root, element_to_delete)
    # output = printLevelOrder(root)
    #output=levelOrderTraversal(root)
    #output=Level_Order_Traversal(root)
    output=levelorder(root)
    
    #print('\n')
    output_string=""
    firstelement = True
    for i in output:
        for x in i :
            if (not firstelement):
                output_string = output_string+ ', ' + str(x)
            if (firstelement):
                output_string = str(x)
                firstelement = False
            
    print(output_string)
    