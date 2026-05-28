
def subarray_sum(arr, k):
    mpp = {0: 1}#hash map
    pre_sum = 0
    cnt = 0
    
    for num in arr:
        pre_sum += num
        rest = pre_sum - k
        cnt += mpp.get(rest, 0)
        mpp[pre_sum] = mpp.get(pre_sum, 0) + 1
    
    return cnt


#arr = list(map(int, input().split()))
#k = int(input())
arr=[1,3,4,5,7,7,9]
k=4

result = subarray_sum(arr, k)

print(result)





def sub_arrays_sum(arr,k):
    mpp={0:1}
    prev_sum=0
    count=0
    for num in arr:
        prev_sum+=num
        rest=prev_sum-k
        count+=mpp.get(rest,0)
        mpp[prev_sum]=mpp.get(prev_sum,0)+1
    return count

#arr=list(map(int,input().split()))
#k=int(input())
result=sub_arrays_sum([5,9,1,2,4,15,6,3],8)
