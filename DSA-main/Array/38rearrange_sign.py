
#brute force approach

def rearrange_element_by_sign1(arr): 
    neg=[]
    pos=[] 
    res=[]
    for num in arr:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    for i in range(max(len(pos),len(neg))):
        res.append(pos[i])
        res.append(neg[i])
    return res
print(rearrange_element_by_sign1([5,10,-3,-1,-10,6]))

def rearrange(arr):
    n=len(arr)
    result=[0]*n
    pos=0
    neg=1
    for i in range(n):
        if arr[i]<0:
            result[neg]=arr[i]
            neg+=2
        else:
            result[pos]=arr[i]
            pos+=2
    return result