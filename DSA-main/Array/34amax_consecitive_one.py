def max_consecutive_one(arr):
    n=len(arr)
    count=0
    max_count=0
    for i in range(0,n):
        if arr[i]==1:
            count+=1
            max_count=max(max_count,count) # this will every time check the maximum but not optimal comared to below 
        else:
            count=0
    return max_count

print(max_consecutive_one([0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,0,1,1,1,1,1,1,1]))
print(max_consecutive_one([1,1,1,1,1,1,1,1,1,1,1]))
print(max_consecutive_one([1,2,1,2,1,2,1,2,1,2,1]))
# time complexity => O(N) and space complexity=>O(1)



def max_consecutive_one(arr):
    n=len(arr)
    count=0
    max_count=0
    for i in range(0,n):
        if arr[i]==1: # this will only check the maximum when other than 1 apear  and also 
            # one time after all the element exausted in the array

            count+=1  
        else:
           max_count=max(count,max_count)   
           count=0    
    return max(max_count,count)
print(max_consecutive_one([0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,0,1,1,1,1,1,1,1]))
# time complexity => O(N) and space complexity=>O(1)


