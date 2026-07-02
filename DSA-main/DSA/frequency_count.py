def count_frequency(a):
    n=len(a)
    d={}
 #   for i in range(0,n):
 #       if a[i] in d:
 #           d[a[i]]+=1
 #       else:
 #           d[a[i]]=1
    for i in range(0,n):
        d[a[i]]=d.get(a[i],0)+1
 
    return d
print(count_frequency([1,2,3,1,2,3,21,3]))
        