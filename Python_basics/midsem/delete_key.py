# Python3 program to implement optimized delete in BST.
 
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
 
if __name__ == '__main__':

    input_string = input()
    element_to_delete = int(input())

    list_of_input = input_string.split(', ')

    root = None
    

    for element in list_of_input:
        root = insert(root, int(element))
    
    #print("Original BST: ", end='')
    #inorder(root)
 
    #print("\n\nDelete a Leaf Node: 20")
    #root = deleteNode(root, element_to_delete)
    #print("Modified BST tree after deleting Leaf Node:")
    #inorder(root)
    output_string = ""
    for i in range(0, len(list_of_input)):
        list_of_input[i] = int(list_of_input[i])
    list_of_input.remove(element_to_delete)
    first_value = True
    for i in list_of_input:
        if (not first_value):
            output_string = output_string+', ' + str(i)
        if first_value:
            output_string = str(i)
            first_value = False
        
    print(output_string)
    