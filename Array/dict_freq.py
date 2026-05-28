#method - 01

def freq_dict1(num):
   
    new=dict()
    for i in range(len(num)):
        if num[i] in new:
            new[num[i]]+=1
        else:
            new[num[i]]=1
    return new
num=[1,2,3,4,5,56,4,4,5,6,6,7,8,9,0,0,9,8,7,6,6,5,4,4,3,3,22,2,12,1]
#print(freq_dict1(num))

#time complexity O(n)


#method - 02


def freq_dict2(num):
       
    hash=dict()
    for i in range(len(num)):
        hash[num[i]]=hash.get(num[i],0)+1

    print(hash)
num=[1,2,3,4,5,56,4,4,5,6,6,7,8,9,0,0,9,8,7,6,6,5,4,4,3,3,22,2,12,1]

print(freq_dict2(num))


