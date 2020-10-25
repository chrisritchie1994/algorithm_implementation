let A = [ 7, 4, 5, 7, 6, 3];

function print(printable){
    console.log(printable)
}


function createList(arraySize) {
    return new Array(arraySize);
}


function merge(l, start, middle, end) {
    let n1 = middle - start + 1;
    let n2 = end - middle;
    let L = createList(n1+1);
    let R = createList(n2+1);
    for (let i=0; i < n1; i++) {
        L[i] = l[start + i];
    }
    for (let j=0; j < n2; j++){
        R[j] = l[middle + 1 + j];
    }

    L[n1] = Infinity;
    R[n2] = Infinity;

    let i = 0;
    let j = 0;

    for(let k = start; k < end + 1; k++) {
        if (L[i] <= R[j]) {
            l[k] = L[i];
            i += 1;
        }
        else {
            l[k] = R[j];
            j += 1;
        }
    }
}

function mergeSort(l, start, end) {
    if(start < end) {
        let middle = Math.floor(((start + end) / 2));
        mergeSort(l, start, middle);
        mergeSort(l, middle + 1, end);
        merge(l, start, middle, end);
    }
    return l
}

print(mergeSort(A, 0, A.length - 1))