def colors_sorting(arr):
    # 0-> red
    #1-> blue
    #2-> orange
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
arr=[0,0,1,2,1,1,0,1,0,2,2,1,0]
print(colors_sorting(arr))