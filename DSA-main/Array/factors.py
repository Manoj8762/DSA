def fact(num):
  
    n=num
    li=[]
    for i in range(1,n+1):
        if n%i==0:
            li.append(i)
        else:
            continue
    return li
#print(fact(num=24))

def facto(num):
    n=num
    li=[]
    for i in range(1,(n//2)+1):
        if n%i==0:
            li.append(i)
     
            
    li.append(n)    
    return li
#print(facto(num=24))


def factoria(num):
    n=num
    li=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            li.append(i)
            if i!=n//i:
                li.append(n//i)
    print(li)
    return sorted(li)
        
            
    return li
print(factoria(num=24))



from math import sqrt
def factorial(num):
    n=num
    li=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            li.append(i)
            if i!=n//i:
                li.append(n//i)
    print(li)
    return sorted(li)

#print(factorial(num=24))

            


    
