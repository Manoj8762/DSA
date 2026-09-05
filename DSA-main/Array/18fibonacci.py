class solve:
    def fun(self,n):
        if n==0 or n==1:
            return n
        return self.fun(n-1)+self.fun(n-2)
    def fib(self,n:int)->int:
        ans=self.fun(n)
        return ans
obj=solve()
print(obj.fib(8))


class solved:
    def func(self,n):
        if n==0 or n==1:
            return n
        return self.func(n-1)+self.func(n-2)
    def fibn(self,n:int)->int:
        solution=self.func(n)
        return solution
    
ob=solved()
print(ob.fibn(8))