def counting_sort(passedArray, highest_num):
    top = highest_num + 1
    count = [0] * top

    for a in passedArray:
        count[a] += 1
    i = 0
    for a in range(top):
        for c in range(count[a]):
            passedArray[i] = a
            i += 1
    return passedArray

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))
# print(counting_sort([1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1, 9], 7))

