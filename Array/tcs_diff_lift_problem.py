members=int(input())
weights=list(map(int,input().split()))
weih=[int(input()) for _ in range(members)]
capacity=int(input())
weights.sort()
count=0
total_weight=0

for weigh in weights:
    if total_weight+weigh<=capacity:
        total_weight+=weigh
        count+=1
    
    else:
        break
    
print(count)    
