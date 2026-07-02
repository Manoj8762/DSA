def merge_sorted_arr(left,right):
    i=j=0
    result=[]
    m=len(left)
    n=len(right)
    
    while i<m and j<n:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    while i<m:
        result.append(left[i])
        i+=1
    
    while j<n:
        result.append(right[j])
        j+=1
        
    return result
print(merge_sorted_arr([1,3,4,5,7,7,9],[2,6,8,10]))


a=[9,1,2,7]
b=len(a)//2

c=a[:b]
print(c)
