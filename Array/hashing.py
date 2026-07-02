def use_hash(n,m):
    result=[0]*12
    for num in n:
        #print(num)
        result[num]+=1

    for num in m:
        if num <1 or num >11:
            print(0)
        else:
          print(result[num])

    

print(use_hash([1,1,11,2,2,6,4,5,3,1,2,1,6,7,8,9,10],[120,14,1,5,65,7,4,6,8,9,10]))



def use_dict(n,m):
    result={}
    for num in n:
        if num in result:
            result[num]+=1
        else:
            result[num]=1
    for num in m:
        if num<1 or num>11:
            print(0)
        else:
            print(result[num])
print(use_dict([1,1,11,2,2,6,4,5,3,1,2,1,6,7,8,9,10],[120,14,1,5,65,7,4,6,8,9,10]))