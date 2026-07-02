nums = list(map(int, input().split()))
d = {}
for i in range(len(nums)):
    if nums[i] not in d:
        d[nums[i]] = 1
    else:
        d[nums[i]] += 1
ans = 0
for i in d.keys():
    if d[i] == 1:
        ans+=i
print(ans)





# both givr same result but in different approach
def only_one_freq_sum(ar):
    freq={}
    for num in ar:
        freq[num]=freq.get(num,0)+1
    print(freq)
    ans=sum(a for a in freq if freq[a]==1)
    return ans
    
a=[1,2,3,4,5,2,1,4,5,6,7,8,9]

b=only_one_freq_sum(a)
print(b)


def only_one_sum(arr):
    fre={}
    for num in arr:
        fre[num]=fre.get(num,0)+1
    print(fre)
    
    s=sum(a for a in fre if fre[a]==1)
    return s