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
