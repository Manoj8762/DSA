

#brute force approach
def three_sum1(arr,k):
    n=len(arr)
    seen=set()

    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    temp=[arr[i],arr[j],arr[k]]
                    temp.sort()
                    seen.add(tuple(temp))
    return [list(item) for item in seen]

print(three_sum1([-1,0,1,2,-1,-4,2],0))


#brute force approach with small optimization
def three_sum2(arr,k):
    n=len(arr)
    seen=set()
    
    for i in range(0,n):
        temp_set=set()
        for j in range(i+1,n):
            third=-(arr[i]+arr[j])
            if third not in temp_set:
                temp_set.add(arr[j])

            else:            
                temp=[arr[i],arr[j],third]
                temp.sort()
                seen.add(tuple(temp))
    return [list(item) for item in seen]

print(three_sum2([-1,0,1,2,-1,-4,2],0))

#optimal solution 
def three_sum3(arr,k):
    arr.sort()
    n=len(arr)
    listed=[]
    
    for i in range(0,n):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            total=arr[i]+arr[j]+arr[k]
            if total <0:
                j+=1
            elif total >0:
                k-=1
            else:
                temp=[arr[i],arr[j],arr[k]]
                listed.append(temp)
                j+=1
                k-=1

                while j<k and arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+1]:
                    k-=1
    return listed
        

print(three_sum3([-1,0,1,2,-1,-4,2],0))








