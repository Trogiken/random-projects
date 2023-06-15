def biggestNumberWithoutMax(lst):
    highest_number = lst[0]
    for big_num in lst:
        if highest_number <= big_num:
            highest_number = big_num
    return highest_number


print(biggestNumberWithoutMax([1, 2, 6, 3, 10, 7, 33, 16]))