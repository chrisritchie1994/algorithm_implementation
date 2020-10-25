import math

# p = start , r = end, q = middle

def merge(l, start, middle, end):
    n1 = middle - start + 1
    n2 = end - middle
    L = [None] * (n1+1)  # included the + 1 despite the zero, because range ends on the number before p2
    R = [None] * (n2+1)  # included the + 1 despite the zero, because range ends on the number before p2
    for i in range(0, n1):  # kept the n1 as of the value
        L[i] = l[start + i]  # removed negative 1 so wouldn't shoot back to end
    for j in range(0, n2):  # kept n2 because start at zero end at value before n2
        R[j] = l[middle + 1 + j] # had to add one so it strarted on the nextg 1

    L[n1] = math.inf  # remove the +1 because it will exceed the list length, and list starts at zeroth position
    R[n2] = math.inf  # remove the +1 because it will exceed the list length, and list starts at zeroth position

    i, j = 0, 0 # maybe could be wrong, maybe it should commence at the zeroth position

    for k in range(start, end + 1):  # added +1 to end of loop so ends on end #
        if L[i] <= R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1


def merge_sort(l, start, end):
    if start < end:

        middle = (start + end) // 2
        merge_sort(l, start, middle)
        merge_sort(l, middle + 1, end)
        merge(l, start, middle, end)

    return l

if __name__ == '__main__':
    l = [4, 0, 3, 7, 8, 1, 1, 3]
    x = merge_sort(l, 0, len(l)-1)
    print(x)
