def reverse_array(ar,left,right):
    if left>=right:
        return ar
    ar[left],ar[right]=ar[right],ar[left]
    
    return reverse_array(ar,left+1,right-1)
<<<<<<< HEAD
a = [1,2,3,4,6,4,65,7,8,9,9,3,21,2,3]

#print(reverse_array(a, 0, len(a) - 1))


def rever(a,lef,rig):
    if lef>=rig:
        return a
    a[lef],a[rig]=a[rig],a[lef]
    return rever(a,lef+1,rig-1)

a1 = [1,2,3,4,6,4,65,7,8,9,9,3,21,2,3]
print(rever(a1,0,len(a1)-1))

=======
print(reverse_array([1,2,3,4,6,4,65,7,8,9,9,3,21,2,3],4,8))
    
   
>>>>>>> 4a6cc1fb1c73c27846510bed6f51a0267b6eaa47
