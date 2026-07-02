def bubble_sort(ar):
    n=len(ar)
    
    for i in range(n-2,-1,-1):   #start from last two element
        for j in range(0,i+1):
            
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]   # replaces the large element comparively among them last posotion at the end of iteration if are out if order
    return ar
#print(bubble_sort([7,8,9,4,5,68,2,31,1]))     # time complexity O(n**2/2)


def bubble_sort(ar):
    c1=0
    n=len(ar)
    for i in range(n-2,-1,-1):   #start from last two element
        is_swap=False
        for j in range(0,i+1):
            c1+=1
            if ar[j]>ar[j+1]:               # descending requires only sign convertion in this line 
                ar[j],ar[j+1]=ar[j+1],ar[j] 
                is_swap=True         # replaces the large element comparively among them last posotion at the end of iteration if are out if order
            
        if is_swap==False:
            return ar ,c1
    return ar


#print(bubble_sort([1, 2, 4, 5, 7, 8, 9, 31, 68]))     # time complexity best case already all the elements are sorted then TC= O(n)

def bub(ar):
    m=len(ar)
    for i in range(m-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
                is_swap=True
        if is_swap==False:
            return ar
    return ar
print(bub([7,8,9,4,5,68,2,31,1]))