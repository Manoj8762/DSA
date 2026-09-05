#brute force approach
def mark_infinity(mat,row,col):         # time complexity => O(N+M)
    r=len(mat)
    c=len(mat[0])
    for i in range(r):
        if mat[i][col]!=0:
            mat[i][col]=float('inf')
    for j in range(c):
        if mat[row][j]!=0:
            mat[row][j]=float('inf')
    return

def set_matrix_zeros1(mat): # time complexity => O(N*M)+O(N*M)
    m=len(mat)
    n=len(mat[0])
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                mark_infinity(mat,i,j)
    for i in range(m):
        for j in range(n):
            if mat[i][j]==float('inf'):
                mat[i][j]=0
    return mat
        
    # for i in range(m):
    #     for j in range(n):
    #         print(mat[i][j],end=' ')
    #     print()
            
mat=[[7,2,6,4],
     [10,5,0,5],
     [1,0,5,4],
     [7,5,4,6]]

print(set_matrix_zeros1(mat)) # total time complexity =>O(N+M)+O(N*M)+O(N*M)




#optimal solition

def set_matrix_zeros2(mat): # time complexity => O(N*M)+O(N*M)
   
    r=len(mat)
    c=len(mat[0])
    row_track=[0 for _ in range(r)]
    col_track=[0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if mat[i][j]==0:
                row_track[i]=-1
                col_track[j]=-1
    for i in range(r):
        for j in range(c):
            if row_track[i]==-1 or col_track[j]==-1:
                mat[i][j]=0
    return mat
    
mat=[[7,2,6,4],
     [10,5,0,5],
     [1,0,5,4],
     [7,5,4,6]]

print(set_matrix_zeros2(mat)) # total time complexity =O(2*N*M)


print([0]*5)