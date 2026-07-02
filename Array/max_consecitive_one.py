def max_consecutive_one(arr):
    n=len(arr)
    count=0
    max_count=0 
    for i in range(0,n):
        if arr[i]==1:
            count+=1     
        else:
            max_count=max(max_count,count)    
            count=0
                
    return max(max_count,count)
print(max_consecutive_one([0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,0,1,1,1,1,1,1,1]))
# time complexity => O(N) and space complexity=>O(1)



def max_consecutive_one(arr):
    n=len(arr)
    count=0
    max_count=0
    for i in range(0,n):
        if arr[i]==1:
            count+=1
            if max_count<count:
                max_count=count     
        else:
           count=0    
    return max_count
print(max_consecutive_one([0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,0,1,1,1,1,1,1,1]))
# time complexity => O(N) and space complexity=>O(1)






def max_consecutive(arr):
    n=len(arr)
    count=1
    max_count=1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        
        max_count=max(count,max_count)
    
        if arr[i]!=arr[i-1]:
            count=1
    return max_count
print(max_consecutive([0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,0,1]))

print(max_consecutive([1,1,2,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0]))
# time complexity => O(N) and space complexity=>O(1)