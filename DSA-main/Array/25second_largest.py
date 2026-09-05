def sec_largest(arr):
    large=float('-inf')
    second_large=float('-inf')
    n=len(arr)

    for num in arr:
        if num>large:
            second_large=large
            large=num
        elif num>second_large and num!=large:
            second_large=num
    return second_large
print(sec_largest([1,2,3,4,5.5,6,5,6,5,4,9,9,0,23,23,24]))