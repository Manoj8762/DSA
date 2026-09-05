
#ascending

def insertion_sort1(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=key
    return arr
#print(insertion_sort1([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))

     
     

#descending 

def insertion_sort2(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j-=1
        
        arr[j+1]=key
    return arr
print(insertion_sort2([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))
        
        
        
        
def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
#print(insertion([1,7,78,6,6,1,5,4,3,3,2,2,5,6,7]))
#[1,7,6,78,6,1,5,4,3,3,2,2,5,6,7] key=6
#[1,6,7,78,6,1,5,4,3,3,2,2,5,6,7]


def i(a):
    n=len(a)
    for i in range(1,n):
        j=i-1
        key=a[i]
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
print(i([1,7,78,6,6,1,5,4,3,3,2,2,5,6,7]))
a=[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 78]
b=a.reverse()
print(b)


def inser(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>=key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

def inse(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 7, 78].reverse())
