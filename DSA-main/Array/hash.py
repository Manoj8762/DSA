def hashing(ar1,ar2):
    hash_map=[0]*11
    for ele in ar1:
        hash_map[ele]+=1
    for ele in ar2:
        if ele<=10 or ele<=1:
            print(hash_map[ele])
        else:
            print(0)
print(hashing([1,2,3,4,1,2,3,4,5,3,2,4,5,6,7,8,8,9,0,10],[1,12,3,4,14,15,17,18,6,8,9,10,100]))
