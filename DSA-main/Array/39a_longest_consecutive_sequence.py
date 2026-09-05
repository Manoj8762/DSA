def max_consecutive_sequence1(arr):
    n=len(arr)
    max_sequence=0
    count=0
    for i in range(n):
        num=arr[i]
        count=1
        while num+1 in arr:
            count+=1
            num+=1
        max_sequence=max(count,max_sequence)
    return max_sequence
print(max_consecutive_sequence1([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(N**2)


#small optimization solution

def max_consecutive_sequence2(arr):
    n=len(arr)
    arr.sort()
    long=1
    max_long=0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            continue
        elif arr[i]+1==arr[i+1]:
            long+=1
        else:
            max_long=max(max_long,long)
            long=1
    max_long=max(max_long,long)
    return max_long
            
print(max_consecutive_sequence2([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(N log N+N)



def max_consecutive_sequence4(arr):
    n=len(arr)
    arr.sort()
    last_small=float('-inf')
    max_long=0
    count=1
    for i in range(n):
        num=arr[i]
        if num-1==last_small:
            count+=1
            last_small=num
        elif num!=last_small:
            max_long=max(max_long,count)
            count=1
            last_small=num
        
    max_long=max(max_long,count)
    return max_long
            
print(max_consecutive_sequence4([1,99,101,98,2,5,3,100,1,1])) 

# small optimization
def max_consecutive_sequence3(arr):
    n=len(arr)
    if n==1:
        return 1
    max_cons=0
    my_set=set(arr)
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            
            while x+1 in my_set:
                count+=1
                x+=1
            max_cons=max(max_cons,count)
    return max_cons            
print(max_consecutive_sequence3([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(N log N+N)


#optimal solution

def max_consecutive_sequence3(arr):
    n=len(arr)
    my_set=set(arr)
    longest=0
    count=0    
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)
        
    return longest
          

print(max_consecutive_sequence3([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(3N)




def mx_consecutive(arr):
    count=0
    longest=float('-inf')
    my_set=set(arr)
    for num in my_set:
        x=num
        count=1
        while x+1 in my_set:
            x=x+1
            count+=1
        longest=max(longest,count)
    return longest

print(mx_consecutive([1,99,101,98,2,5,3,100,1,1]))
    






            