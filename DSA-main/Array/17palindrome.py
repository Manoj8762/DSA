n=82428
num=n
rev=0
while num>0:
    remainder=num%10
    num=num//10
    rev=(rev*10)+remainder
print(True if n==rev  else False)



n=232
num=n
r=0
while num>0:
    r=num%10
    num=num//10
    rev=(rev*10)+r
print(True if rev==n else False)



def palin(s,left,right):
    if left>=right:
        return True
    
    if s[left]!=s[right]:
        return False
    return palin(s,left+1,right-1)


s="abcdefg"
left=0
right=len(s)-1
print(palin(s,left,right))