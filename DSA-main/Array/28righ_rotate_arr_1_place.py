def r1otate_by_1(arr):
    n=len(arr)
    arr=[arr[n-1]]+arr[:n-1] # concatenation of 2 array is a array
    # this will save in a different memeory adress
    return arr

def r2otate_by_1(arr):
    n=len(arr)
    arr[:]=[arr[n-1]]+arr[:n-1] # concatenation of 2 array is a array
    # this will save in a same memeory adress 
    return arr



# this is the optimal solution
def r3otate_by_1(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[i]=temp
    return arr
print(r1otate_by_1([1,2,3,4,5,6,7,7,8,9,0,10]))
print(r2otate_by_1([1,2,3,4,5,6,7,7,8,9,0,10]))
print(r3otate_by_1([1,2,3,4,5,6,7,7,8,9,0,10]))


