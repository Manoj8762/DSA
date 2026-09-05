def insert_interval(arr,new):
    n=len(arr)
    merged=[]
    for i in range(n):
        start,end=arr[i]

        if end<new[0]:
            merged.append([start,end])
        elif start>new[1]:
            merged.append(new)
            merged.extend(arr[i:])
            return merged
        else:
            new[0]=min(new[0],start)
            new[1]=max(new[1],end)
    merged.append([new[[0],new[1]]])
    return merged

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert_interval(intervals,newInterval))
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert_interval(intervals,newInterval))
    
