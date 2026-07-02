def merge_arrays(left,right):
    i,j=0,0
    result=[]
    m,n=len(left),len(right)
   
    while i<m and j<n:
        if left[i]<= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<m:
        while i<m:
            result.append(left[i])
            i+=1
        
    
    if j<n:
        while j<n:
            result.append(right[j])
            j+=1
    return result

def merge_sorting(ar):
    if len(ar)<=1:
        return ar
    mid=len(ar)//2
    left_arr=ar[:mid]
    right_arr=ar[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_arrays(left,right)

#print(merge_sort([7,8,9,9,4,56,6,2,3,0,2,3]))



def merge_array(left,right):
    i,j=0,0
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
            
            
    #result.extend(left[i:])        # with extend method also its possible
    #result.extend(right[j:])               
    
    if i<m:
        while i<m:
            result.append(left[i])
            i+=1
    if j<n:                                      # without extend list method is possible by use condition and while loop
        while j<n:
            result.append(right[j])
            j+=1
    
    
    
    return result


def merge_sort(ar):
    if len(ar)<=1:
        return ar
    mid=len(ar)//2
    left_ar=ar[:mid]
    right_ar=ar[mid:]
    left=merge_sort(left_ar)
    right=merge_sort(right_ar)
    return merge_array(left,right)

print(merge_sort([7,8,9,9,4,56,6,2,3,0,2,3]))

            
            
    