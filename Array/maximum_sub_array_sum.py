# bruteforce approach

def max_sub_array_sum1(arr):
    n=len(arr)
    
    maxi=float('-inf')
    for i in range(n):
        total=0
        for j in range(i,n):
            total+=arr[j]
            maxi=max(total,maxi)
        
    return maxi

print(max_sub_array_sum1([-2,1,-3,4,-1,2,1,-5,4,6]))
# time complexity => O(N **2 )
            
 
 # bruteforce approach           
            
def max_sub_sum2(arr):
    n=len(arr)
    
    maxi=float('-inf')
    for i in range(n):
       
        for j in range(i,n):
            total+=arr[j]
            maxi=max(total,maxi)
        total=0
      
    return maxi

print(max_sub_sum2([-2,1,-3,4,-1,2,1,-5,4]))
# time complexity => O(N **2 )



# optimal solution for this is 
# using kadane's algorithm

def max_sub_sum3(arr):
    maxi=float('-inf')
    total=0
    for num in arr:
        total+=num

        maxi=max(maxi,total)
        if total<0:
            total=0
      
    return maxi

print(max_sub_sum3([-2,1,-3,4,-1,2,1,-5,4]))

#time complexity => O(N)
#space complexity =>O(N)
            
            
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        