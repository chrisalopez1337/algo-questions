function nodeDepths(root) {
    let solution = 0,
        que = [{ node: root, level: 0}];
    while (que.length > 0) {
        const { node, level } = que.pop();
	solution += level;
	if (node.right) que.push({ node: node.right, level: level + 1 }); 
	if (node.left) que.push({ node: node.left, level: level + 1 }); 
    }
    return solution;
}
