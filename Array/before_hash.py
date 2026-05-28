def before(n,m):
    new={}
    set(m)
    for num in m:
        count=0
        if num<100:
            for x in n:
                if num==x:
                    count+=1
            new[num]=count
        else:
            continue
    return new
        #print(f'{num}:{count}')
        
n=[1,1,2,3,1,2,4,4,5,4,5,7,7,8,9,5,7,5,7,8]
m=[23,3,4,2,1,3,4,5,3,23,45,5,4,23,4,5,5,2,134,12]

print(before(n,m))