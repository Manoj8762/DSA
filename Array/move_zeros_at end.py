
def move_zeros1(arr):
    n=len(arr)
    if n==1:
        return arr
    j=0
    for num in arr:         # O(N)
        if num !=0:
            arr[j]=num
            j+=1
    if j==n:
        return arr
        
    while j<n:                 #O(N-J)
        arr[j]=0
        j+=1
    return arr

#print(move_zeros1([1,0,2,4,3,0,0,3,5,1])) #O(N+N-J)


def move_zeros2(arr):
    n=len(arr)
    if n==1:
        return arr
    temp=[]
    for num in arr:         # O(N)
        if num !=0:
            temp.append(num)
    m=len(temp)
    for i in range(0,m):    # O(M)
        arr[i]=temp[i]
        
    for i in range(m,n):    ## O(N-M)
        arr[i]=0
              
    return arr

#print(move_zeros2([1,0,2,4,3,0,0,3,5,1]))

# time complexity => O(N+M+N-M)=>O(2N)



#optimal solution

def move_zeros3(arr):
    n=len(arr)
    if n==1:
        return arr
    i=0
    j=i+1
    while j<n:
        if arr[i]!=0:
            i+=1
        elif arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    return arr
#print(move_zeros3([1,0,2,4,3,0,0,3,5,1])) #O(N)


# #optimal solution inplace change


def move_zeros4(arr):
    n=len(arr)
    if n==1:
        return
    i=0
    j=i+1
    while j<n:
        if arr[i]!=0:
            i+=1
        elif arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    return 
#print(move_zeros4([1,0,2,4,3,0,0,3,5,1])) #O(N)


def move_zeros5(arr):
    n=len(arr)
    if n==1:
        return arr
    i=0
  
    while i<n:
        if arr[i]==0:
            break
        i+=1
            
    if n==i:
        return arr
    
    j=i+1
    
    while j<n:
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
        
    return arr
        
#print(move_zeros5([1,0,2,4,3,0,0,3,5,1])) #O(N)
#print(move_zeros5([1,2,4,3,3,5,1])) #O(N)



def move_zero_end(ar):
    n=len(ar)
    if n==1:
        return ar
    i=0
    while i<n:
        if ar[i]==0:
            break
        i+=1
    
    if i==n:
        return ar
    
    j=i+1
    while j<n:
        if ar[j]!=0:
            ar[j],ar[i]=ar[i],ar[j]
            i+=1
        j+=1
    return ar
