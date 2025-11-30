def reverse_array(ar,left,right):
    if left>=right:
        return ar
    ar[left],ar[right]=ar[right],ar[left]
    
    return reverse_array(ar,left+1,right-1)
print(reverse_array([1,2,3,4,6,4,65,7,8,9,9,3,21,2,3],4,8))
    
   