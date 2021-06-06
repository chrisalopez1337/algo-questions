const findThreeLargestNumbers = (array) => {
    let solution = [-Infinity, -Infinity, -Infinity];
    array.forEach(num => {
        if (num > solution[2]) {
            solution[0] = solution[1]
            solution[1] = solution[2]
            solution[2] = num
        } else if (num > solution[1]) {
            solution[0] = solution[1]
            solution[1] = num
        } else if (num > solution[0]) {
            solution[0] = num
        }
    });
    return solution;
}
