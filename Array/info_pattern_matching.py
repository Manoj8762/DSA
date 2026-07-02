class Solution:
    def pattern_match(self,string:str,pattern:str)->list:
        m=len(pattern)
        n=len(string)
        result=[]
        if m>n or m==0:
            return []
        
        for i in range(0,n-m+1):
            if string[i:m+i]==pattern:
                result.append(i)
        return result
solved=Solution()
print(solved.pattern_match('AABAACAADAABAABA','AABA'))



#kmp algorithm
