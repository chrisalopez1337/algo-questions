const insertionSort(array) => {
    for (let i = 1; i < array.length; i++) {
        let j = i;
        while (j > 0 && array[j] < array[j-1]) {
            [array[j], array[i]] = [array[i], array[j]];
            j -= 1;
        }
    }
    return array;
}
