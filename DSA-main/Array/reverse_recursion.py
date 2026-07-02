def reverse_recur(arr,left,right):
    if left>=right:
        return arr
    arr[left],arr[right]=arr[right],arr[left]
    return reverse_recur(arr,left+1,right-1)
        
    
arr=[1,2,3,4,5,6,7,8,9,10]
print(reverse_recur(arr,0,len(arr)-1))





def reverse(ar,left,right):
    if right<=left:
        return ar
    ar[left],ar[right]=ar[right],ar[left]
    return reverse(ar,left+1,right-1)
ar=[1,2,3,4,5,6,7,8,9,10]
print(reverse(ar,3,8))
    
    