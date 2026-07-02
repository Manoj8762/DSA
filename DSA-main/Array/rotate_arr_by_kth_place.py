
def kth_right_rotation1(arr,k):
    n=len(arr)

    for _ in range(k):
        temp=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        
        arr[0]=temp
    return arr

#print(kth_right_rotation1([10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9],8))

def kth_right_rotation2(arr,k):
    n=len(arr)
    rotation=k%n
    R=rotation
    for _ in range(rotation):
        temp=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        
        arr[0]=temp
    return arr

#print(kth_right_rotation2([10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9],8))
#print(kth_right_rotation2([10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9],18)) # its  slight optimal solution TC=>O(R*N)
# time complexity => O(N*R)

def kth_right_rotation3(arr,k):
    rotation=k%len(arr)
    R=rotation
    for _ in range(rotation):
        e=arr.pop()
        arr.insert(0,e)
    return arr

#print(kth_right_rotation3([10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9],8))
# time complexity => O(N*R)


# slicing through

def kth_right_rotation5(arr,k):
    n=len(arr)
    r=k%n
    arr[:]=arr[n-r:]+arr[:n-r]
    return arr
#print(kth_right_rotation5([10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9],8))
# time complexity => O(N) => optimal but slicing through


# without sclicing

def reverse(arr, left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
        
                                            #11-4-1
arr=[10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
#[7, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
#[10, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
#[6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 7]
#[10, 1, 2, 3, 4, 5, 6, 9, 8, 7, 7]
#[7, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

n=len(arr)
k=8
r=k%n # Its required when the lenght of the array < k th value its not done then kth rotation required it increases the time complexity

# Step 1: reverse last k elements
reverse(arr, n-r, n-1)

# Step 2: reverse first n-k elements
reverse(arr, 0, n-r-1)

# Step 3: reverse whole array
reverse(arr, 0, n-1)

print(arr)

#time complexity => O(N)= k/2+(N-k)/2+N/2