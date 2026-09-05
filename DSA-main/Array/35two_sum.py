

#brute force solution

def two_sum1(arr,target):
    for i in range(len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
    return -1

#print(two_sum1([5,9,1,2,4,15,6,3],13))



#optimal solution
def two_sum2(arr,target):
    n=len(arr)
    hash_map={}
    for i in range(n):
        remain=target-arr[i]
        if remain in hash_map:
            return [i,hash_map[remain]]
        hash_map[arr[i]]=i
    return -1

#print(two_sum2([5,9,1,2,4,15,6,3],8))



def two_sum3(arr,target):
    n=len(arr)
    hash_map={}
    for i in range(0,n):
        remaining=target-arr[i]
        if remaining not in hash_map:
            hash_map[arr[i]]=i
        else:
            print(hash_map[remaining],i)#+
    #return      

        
print(two_sum3([1,3,4,5,2,2,4,9],4))
print(two_sum3([5,9,1,2,4,15,6,3],8))