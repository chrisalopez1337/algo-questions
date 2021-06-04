# I: Root node of a binary tree
# O: The depth sum of the tree
# --> Depth = each node is a value of parent node + 1 where the root is 0
# C: O(n) Time | O(h) space - where h is the height of the tree and n is the number of nodes
# E:

# General Idea: in this we are going to be using a BFS search and we can just start at the top and track the depth


def nodeDepths(root):
	solution = 0
	que = [{ "node": root, "level": 0}]
	while len(que) is not 0:
		current = que.pop()
		node, level = current["node"], current["level"]
		solution += level
		if node.left:
			que.append({"node": node.left, "level": level + 1})
		if node.right:
			que.append({"node": node.right, "level": level + 1})
	return solution
