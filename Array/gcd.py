

class Solution:
    # brute force approach
    def gcd1(self,m,n):
        ans=1
        for i in range(1,min(m,n)):
            if m%i==0 and n%i==0:
                ans=i
        return ans
    
    # optimal approach
    def gcd2(self,m,n):
        while n!=0:
            m,n=n,m%n
        
        return m
    
    #recursive optimal approach
    def recur_gcd(self,m,n):
        if n==0:
            return m
        return self.recur_gcd(n,m%n)
    
    import math
    print(math.gcd(18,12))
    
solved=Solution()
print(solved.gcd1(18,12))
print(solved.gcd2(18,12))
print(solved.recur_gcd(18,12))