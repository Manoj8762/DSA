
# worst case of sorting using bubble sort

def bubble1(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


#print(bubble1([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))


# best case of sorting

def bubble(arr):
    is_swap=False
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                is_swap=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if is_swap==False:
            return 
    return arr


#print(bubble([9,78,7,6,6,1,5,4,3,3,2,2,5,6,7]))




def bub(arr):
    n=len(arr)
    is_swap=False
    for i in  range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                is_swap=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if is_swap==False:
            return 
    return arr
#print(bub([1,2,3,4,5,6,7,8,9]))
#print(bub([66, 62, 21, 9, 8, 7, 5, 5, 4, 4, 3, 3, 1]))

def bub1(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bub1([66, 62, 21, 9, 8, 7, 5, 5, 4, 4, 3, 3, 1]))

                

                
                
            