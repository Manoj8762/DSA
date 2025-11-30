def insertion_sort(ar):
    n=len(ar)
    for i in range(1,n):
        key=ar[i]
        j=i-1
        while j>=0 and ar[j]>key: # for convertion to descending needs condition with the key
            ar[j+1]=ar[j]
            j-=1
        
                                # time complexity O(n**2/2)
                                # first element as j
                                #second element considered as key
        
        ar[j+1]=key
    return ar
print(insertion_sort([3,5,6,4,8,9,7,1]))