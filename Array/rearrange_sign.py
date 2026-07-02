
#brute force approach

def rearrange_element_by_sign1(arr):  
    pos=[]
    neg=[]
    for num in arr:         #  time complexity =>O(N)
        if num<0:
            neg.append(num)
        else:
            pos.append(num)             # space complexity =>O(N/2+N/2)
          
    lis=[]
    i=0
    j=0
    while i< len(pos) and j< len(neg):      #time complexity =>O(N/2)
        lis.append(pos[i])
        lis.append(neg[j])
        i+=1
        j+=1
    return lis
print(rearrange_element_by_sign1([5,10,-3,-1,-10,6]))


#brute force approach

def rearrange_element_by_sign2(arr):  
    pos=[]
    neg=[]
    for num in arr:         #  time complexity =>O(N)
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    n=len(arr)    
    lis=[0]*n
    for i in range(0,len(pos)):
        lis[i*2]=pos[i]
        lis[(i*2)+1]=neg[i]
    return lis
print(rearrange_element_by_sign2([5,10,-3,-1,-10,6]))



#optimal approach

def rearrange_element_by_sign3(arr):  
    n=len(arr)
    result=[0]*n
    pos_index=0
    neg_index=1

    for num in arr:         #  time complexity =>O(N)
        if num>=0:
            result[pos_index]=num
            pos_index+=2
            
        else:
           result[neg_index]=num
           neg_index+=2
          
    return result
print(rearrange_element_by_sign3([5,10,-3,-1,-10,6]))

    #  time complexity =>O(N)











