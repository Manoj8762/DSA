def overlapping(arr):
    over=[]
    for start,end in arr:
        if not over or over[-1][1]<start:
            over.append([start,end])
        else:
            over[-1][1]=max(over[-1][1],end)

print(overlapping([[1, 3],[2, 6],[8, 10],[9, 12]]))



def overlapp_interval(arr):

    overalpped=[]
    for st,end in arr:
        if not overalpped or overalpped[-1][1]<st:
            overalpped.append([st,end])
        else:
            overalpped[-1][1]=max(overalpped[-1][1],end)
    return overalpped

print(overlapp_interval([[2, 6],[8, 10],[9, 12]]))


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         merge=[]
#         interval=sorted(intervals,key=lambda x:x[0])
#         for start,end in interval:
#             if not merge or merge[-1][1]<start:
#                 merge.append([start,end])
#             else:
#                 merge[-1][1]=max(end,merge[-1][1])
#         return merge

