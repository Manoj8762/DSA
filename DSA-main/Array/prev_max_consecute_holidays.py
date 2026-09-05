# Yes — this is a sliding window / two-pointer problem.
# Given:
# n = 1 to 20
# m = 5 obligations
# k = 2 obligations can be deleted
# obligations = [3, 8, 12, 15, 18]
# We want the maximum number of consecutive days without obligations after deleting at most k obligations.


def max_cons_holidy(N,M,k,Obligation):
    left=0
    ans=0

    for right in range(M):

        while right-left+1 > k:
            left+=1

        previous=0 if left==0 else Obligation[left-1]
        next_day=N+1 if right==M-1 else Obligation[right+1]

        ans=max(ans, next_day -  previous-1)
    return ans

            
N,M,k=map(int,input().split())
Obligation=list(map(int,input().split()))
Obligation.sort()
print(max_cons_holidy(N,M,k,Obligation))


