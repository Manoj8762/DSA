def upper1(arr):
    row=len(arr)
    col=len(arr[0])
    for i in range(row):
        for j in range(col):
            if i<=j:   
                print(arr[i][j], end='')
            else:  
                print('*', end='')
        print()
a=[[5,10,8],
    [7,6,3],
    [2,1,9]]
upper1(a)

print('------------------------------------')
print('------------------------------------')

def lower1(arr):
    row=len(arr)
    col=len(arr[0])
    for i in range(row):
        for j in range(col):
            if i>=j:
                print(arr[i][j], end='')
            else:
                print('*', end='')
        print()

arr=[[5,10,8],
    [7,6,3],
    [2,1,9]]
lower1(arr)
print('------------------------------------')
print('------------------------------------')

def diagonal1(arr):
    row=len(arr)
    col=len(arr[0])
    for i in range(row):
        for j in range(col):
            if i==j:
                print(arr[i][j], end='')
            else:
                print('*', end='')
        print()

arr=[[5,10,8],
    [7,6,3],
    [2,1,9]]

diagonal1(arr)


print('------------------------------------')
print('------------------------------------')


def diagonal2(arr):
    row=len(arr)
    col=len(arr[0])
    for i in range(row):
        for j in range(col):
            if i+j==row-1:
                print(arr[i][j], end='')
            else:
                print('*', end='')
        print()

arr=[[5,10,8],
    [7,6,3],
    [2,1,9]]

diagonal2(arr)
print('------------------------------------')
print('------------------------------------')


def transpose1(arr):
    row=len(arr)
    col=len(arr[0])
    transpose=[[0]*row for _ in range(col)]
    print(transpose)
    for i in range(row):
        for j in range(col):
            transpose[j][i]=arr[i][j]
            
    for i in range(row):
        for j in range(col):
            print(transpose[i][j], end =' ')
        print()
            
        
    

arr=[[5,10,8],
     [7,6,3],
     [2,1,9]]

print(transpose1(arr))