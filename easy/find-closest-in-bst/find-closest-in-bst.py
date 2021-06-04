# I: Root of a BST, and a target int
# O: value in the BST closest to the target int
# C: O(log(n)) Time | O(1) Space
# E: N/A

# Basic Idea: We want to recurse through the tree while storing the closest
# value to the target and when we have no more nodes to traverse, return that

def findClosestValueInBst(tree, target):
	return helper(tree, target, tree.value)

def helper(node, target, closest):
	if node.value == target:
		return node.value
	newDistance = abs(target - node.value)
	closestDistance = abs(target - closest)
	if newDistance < closestDistance:
		closest = node.value
	if node.value < target and node.right is not None:
		return helper(node.right, target, closest)
	elif node.value > target and node.left is not None:
		return helper(node.left, target, closest)
	else:
		return closest
