class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def insert(node, key):
    if node is None:
        return TreeNode(key)
 
    if key < node.val:
        node.left = insert(node.left, key)
    elif key > node.val:
        node.right = insert(node.right, key)
 
    return node

def delete_Node(root, key):
    if not root:
        return root
    if root.val > key:
        root.left = delete_Node(root.left, key)
    elif root.val < key:
        root.right= delete_Node(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        root.right = delete_Node(root.right,root.val)
    return root

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   

def printPostorder(node):
    if node == None:
        return
 
    printPostorder(node.left)
 
    printPostorder(node.right)
 
    print(node.val, end=' ')

def inorder(root):
        if root==None:
            return
        inorder(root.left)
        print(root.val)
        inorder(root.right)  

def smallestElementSumRec(root, k_list, count) :
    if (root == None) :
        return 0
    if (count[0] > k_list[0]) :
        return 0
    res = smallestElementSumRec(root.left, k_list, count)
    if (count[0] >= k_list[0]) :
        return res
    res += root.val
    count[0] += 1
    if (count[0] >= k_list[0]) :
        return res
    return res + smallestElementSumRec(root.right,
                                        k_list, count)
def smallestElementSum(root, k):
    count = [0]
    return smallestElementSumRec(root, k_list, count)

input_string = input()
K_element_to_delete = int(input())

list_of_input = input_string.split(' ')

root = TreeNode(int(list_of_input[0]))
for i in list_of_input:
    root = insert(root,key=int(i))

delete_Node(root , K_element_to_delete)

k_list = [K_element_to_delete]
output= smallestElementSum(root,k_list)
print(output)
