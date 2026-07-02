def hashings(n,m):
    hash_list=[0]*27
    for ch in n:
        asc_val=ord(ch)
        index=asc_val-97
        hash_list[index]+=1
    for ch in m:
        asc_val=ord(ch)
        index=asc_val-97
        print(hash_list[index] ,end=" ")
                
#print(hashing("aaadbaaaahdcssd",['d','a','y','u']))

def hashing(n,m):
    hash_list=[0]*27
    for ch in n:
        asci_val=ord(ch)
        index=asci_val-97
        hash_list[index]+=1
    for ch in m:
        asci_val=ord(ch)
        index=asci_val-97
        print(hash_list[index],end=' ')
print(hashing("aaadbaaaahdcssd",['d','a','y','u']))#