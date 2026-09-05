def sorting_binary(arr,target,low,high):
    if low>high:
         return -1
    
    mid=(low+high)//2
    if arr[mid]==target:
         return mid
    elif arr[mid]<target:
            return sorting_binary(arr,target,mid+1,high)
    else:
        return sorting_binary(arr,target,low,mid-1)
        
arr=[2,4,6,7,9,10,11,13,15]
low=0
high=len(arr)-1
target=6
print(sorting_binary(arr,target,low,high))

target=16
print(sorting_binary(arr,target,low,high))

target=8
print(sorting_binary(arr,target,low,high))

    

  
