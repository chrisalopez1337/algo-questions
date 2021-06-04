function findClosestValueInBst(tree, target) {
	return helper(tree, target, tree.value);
}

function helper(node, target, closest) {
	if (node.value === target) return node.value;
	
	const newDistance = Math.abs(target - node.value);
	const currentDistance = Math.abs(target - closest);
	
	if (newDistance < currentDistance) closest = node.value;
	
	if (node.value > target && node.left) {
		return helper(node.left, target, closest);
	} else if (node.value < target && node.right) {
		return helper(node.right, target, closest);
	} else {
		return closest;
	}
}
