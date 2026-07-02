
#parameterized recursion

def sum_fun1(sum,i,n):
    if i>n:
        print(sum)
        return
    sum_fun1(sum+i,i+1,n)
sum_fun1(0,1,10)



