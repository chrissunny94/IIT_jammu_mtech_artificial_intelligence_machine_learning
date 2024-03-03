INT_MAX = 2147483647
class createNode:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def insert(root, key) :
    if (root == None) :
	    return createNode(key)
    if (root.data > key) :
	    root.left = insert(root.left, key)
	elif (root.data < key):
	    root.right = insert(root.right, key)
	return root

def ksmallestElementSumRec(root, k, count) :
	if (root == None) :
		return 0
	if (count[0] > k[0]) :
		return 0
	res = ksmallestElementSumRec(root.left, k, count)
	if (count[0] >= k[0]) :
		return res
	res += root.data
	count[0] += 1
	if (count[0] >= k[0]) :
		return res
	return res + ksmallestElementSumRec(root.right,
										k, count)
def ksmallestElementSum(root, k):
	count = [0]
	return ksmallestElementSumRec(root, k, count)

if __name__ == '__main__':

	root = None
	root = insert(root, 20)
	root = insert(root, 8)
	root = insert(root, 4)
	root = insert(root, 12)
	root = insert(root, 10)
	root = insert(root, 14)
	root = insert(root, 22)
	
	k = [3]
	print(ksmallestElementSum(root, k))

