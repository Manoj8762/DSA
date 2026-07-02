def max_consecutive_sequence1(arr):
    n=len(arr)
    max_sequence=0
    count=0
    for i in range(0,n):
        num=arr[i]
        count+=1
        while num+1 in arr:
            num=num+1
            count+=1
        max_sequence=max(max_sequence,count)
        count=0
        
    return max_sequence

print(max_consecutive_sequence1([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(N**2)


#optimal solution

def max_consecutive_sequence2(arr):
    n=len(arr)
    arr.sort()
    
    longest=0
    #last_samller=float('-inf')
    count=1
    for i in range(1,n):
        if arr[i-1]==arr[i]:
            continue
         
        elif arr[i-1]+1==arr[i]:
            count+=1
            #last_samller=arr[i]
            longest=max(longest,count)
        
        else:
            count=1
            
    return longest
print(max_consecutive_sequence2([1,99,101,98,2,5,3,100,1,1]))        #time complexity O(N log N+N)






def max_consecutive_sequence3(arr):
    n=len(arr)
    arr.sort()
    longest=0
    last_samller=float('-inf')
    count=1
    for i in range(0,n):
        num=arr[i]
        if num-1==last_samller:
            count+=1
            last_samller=num
            longest=max(longest,count)
        elif num-1 != last_samller:
            count=1
            last_samller=num
        longest=max(longest,count)
        
    return longest
          

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
    






            