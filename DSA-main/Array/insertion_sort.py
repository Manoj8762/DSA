
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
print(insertion_sort1([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))
     
     

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
print(insertion([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))