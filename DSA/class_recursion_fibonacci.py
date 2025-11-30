
class solution:
    def __init__(self):
        self.store=dict()
    def function(self, num):
        if num in self.store:               #time complexity O(2**n)
                                            # each operation take further two extra operation
            return self.store[num]
        if num==0 or num==1:
            return num
        self.store[num]=self.function(num-1)+self.function(num-2)
        return self.store[num]
    def fib(self,n:int)->int:
        return self.function(n)
obj=solution()
answer=obj.fib(5)
print(answer)

