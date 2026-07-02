

def is_prime(num:int)->bool:
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    for i in range(4,int(num**0.5)+1):
        if num%i==0 or num%(i+2)==0:
            return False
    
    return True


def is_sum_prime(num:int)->bool:
    a=num
    s=0
    while a>0:
        remainder=a%10
        a=a//10
        s+=remainder
        
    return is_prime(s)



m=10
n=30
for i in range(m,n+1):
    if is_prime(i) and is_sum_prime(i):
        print(i)
