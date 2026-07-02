def funcc(x,n):
    if n == 0:
        return
    print(x)
    funcc(x, n - 1)
#funcc(15,4)

# printing 1 to n natural number using recursion

def number(x,n):
    if x>n:
        return          # head recursion
    print(x)
    number(x+1,n)
# number(1,5)
    
        

def numbers(x,n):
    if x>n:
        return          # tail recursion
    numbers(x+1,n)
    print(x)
    
#numbers(1,5)


def num(n):
    if n==0:
        return   #head recursion
    print(n)
    num(n-1)
#num(5)


def nums(n):
    if n==0:
        return
    nums(n-1)           #tail recursion
    print(n)
nums(5)


