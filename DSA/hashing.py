def check_array_frequency(n,m):                 #1<= num <=10
    hash_list=[0]*11
    for num in n:      # Time complexity O(n)   #
        hash_list[num]+=1
        result=[]
    for num in m:           # time complexity O(m) 
        if num <1 or num > 10:
            print(0,end=" ")
        else:
            print(hash_list[num],end=" ")
    
#print(check_array_frequency([1,1,2,3,3,4,4,7,8,9,5,6,2,3,2,4,10,10,10],[14,45,74,56,10,66,10,4,42,20,3]))


def check_array_freq(n,m):
    hash_list=[0]*11
    for num in n:
        hash_list[num]+=1
    for num in m:
        if num<1 or num>10:
            print(0,end=' ')
        else:
            print(hash_list[num],end=" ")
            
print(check_array_freq([1,1,2,3,3,4,4,7,8,9,5,6,2,3,2,4,10,10,10],[14,45,74,56,10,66,10,4,42,20,3]))
            
              