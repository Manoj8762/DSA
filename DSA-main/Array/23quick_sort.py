def partition(arr,low,high):
    p=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=p and i<=high-1:
            i+=1
        while arr[j]>p and j>=low+1:
            j-=1
                                            #10,5,77,9,2,1,7,14
                                            #10,5,7,9,2,1,77,14
                                            #1,5,7,9,2,10,77,14
                                            #1,5,2,9,7,10,77,14
                                            #1,2,5,9,7,10,77,14
                                            #1,2,5,7,9,10,77,14
                                            #1,2,5,7,9,10,14,77  
                                            #                                                                                           
        if i<j:                            
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        partition_index=partition(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
    return arr
    

arr=[2,2,5,6,7]
#arr=[5,5,5,5,5]
high=len(arr)-1
low=0
print(quick_sort(arr,low,high))




def partion_pivot(ar,low,high):
    piv=ar[low]
    i=low
    j=high
    while i<j:
        while ar[i]<=piv and i<=high-1:
            i+=1
        while ar[j]>=piv and j>=low+1:
            j-=1
        if i<j:
            ar[i],ar[j]=ar[j],ar[i]
    ar[low],ar[j]=ar[j],ar[low]
    return j

def partion(ar,low,high):
    if low<high:
        part_index=partion_pivot(ar,low,high)
        partion(ar,low,part_index-1)
        partion(ar,part_index+1,high)
    return ar

a=[2,2,5,6,7]
lo=0
h=len(a)-1
print(partion(a,lo,h))



def quick_sorts(arr,low,high):
    p=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=p and i<=high-1:
            i+=1
        while arr[j]>=p and j>=low+1:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def parti(arr,low,high):
    if low<=high:
        partition_index=quick_sorts(arr,low,high)
        parti(arr,low,partition_index-1)
        parti(arr,partition_index+1,high)
    return arr
        
a=[2,2,5,6,7]
h=len(a)-1
l=0
print(parti(a,l,h))



def quicking(arr,l,h):
    i=l
    j=h
    p=arr[l]
    while i<j:
        while arr[i]<=p and i<=h-1:
            i+=1

        while arr[j]>=p and j>=l+1:
            j-=1

        if i<j:
            arr[j],arr[i]=arr[i],arr[j]
    arr[l],arr[j]=arr[j],arr[l]
    return j
