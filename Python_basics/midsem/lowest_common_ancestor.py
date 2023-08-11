#chris sunny 
#August 5th
class Node:
    def __init__(self, val): 
        self.val = val  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.val) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lowestcommonancestor(root, v1, v2):
    if (root.val < v1 and root.val > v2) or (root.val > v1 and root.val < v2):
        return root
    elif root.val < v1 and root.val < v2:
        return lowestcommonancestor(root.right, v1, v2)
    elif root.val > v1 and root.val > v2:
        return lowestcommonancestor(root.left, v1, v2)
    elif root.val == v1 or root.val == v2:
        return root

def lca(root, v1, v2):
    if (root.info < v1 and root.info > v2) or (root.info > v1 and root.info < v2):
        return root
    elif root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    elif root.info == v1 or root.info == v2:
        return root    
    
  

BSTtree_ = BinarySearchTree()
Number_ofNodes = int(input())

INPUT_ARRAY_ = list(map(int, input().split()))

for i in range(Number_ofNodes):
    BSTtree_.create(INPUT_ARRAY_[i])

List_of_nodes = list(map(int, input().split()))

Final_output = lowestcommonancestor(BSTtree_.root, List_of_nodes[0], List_of_nodes[1])
print (Final_output.val)