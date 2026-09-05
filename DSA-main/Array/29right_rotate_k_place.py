#bruteforce approach
def rotate_by_k1(arr,k):
    n=len(arr)
    k=k%n
    for _ in range(k):
        e=arr.pop()
        arr.insert(0,e) #o(n)
    return arr
print(rotate_by_k1([1,2,3,4,5,6,7,8,8,9],3))


# small optimized using slicing
def rotate_by_k2(arr,k):
    n=len(arr)
    k=k%n
    arr[:]=arr[n-k:]+arr[:n-k]
    return arr
print(rotate_by_k2([1,2,3,4,5,6,7,8,8,9],3))



# this is the optimal solutions so it would take O(N)
#space complexity O(1)
def reverse(arr,s,e):
    while s<e:
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return

def rotate_by_k(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)
    return arr
print(rotate_by_k([1,2,3,4,5,6,7,8,8,9],3))