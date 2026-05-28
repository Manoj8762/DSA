n=int(input())
a=[ int(input()) for _ in range(n)]
count=0
print(a)
for i in range(1,n):
    if i==n:
        break
    if (a[i-1]& a[i])*2<(a[i-1]|a[i]):
        count+=1

print(count)
        