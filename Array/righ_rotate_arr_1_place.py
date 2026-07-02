def right_rotate1(arr,k):
    
    arr = arr[-k:]+arr[:-k]
    
    return arr

print(right_rotate1([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10],2))   #adress change hota hai



def right_rotate2(arr,k):
    
    arr[:] = arr[-k:]+arr[:-k]
    return arr

print(right_rotate2([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10],2))  #same address space


def right_rotate3(arr,k):
    n=len(arr)
    arr[:] = arr[n-k:]+arr[:n-k]
    return arr

print(right_rotate3([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10],2))  #same address space without negative index 
#all three cases time complexity O(N)



# without using slicing

def right_rotate4(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr


print(right_rotate4([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]))
#time complexity O(N)