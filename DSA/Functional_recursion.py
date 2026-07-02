def sum_num(n):
    if n==1:
        return 1
    return n+sum_num(n-1)
#print(sum_num(5))
    
    
def fact_num(n):
    if n==1 or n==0:
        return 1
    return n*fact_num(n-1)
print(fact_num(5))
    