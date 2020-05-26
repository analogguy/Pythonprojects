def quick_sort(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop() #removes the last element and returns it to pivot then

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) #Can concatenate only list to list, not int, so we had to make pivot as list

print(quick_sort([3,2,99, 7, 5, 87, 12, 34, 33, 2]))   #sequence needs to be passed as a list

