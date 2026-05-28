problem='''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters'''



class Solution1:
    
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        
        count=[0]*26
        for ch in s:
            count[ord(ch)-ord('a')]+=1
        for ch in t:
            if count[ord(ch)-ord('a')]==0:
                return False
            count[ord(ch)-ord('a')]-=1
        return True
'''
s,t=input().lower().split()
solved1=Solution1()
print(solved1.isAnagram(s,t))
'''



class Solution2:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        
        freq1={}
        freq2={}
        for i in range(len(s)):
            freq1[s[i]]=freq1.get(s[i],0)+1
            freq2[t[i]]=freq2.get(t[i],0)+1

        if freq1==freq2:
            return True
        else:
            return False
s,t=input().lower().split()
solved2=Solution2()
print(solved2.isAnagram(s,t))

