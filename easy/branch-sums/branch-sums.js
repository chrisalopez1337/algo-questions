function branchSums(root) {
	let solution = [];
	helper(root, 0, solution)
	return solution;
}

function helper(node, runningSum, solution) {
	if (!node) return;
	const newRunningSum = runningSum + node.value;
	if (!node.left && !node.right) return solution.push(newRunningSum);
	helper(node.left, newRunningSum, solution);
	helper(node.right, newRunningSum, solution);
}
