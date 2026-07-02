
def function(num):

    if num==0 or num==1:
        return num                          # due each operation take further two operation
    num=function(num-1)+function(num-2)     # time complexity O(2**n)
    return num
def fib(n:int)->int:
    answer=function(n)
    return answer


result=fib(5)
#print(result)
    
    
def func(num):
    if num==0 or num==1:
        return num
    num=func(num-1)+func(num-2)
    return num
def fib(n:int)->int:
    ans=func(n)
    return ans
result=fib(5)
print(result)