def find_factors(num):
    i=1
    li=[]
    while num>=i:
        
        if num%i==0:
            li.append(i)#
            i+=1
        else:
            i+=1
    return li



def find_fact(num):
    result=[]
    for i in range(1,num//2):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result
            
            
def find_factor(num):   
    result=[]         
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            
            result.append(i)
            if i != num//i:
                result.append(num//i)
    result.sort()
    return result # sorting time complexity O( n log n)
# factor time complexity O(sqrt(n)+ n log n)                

print(find_factor(15))
print(find_factor(20))
print(find_factor(25))
print(find_factor(7))