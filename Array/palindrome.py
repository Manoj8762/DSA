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

    