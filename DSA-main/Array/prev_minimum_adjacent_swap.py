# You are given a binary string S consisting only of '0' and '1'.
# Your task is to find the minimum number of adjacent swaps required to make all
#  identical characters appear together in one contiguous block.
# You have two choices:
# Group all '1' characters together.
# Group all '0' characters together.
# Return the minimum swaps required among the two options.
# Adjacent swap means swapping two neighboring characters.
# Input
# S = "1001"
# Output
# 0
# Explanation
# Grouping all 1s together:
# 1001 -> 0110
# Requires 1 swap.
# Grouping all 0s together:
# The 0s are already together, so it requires 0 swaps.
# Therefore, the minimum is:
# 0



def min_adjacent_swaps(s, ch):
    position=[]

    for i in range(len(s)):
        if ch==s[i]:
            position.append(i)
    n=len(position)
    if n<=1:
        return 0
    adjusted=[position[i]-i for i in range(n)]

    median=adjusted[n//2]

    return sum(abs(x-median) for x in adjusted)

s = "10101"
ones=min_adjacent_swaps(s, '1')#it will hold 2
zeros=min_adjacent_swaps(s, '0')#it will hold 1
print(min(ones,zeros))


s = "1100"
ones=min_adjacent_swaps(s, '1')#it will hold 0
zeros=min_adjacent_swaps(s, '0')#it will hold 0

print(min(ones,zeros))