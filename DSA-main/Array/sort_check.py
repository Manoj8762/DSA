def sort_check(arr):    
    for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
    return True
print(sort_check([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))
print(sort_check([1,2,3,4,5,5,8]))