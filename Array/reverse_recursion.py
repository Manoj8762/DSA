def reverse_recur(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_recur(arr,left+1,right-1)
        
    return arr
arr=[1,2,3,4,5,6,7,8,9,10]
print(reverse_recur(arr,0,len(arr)-1))
    
    