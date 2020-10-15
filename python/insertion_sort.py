
def insertion_sort(l):
    for j in range(0, len(l)):
        key = l[j]
        i = j - 1
        while i > -1 and l[i] > key:
            l[i+1] = l[i]
            i = i - 1
        l[i+1] = key

    print(l)

if __name__ == '__main__':
    l = [3, 4, 5, 7, 6, 3]
    insertion_sort(l)
