def palindrome(s,left,right):
    
    if left>=right:
        return True 
    if s[left]!=s[right]:       #using recursion
        return False
        
    return palindrome(s,left+1,right-1)
st="malayalam"
#print(palindrome(st,0,len(st)-1))


def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:       #using while
            return False
        left+=1
        right-=1
    return True
s = "malayalam"
print(is_palindrome(s))