# bruteforce approach
def max_sub_array_sum1(arr):
    n=len(arr)
    maxi=float('-inf')
    tot=0
    for i in range(0,n):
        tot=0
        for j in range(i,n):
            tot+=arr[j]
            maxi=max(maxi,tot)      
    return maxi

print(max_sub_array_sum1([-2,1,-3,4,-1,2,1,-5,4,6]))
# time complexity => O(N **2 )
 

# optimal solution for this is 
# using kadane's algorithm

def max_sub_sum3(arr):
    maxima=float('-inf')
    total=0
    for num in arr:
        total+=num
        maxima=max(total,maxima)
        if total<0:
            total=0
    return maxima
print(max_sub_sum3([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_sum3([-2,1,-3,4,-1,2,1,-5,4,6]))

#time complexity => O(N)
#space complexity =>O(N)
            
            
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        