def max_consecutive_element2(arr):
    n=len(arr)
    max_count=0
    count=1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            max_count=max(max_count,count)
            count=1
    return max(max_count,count)
print(max_consecutive_element2([1,1,1,2,3,3,3,3,4,4,5,6,7]))


def max_consecutive_element1(arr):
    n=len(arr)
    max_count=0
    count=1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            max_count=max(max_count,count)
            count=1
    return max(max_count,count)
print(max_consecutive_element1([1,1,1,2,3,3,3,3,4,4,5,6,7]))
# the above code is optimal as compared with the below code

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
print(max_consecutive([1,1,1,2,4,4,5,6,7,3,3,3,3]))

# time complexity => O(N) and space complexity=>O(1)

        