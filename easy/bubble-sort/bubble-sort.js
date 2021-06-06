const bubbleSort = (array) => {
    let swapped = false,
        i = 0;
    while (i < array.length-1) {
        if (array[i] > array[i+1]) {
            [ array[i], array[i+1] ] = [ array[i+1], array[i] ];
            swapped = true;
        } i++;
    }
    return swapped ? bubbleSort(array) : array
}

// General idea with bubble sort is to "bubble up" the larger numbers 
