
# 1,2,3,4,0,0,9,8,7,9,0,0,9  
# =>   1,2,3,4,9,8,7,9,9,0,0,0,0

# brute force time complexity O(2N)
def move_zero1(arr):
    c=0
    a=[]
    if len(arr)==1:
        return
    for i in range(len(arr)):
        if arr[i]==0:
            c+=1
        else:
            a.append(arr[i])
    for _ in range(c):
        a.append(0)
    arr[:]=a
    return arr
print(move_zero1([1,2,3,4,0,0,9,8,7,9,0,0,9]))



# optimal solution


def move_zero(arr):
    n=len(arr)
    if n==1:
        return
    i=0
    j=1

    while j<n:
        if arr[i]==0 and arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        elif arr[j]==0:
            j+=1
        else:
          i+=1
        if j<=i:
            j=i+1  
    return arr
print(move_zero([1,2,3,4,0,0,9,8,7,9,0,0,9]))



#optimal solution with cleaner version of two pointer 


def move_zero2(arr):
    n=len(arr)
    if n==1:
        return
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

    return arr
print(move_zero2([1,2,3,4,0,0,9,8,7,9,0,0,9]))



#the optimal code is this because it will avoid unnessasary swaping/opertions
def move_zero3(arr):
    n=len(arr)
    if n==1:
        return
    i=0
    # this if the array has no zeros then no need to forward
    while i<n:
        if arr[i]==0:
            break
        i+=1
    if i==n:
        return
    # instead of swaaping entire array utill zero found in array then  we need to move the zero to the end 
    j=i+1
    while j<n:
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        j+=1
    return
print(move_zero3([1,2,3,4,0,0,9,8,7,9,0,0,9]))


