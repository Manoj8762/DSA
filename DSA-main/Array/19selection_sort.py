# selecting the smallest elemnt in a array then swap the position among both
# minmum index primarily 0
def selection_sort_asc(ar):
    n=len(ar)
    
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if ar[j]<ar[min_index]:             # time complexity O(N**2)
                min_index=j
        ar[i],ar[min_index]=ar[min_index],ar[i]
            
    return ar
#print(selection_sort_asc([4,5,7,8,9,5,62,3,66,4,3,21,1]))


# selecting the smallest elemnt in a array then swap the position among both
# minmum index primarily 0
def selection_sort_desc(ar):
    for i in range(0,len(ar)):
        max_index=i
        for j in range(i+1,len(ar)):
            if ar[j]>ar[max_index]:
                max_index=j
        ar[i],ar[max_index]=ar[max_index],ar[i]
    return ar
print(selection_sort_desc([4,5,7,8,9,5,62,3,66,4,3,21,1]))




def select(arr):
    n=len(arr)
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]
    return arr
print(select([4,5,7,8,9,5,62,3,66,4,3,21,1]))

def selec(arr):
    n=len(arr)
    for i in range(n):
        mn=i
        for j in range(i+1,n):
            if arr[mn]>arr[j]:
                mn=j
        arr[i],arr[mn]=arr[mn],arr[i]
    return arr

print(selec([4,5,7,8,9,5,62,3,66,4,3,21,1]))


