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
#print(merge_sorted_arr([1,3,4,5,7,7,9],[2,6,8,10]))
    

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_sorted_arr(left,right)
    
print(merge_sort([4,4,2,2,1,0]))
    




def merge_sorting1(left,right):
    m=len(left)
    n=len(right)
    i=j=0
    re=[]
    while i<m and j<n:
        if left[i]<=right[j]:
            re.append(left[i])
            i+=1
        else:
            re.append(right[j])
            j+=1
    while i<m:
        re.append(left[i])
        i+=1
    while j<n:
        re.append(right[j])
        j+=1
    return re

def merging(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merging(left_arr)
    right=merging(right_arr)

    return merge_sorting1(left,right)
print(merging([2,1,3,4,4,7,5,9]))

# def merge_sorting1(left,right):
#     m=len(left)
#     n=len(right)
#     i=j=0
#     re=[]

#     while i<m and j<n:
#         if left[i]<=right[j]:
#             re.append(left[i])
#             i+=1
#         else:
#             re.append(right[j])
#             j+=1

#     while i<m:
#         re.append(left[i])
#         i+=1

#     while j<n:
#         re.append(right[j])
#         j+=1

#     return re


# def mer(arr):
#     if len(arr)<=1:
#         return arr

#     mid=len(arr)//2

#     left_arr=arr[:mid]
#     right_arr=arr[mid:]

#     left=mer(left_arr)
#     right=mer(right_arr)

#     return merge_sorting1(left,right)


# print(mer([2,1,3,4,4,7,5,9]))