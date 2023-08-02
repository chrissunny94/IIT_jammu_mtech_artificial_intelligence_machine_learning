
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
	# Base case
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

# Driver Code
if __name__ == '__main__':
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80
	root = None
	root = insert(root, 50)
	root = insert(root, 30)
	root = insert(root, 20)
	root = insert(root, 40)
	root = insert(root, 70)
	root = insert(root, 60)

	print("Original BST: ", end='')
	inorder(root)

	print("\n\nDelete a Leaf Node: 20")
	root = deleteNode(root, 20)
	print("Modified BST tree after deleting Leaf Node:")
	inorder(root)

	print("\n\nDelete Node with single child: 70")
	root = deleteNode(root, 70)
	print("Modified BST tree after deleting single child Node:")
	inorder(root)

	print("\n\nDelete Node with both child: 50")
	root = deleteNode(root, 50)
	print("Modified BST tree after deleting both child Node:")
	inorder(root)

