def largest(arr):
    large=float('-inf')
    for num in arr:
        if num>=large:
            large=num 
    return large

#print(largest([4,4,2,2,1,0]))


def second_largest(arr):
    large=float('-inf')
    second_large=float('-inf')
    
    for num in arr:
        if num>large:
            second_large=large
            large=num
        elif num<large and second_large<num:
            second_large=num
    return second_large

print(second_largest([4,4,112,25,1,112]))



            