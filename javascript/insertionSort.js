
function insertionSort(l) {
    for (let j=1; j < l.length; j++) {
        let key = l[j];
        let i = j - 1;
        while (i > -1 && l[i] > key){
            l[i+1] = l[i];
            i = i - 1;
        }
        l[i+1] = key;

    }
    console.log(l)
}

l = [7, 4, 5, 7, 6, 3]
insertionSort(l);