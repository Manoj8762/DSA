def bst(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
ar=[10,20,30,40,50,60,70,80,90]

print(bst(ar,50))