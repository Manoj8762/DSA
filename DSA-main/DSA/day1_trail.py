def char_hashing(n,m):
    hash_list=[0]*27
    for ch in n:
        asc_val=ord(ch)
        index=asc_val-97
        hash_list[index]+=1
    for ch in m:
        asc_val=ord(ch)
        index=asc_val-97
        print(hash_list[index],end=" ")
#print(char_hashing("aaadbaaaahdcssd",['d','a','y','u']))#

def count_freq(ar):
    new=dict()
    for i in range(len(ar)):
        new[ar[i]]=new.get(ar[i],0)+1
       
    return new
#print(count_freq(list("aaadbaaaahdcssd")))


