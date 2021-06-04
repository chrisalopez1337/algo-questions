// Doing it again in JS just for practice

const validateSubsequence = (array, sequence) => {
    let i = 0,
        x = 0;
    while (i < array.length && x < sequence.length) {
        if (sequence[x] === array[i]) x++;
        i++;
    }
    return x === sequence.length;
}

const array = [5, 1, 22, 25, 6, -1, 8, 10];
const sequence = [1, 6, -1, 10];
const expected = true;

console.log(validateSubsequence(array, sequence), expected);
