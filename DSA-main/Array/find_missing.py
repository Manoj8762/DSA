def find_missing1(arr):
    n=len(arr)
    for i in range(0,n+1): #tc=>O(N)
        if i not in arr:  # time complexity of membership operator =>O(N)
            return i

#print(find_missing1([0,1,2,3,4,5,6]))

#tc => O(N pow 2)



def find_missing2(arr):
    n=len(arr)
    freq={}
    for i in range(n+1):
        freq[i]=0
    for num in arr:
        freq[num]=1
    for k,value in freq.items():
        if value==0:
            return k
#print(find_missing2([0,1,2,3,4,5,6])) #time complexity => O(3N)



# optimal solution 

def find_missing3(arr):
    n=len(arr)
    arr_sum=sum(arr)
    total_sum=n*(n+1)//2

    return total_sum - arr_sum

print(find_missing3([0,1,2,3,4,5,6,7])) #time complexity =>O(N)


def find_missing4(arr):
    
    n = len(arr)
    
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    
    return total_sum - arr_sum


#print(find_missing4([1,2,3,4,5,6,7,8]))    ##time complexity =>O(N)