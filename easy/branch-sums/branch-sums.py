def branchSums(root):
    # Write your code here.
	arr = []
	helper(root, 0, arr)
	return arr

def helper(node, pathSum, result):
	if node is None:
		return
	
	newRunningSum = pathSum + node.value
	
	if node.right is None and node.left is None:
		result.append(newRunningSum)
		return
	
	helper(node.left, newRunningSum, result)
	helper(node.right, newRunningSum, result)

