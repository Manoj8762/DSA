# N houses arranged in a line.
# C available colors.
# cost[i][j] = cost of painting house i with color j.
# Two adjacent houses cannot have the same color.
# Total cost must be <= B.
# Among all valid color assignments, find the minimum total cost.
# If the minimum cost is greater than B, return -1.

# 3=>N
# 3=>C
# 20=>B

# 1 5 3 
# 2 9 4 
# 3 1 7

# op=6


def minimum_cost_cal(cost,N,C,B):
    dp=[[float('inf')]*(C) for _ in range(N)]
    # print(dp)
    for color in range(C):
        dp[0][color]=cost[0][color]
    # print(dp)

    for i in range(1,N):
        for color in range(C):
            for prev in range(C):
                print(prev,color)
                if prev==color:
                    continue
                dp[i][color]=min(dp[i][color],dp[i-1][prev]+cost[i][color])
    # print(cost)
    # print(dp)
    ans=float('inf')
    for i in range(C):
        ans=min(ans,dp[N-1][i])
    if ans>B:
        return -1
    else:
        return ans

# N=int(input('enter the number of houses need to be painted '))
# C=int(input('enter the number of colors to paint '))
# B=int(input('total budget allocated '))
# # cost = [[0] * C for _ in range(N)]

# cost=[]
# for _ in range(N):
#     row=list(map(int,input().split()))
#     cost.append(row)
# print(minimum_cost_cal(cost,N,C,B))


N=3
C=3
B=20
c=[[1,5,3],[2,9,4],[3,1,7]]
print(minimum_cost_cal(c,N,C,B))