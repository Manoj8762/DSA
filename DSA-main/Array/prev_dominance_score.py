# dp

#ip=5 2
# 1,2,2,1,2
#->1   | 2,2,1,2
#1+3=4
#op 4

#ip= 6 3
# 1,1,2,2,3,3
#->1,1 | ,2,2 | ,3,3
#2+2+2
#6
#op 6

# def dominance(arr,k,N):
#     mode=[[0]*(N+1) for _ in range(N+1)]
#     for l in range(1,N+1):
#         freq={}
#         for r in range(1,N+1):
#             val=arr[r-1]
#             freq[val]=freq.get(val,0)+1
#             mode[l][r]=max(mode[l][r-1],freq[val])
#     print(mode)

#     NEG=-1
#     dp=[[NEG]*(k+1) for _ in range(N+1)]
#     dp[0][0]= 0
#     print(dp)
    
#     for groups in range(1,k+1):
#         for i in range(1,N+1):
#             for j in range(groups-1,i):
#                 if dp[j][groups-1]==NEG:
#                     continue
#                 dp[i][groups]=max(dp[i][groups],dp[j][groups-1]+mode[j+1][i])
#     print(dp)
#     return dp[N][k]

# data=list(map(int,input().split()))
# N=data[0]
# k=data[1]
# arr=data[2:2+N]
# print(dominance(arr,k,N))


# def ca(arr,k,N):
#     mode=[[0]*(N+1) for _ in range(N+1)]

#     for s in range(1,N+1):
#         freq={}
#         for e in range(1,N+1):
#             val=arr[e-1]
#             freq[val]=freq.get(val,0)+1
#             mode[s][e]=max(mode[s][val],freq[val])
#     neg=float('-inf')
#     dp=[[neg]*(k+1) for _ in range(N+1)]
#     dp[0][0]=0

#     for groups in range(1,k+1):
#         for i in range(1,N+1):
#             for j in range(groups-1,i):
#                 if dp[j][groups-1]==neg:
#                     continue
#                 dp[i][groups]=max(dp[i][groups],dp[j][groups-1]+mode[j+1][i])
#     return dp[N][k]

# print(ca([1,2,2,1,2],2,5))


def cals(arr,k,N):
    mode=[[0]*(N+1) for _ in range(N+1)]
    for s in range(1,N+1):
        freq={}
        for e in range(s,N+1):
            val=arr[e-1]
            freq[val]=freq.get(val,0)+1
            mode[s][e]=max(mode[s][e-1],freq[val])
    neg=-1
    dp=[[-1]*(k+1) for _ in range(N+1)]
    dp[0][0]=0

    for groups in range(1,k+1):
        for i in range(1,N+1):
            for j in range(groups-1,i):
                if dp[j][groups-1]==neg:
                    continue
                dp[i][groups]=max(dp[i][groups],dp[j][groups-1]+mode[j+1][i])
    return dp[N][k]
print(cals([1,2,2,1,2],2,5))
print(cals([1,1,2,2,3,3],3,6))



def dominance_calculator(arr,k,N):
    mode=[[0]*(N+1) for _ in range(N+1)]

    for s in range(1,N+1):
        frequency={}
        for e in range(s,N+1):
            val=arr[e-1]
            frequency[val]=frequency.get(val,0)+1

            mode[s][e]=max(mode[s][e-1],frequency[val])

    dp=[[-1]*(k+1)for _ in range(N+1)]
    dp[0][0]=0

    for groups in range(k+1):
        for i in range(N+1):
            for j in range(groups-1,i):
                if dp[j][groups-1]==-1:
                    continue
                dp[i][groups]=max(dp[i][groups],dp[j][groups-1]+mode[j+1][i])
    return dp[N][k]


def dominance(arr, k, N):
    # ------------------------------------------------
    # STEP 1: Calculate mode score for every subarray
    # mode[l][r] = maximum frequency in arr[l-1:r]
    # ------------------------------------------------
    mode = [[0] * (N + 1) for _ in range(N + 1)]
    for s in range(1, N + 1):
        freq = {}
        for e in range(s, N + 1):
            val = arr[e - 1]
            freq[val] = freq.get(val, 0) + 1
            mode[s][e] = max(
                mode[s][e - 1],
                freq[val]
            )
    # ------------------------------------------------
    # STEP 2: DP
    #
    # dp[i][groups] =
    # maximum score for first i elements
    # divided into exactly groups groups
    # ------------------------------------------------
    NEG = -1
    dp = [[NEG] * (k + 1) for _ in range(N + 1)]
    # Base case
    dp[0][0] = 0
    # Number of groups
    for groups in range(1, k + 1):
        # Number of elements considered
        for i in range(1, N + 1):
            # j = position where last group starts
            for j in range(groups - 1, i):
                # Previous state is impossible
                if dp[j][groups - 1] == NEG:
                    continue
                
                
                    
                

                dp[i][groups] = max(
                    dp[i][groups],
                    dp[j][groups - 1] + mode[j + 1][i]# Previous groups + score of last group
                )

    return dp[N][k]

# data = list(map(int, input().split()))
# N = data[0]
# k = data[1]
# arr = data[2:2 + N]
print(dominance([1,2,2,1,2],2,5))
# print(dominance(arr, k, N))