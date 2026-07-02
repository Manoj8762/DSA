def palind(str,left,right):
    if left>=right:
        return True
    
    if str[left]!=str[right]:
        return False
        
    return palind(str,left+1,right-1)
        
str="mom"
left=0
right=len(str)-1
print(palind(str,left,right))



# using while loop

def palindrome_while(str,left,right):
    
    while left<right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True
str="mom"
left=0
right=len(str)-1
print(palindrome_while(str,left,right))
        
    