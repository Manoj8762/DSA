def duplicate_remove(arr):
    seen=set()
    clean=[]
    for num in arr:
        if num not in seen:
            clean.append(num)
            seen.add(num)
    return clean
#print(duplicate_remove([1,1,3,4,5,3,2,1,4,5,6,6]))


# remove duplicate element from the sorted array [in place] return the number of unique elements at the last of unique element within the array

def inplace_unique1(arr):
    freq=dict()
    for num in arr:
            freq[num]=0
    j=0
    for k in freq:
        arr[j]=k
        j+=1
    return j
#print(inplace_unique1([1,1,3,4,5,3,2,1,4,5,6,6]))


#optimal solution

def inplace_unique_optimal(arr):
    n=len(arr)
    if n==1:
        return arr
    i=0
    j=i+1
    while j<n:
        if arr[i]!=arr[j]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return arr
   
print(inplace_unique_optimal([1,1,2,3,4,5,1,16,7,8,9]))
print(inplace_unique_optimal([1,1,2,2,3,3,4,4,5,6,7,8,9,1,2,3]))



def remove_duplicates_sorted(arr):
    if not arr:
        return 0
    if len(arr)==1:
        return arr

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return arr[:i]

print(remove_duplicates_sorted([1,1,2,2,3,3,4,4,5,6,7,8,9,1,2,3]))
            
            