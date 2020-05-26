def bubble(list_a):
    indexing_length = len(list_a) - 1 # -1 bcos we can't compare last number to number after it because there isn't any
    sorted = False

    while not sorted:  # means as long as its not true, or is false
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

print(bubble([1,3,2,5,4,77,86,54,3]))

