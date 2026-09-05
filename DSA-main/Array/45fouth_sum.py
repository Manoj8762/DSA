# this is brute force approach

def find_four_sum1(arr,target):
    n=len(arr)
    seen=set()
    
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            temp_set=set()
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    total=arr[i]+arr[j]+arr[k]+arr[l]
                    if total==target:
                        temp=[arr[i],arr[j],arr[k],l]
                        temp.sort()
                    seen.add(tuple(temp))
    return [list(item)for item in seen]

a=[1,0,-1,0,2,-2,5,9]
target=0
print(find_four_sum1(a,target))




# this is brute force approach with small optimization

def find_four_sum2(arr,target):
    n=len(arr)
    seen=set()  
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            temp_set=set()
            for k in range(j+1,n-1):
                l=-(arr[i]+arr[j]+arr[k])
                if l not in temp_set:
                    temp_set.add(arr[k])
                else:    
                    temp=[arr[i],arr[j],arr[k],l]
                    temp.sort()
                    seen.add(tuple(temp))
    return [list(item)for item in seen]

a=[1,0,-1,0,2,-2,5,9]
target=0
print(find_four_sum2(a,target))


# optimal solution

def find_four_sum3(arr,target):
    n=len(arr)
    result=[]
    arr.sort()
    for i in range(0,n-3):
        if i!=0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        for l in range(n-1,3,-1):
            if l!=n-1 and arr[l]==arr[l+1]:
                continue
            k=l-1
            while j<k:
                total=arr[i]+arr[j]+arr[k]+arr[l]

                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    temp=[arr[i],arr[j],arr[k],arr[l]]
                    result.append(temp)
                    j+=1
                    k-=1

                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
    return result
                    
a=[1,0,-1,0,2,-2,5,9]
target=0
print(find_four_sum3(a,target))


def find_four_sum4(arr,target):
    n=len(arr)
    result=[]
    arr.sort()
    for i in range(n-3):
        if i<0 and arr[i]==arr[i-1]:
            continue
        
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                total=arr[i]+arr[j]+arr[left]+arr[right]

                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    temp=[arr[i],arr[j],arr[left],arr[right]]
                    result.append(temp)
                    left+=1
                    right-=1

                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:

                        right-=1
    return result

a=[1,0,-1,0,2,-2,5,9]
target=0
print(find_four_sum4(a,target))




