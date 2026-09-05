def check_sort(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]>arr[i+1]:
            return -1
        else:
            continue
    return 'sorted'