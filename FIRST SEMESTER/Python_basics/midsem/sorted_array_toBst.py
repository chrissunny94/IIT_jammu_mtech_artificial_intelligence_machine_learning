 
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
 
 
def sortedArrayToBST(arr):
 
    if not arr:
        return None
 
    mid = (len(arr)) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root
 
def preOrder(node):
    if not node:
        return
    return str(node.data) + ' ' + str(preOrder(node.left))  + str(preOrder(node.right))
    print( node.data)
    preOrder(node.left)
    preOrder(node.right)
 
 
 
input_string = input()
list_of_input = input_string.split(', ')

#arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(list_of_input)
#print( "PreOrder Traversal of constructed BST ")
output_bst = preOrder(root)
#print(output_bst)
filterd_output = output_bst.replace('None','')
print(filterd_output)