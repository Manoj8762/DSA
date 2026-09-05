def merge2_sort_to_unique1(left,right):
    m=len(left)
    n=len(right)
    i=0
    j=0
    result=[]

    while i<m and j<n:
        if left[i]<=right[j]:
            if not result or left[i]!=result[-1]:
                result.append(left[i])
            i+=1
        
        else: 
            if not result or right[j]!=result[-1]:
                result.append(right[j])
            j+=1
    while i<m:
        if not result or left[i]!=result[-1]:
            result.append(left[i])
        i+=1
        
    while j<n:
        if not result or right[j]!=result[-1]:
            result.append(right[j])
        j+=1
        
    
    return result
#print(merge2_sort_to_unique1([1,3,5,7,9,11,13,15],[2,4,6,7,8,10,12]))
# time complexity => O(M+N)



def merge2_sort_to_unique2(left,right):
    m=len(left)
    n=len(right)
    i=0
    j=0
    result=[]

    while i<m and j<n:
        if left[i]<=right[j]:
            if len(result)==0 or left[i]!=result[-1]:
                result.append(left[i])
            i+=1
        
        else: 
            if len(result)==0 or right[j]!=result[-1]:
                result.append(right[j])
            j+=1
    while i<m:
        if len(result)==0 or left[i]!=result[-1]:
            result.append(left[i])
        i+=1
        
    while j<n:
        if len(result)==0 or right[j]!=result[-1]:
            result.append(right[j])
        j+=1
        
    
    return result
print(merge2_sort_to_unique2([1,3,5,7,9,11,13,15],[2,4,6,7,8,10,12]))

# time complexity => O(M+N)



def merge(left,right): 
    i=0
    j=0
    m=len(left)
    n=len(right)
    res=[]
    while i<m and j<n:
        if left[i]<=right[j]:
            if len(res)==0 or res[-1]!=left[i]: # if not res or res[-1]!=left[i]:
                res.append(left[i])
            i+=1
        else:
            if len(res)==0 or res[-1]!=right[j]: # if not res or res[-1]!=right[j]:
                res.append(right[j])
            j+=1
    while i<m:
        if len(res)==0 or res[-1]!=left[i]: # if not res or res[-1]!=left[i]:
            res.append(left[i])
        i+=1
    while j<n:
        if len(res)==0 or res[-1]!=right[j]: # if not res or res[-1]!=right[j]:
            res.append(right[j])
        j+=1
    return res
print(merge([1,2,3,4,5,6,7,8],[5,6,7,8,9,10]))

            