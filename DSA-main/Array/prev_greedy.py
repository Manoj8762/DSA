#Not understood
# # You are given N heat-doze/load values stored in an array heat.
# There are two types of queries:
# Type 1 — Update
# 1 pos value
# Update the heat value at position pos:
# heat[pos] = value
# Type 2 — Process a range
# 2 l r k critical
# For the range [l, r]:
# Consider every heat value from l to r.
# If a heat value is greater than or equal to critical, activate Turbo Mode and multiply that value by 4.
# Associate each resulting value with its original index.
# Sort these (value, index) pairs in descending order of value.
# Greedily select up to k indices.
# A new index can be selected only if its distance from every already-selected index is at least d:
# abs(previous_index - current_index) >= d
# Add the values of the selected elements to the query's total.
# The code you wrote then accumulates the result of all type-2 queries into ans.

def processQuery(heat, l, r, k, d, critical):
    arr = []
    # Step 1: Apply turbo mode
    for i in range(l, r + 1):
        value = heat[i]
        if value >= critical:
            value *= 4
        arr.append((value, i))
    # Step 2: Sort descending by value
    arr.sort(reverse=True)
    total = 0
    selected = []
    # Step 3: Greedily pick valid indices
    for value, idx in arr:
        valid = True
        # Check distance constraint
        for prev in selected:
            if abs(prev - idx) < d:
                valid = False
                break
        # Select if valid
        if valid:
            selected.append(idx)
            total += value
            # Maximum k elements
            if len(selected) == k:
                break
    return total


# Input
n = int(input())
d = int(input())
heat = list(map(int, input().split()))
q = int(input())
ans = 0
for _ in range(q):
    query_type = int(input())
    # Type 1: Update
    if query_type == 1:
        pos, value = map(int, input().split())
        heat[pos] = value
    # Type 2: Process query
    else:
        l, r, k, critical = map(int, input().split())
        ans += processQuery(
            heat,
            l,
            r,
            k,
            d,
            critical
        )

print(ans)