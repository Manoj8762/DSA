

#brute force approach
def three_sum1(arr,k):
    n=len(arr)
    my_set=set()
    
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    temp=[arr[i],arr[j],arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return [list(ans) for ans in my_set ]


print(three_sum1([-1,0,1,2,-1,-4],0))


#better solution
def three_sum2(ar,k):
    n=len(ar)
    
    result_set=set()
    for i in range(0,n):
        my_set=set()
        for j in range(i+1,n):
            third=-(ar[i]+ar[j])
            if third in my_set:
                temp=[ar[i],ar[j],third]
                temp.sort()
                result_set.add(tuple(temp))
            my_set.add(ar[j])
            
    return [list(ans) for ans in result_set]
#print(three_sum2([-1,0,1,2,-1,-4],0))



#better solution
def three_sum3(ar,k):
    n=len(ar)
    ar.sort()
    ans=[]
    for i in range(n):
        if i!=0 and ar[i]==ar[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            total_sum=ar[i]+ar[j]+ar[k]
            if total_sum<0:
                j+=1
            elif total_sum>0:
                k-=1
            else:
                temp=[ar[i],ar[j],ar[k]]
                ans.append(temp)
                j+=1
                k-=1
                
                while j<k and ar[j]==ar[j-1]:
                    j+=1
                while j<k and ar[k]==ar[k-1]:
                    k-=1
    return ans
                
                
    #return [list(ans) for ans in result_set]
print(three_sum3([-2,-2,-2,-1,-1,0,0,0,2,2,2,2,-1],0))




def sum_3(a):
    a.sort()
    n=len(a)
    result=[]
    for i in range(n):
        if i!=0 and a[i]==a[i-1]:
            continue
        j=i+1
        k=n-1
        
        while j<k:
            total=a[i]+a[j]+a[k]
            if total<0:
                j+=1
            elif total>0:
                k-=1
            else:
                temp=[a[i],a[j],a[k]]
                result.append(temp)
                j+=1
                k-=1
                
                while j<k and a[j]==a[j-1]:
                    j+=1
                while j<k and a[k]==a[k-1]:
                    k-=1
    return result


print(sum_3([-2,-2,-2,-1,-1,0,0,0,2,2,2,2,-1]))




def three(arr):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        
        j=i+1
        k=n-1
        while j<k:
            total=arr[i]+arr[j]+arr[k]
            
            if total<0:
                j+=1
            elif total>0:
                k-=1
            else:
                temp=[arr[i],arr[j],arr[k]]
                ans.append(temp)
                
                while j<k and arr[j]==arr[j+1]:
                    j+=1
                while j<k and arr[k]==arr[k-1]:
                    k-=1
    return ans


print(three([-2,-2,-2,-1,-1,0,0,0,2,2,2,2,-1]))

    
