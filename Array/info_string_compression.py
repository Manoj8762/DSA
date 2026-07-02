class Solution:
    def string_compress(self,string:str)->list:
        if len(string)==0:
            return []
        string=string.lower()
        i=0
        result=[]
        while i<len(string):
            ch=string[i]
            count=0
            while i<len(string) and string[i]==ch:
                count+=1
                i+=1
            result.append(ch)
            if count>=1:
                result.append(str(count))
        return result
            
            
solved=Solution()
print(solved.string_compress('aaabbccdD'))