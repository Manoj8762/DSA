

def calculate(a,b,n,N):
    ans=0
    extra_cost=[]

    for i in range(n):
        ans+=a[i]

        city_b=b[i]+min(a[i],b[i])
        extra_cost.append(city_b-a[i])
    extra_cost.sort()
    for i in range(N):
        ans+=extra_cost[i]
    return ans
if __name__=='__main__':
    N=int(input('enter the number of employees need to go to per city '))
    n=N*2
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(calculate(a,b,n,N))

# ip=210 30 50 20 20 10 40 30
# data=list(map(int,input().split()))
# N=data[0]
# a=data[1:1+2*N]
# b=data[1+2*N:1+4*N]


# ip=2,10,30,50,20,20,10,40,30
# data=list(map(int,input().split(',')))
# N=data[0]
# a=data[1:1+2*N]
# b=data[1+2*N:1+4*N]


# First line contains N
# Second line contains N integers
# Third line contains N integers

# N = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))


# First line contains N
# Second line contains N*2 integers
# N = int(input())
# data = list(map(int, input().split()))
#a=data[0:2*N]
#b=data[2*N:4*N]
