const productSum = (array, level=1) => {
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        const elem = array[i];
        if (Array.isArray(elem)) {
            sum += productSum(elem, level+1);
        } else {
            sum += elem;
        }
    }
    return sum * level;
}
