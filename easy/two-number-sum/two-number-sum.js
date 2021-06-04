// Did it in python already just doing it in JS as well

const twoNumberSum = (array, targetSum) => {
    const seen = {};
    for (let i = 0; i < array.length; i++) {
        let target = targetSum - array[i];
        if (seen[target]) return [array[i], target];
        seen[array[i]] = array[i];
    }
    return [];
}

const array = [3, 5, -4, 8, 11, 1, -1, 6];
const targetSum = 10;
const expected = [-1, 11];

console.log(twoNumberSum(array, targetSum), expected);
