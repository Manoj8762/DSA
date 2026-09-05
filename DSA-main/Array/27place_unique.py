# this is bruteforce approach

# time complexity O(2N)
# if the arr is sorted

def place_unique_count(arr):
    freq={}
    for num in arr:
        if num not in freq:
            freq[num]=0 #O(1)
    j=0

    for key in freq:
        arr[j]=key
        j+=1
    # print(len(set(arr)))
    return j
print(place_unique_count([1,2,3,4,5,6,7,8,9,9,0,0,1,2,3,3,4,4,5,6,7,8,8]))


#works only when the array is sorted if not then need to sort the array
# two pointer 
# time complexity O(N)

def place_unique(arr):
    n=len(arr)
    if n==1:
        return 1
    arr.sort()
    i=0
    j=i+1
    while j<n:
        if arr[i]!=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
           
        j+=1
    return i+1
print(place_unique([1,2,3,4,5,6,7,8,9,9,0,0,1,2,3,3,4,4,5,6,7,8,8]))


def unique_inplace(arr):
    n=len(arr)
    if n==1:
        return 1
    arr.sort()
    i=0
    j=i+1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
        j+=1
    return i+1

print(unique_inplace([1,2,3,4,5,6,7,8,9,9,0,0,1,2,3,3,4,4,5,6,7,8,8]))
    




    