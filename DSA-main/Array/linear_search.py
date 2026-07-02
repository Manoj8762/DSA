def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    
    return -1
    
print(linear_search([1,2,3,4,5,6,7,8],9))
