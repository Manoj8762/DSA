#functional recursion

def sum_func(n):
    if n==1:
        return 1
    
    return n + sum_func(n-1)
x=sum_func(10)
print(x)
    
    
def fact_func(num):
    if num==1 or num==0:
        return 1

    return num * fact_func(num-1)
x=fact_func(5)
print(x)
