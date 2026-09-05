
# brute force approach
def rotate_matrix(mat):
   
    m=len(mat)
    n=len(mat[0])
    res=[[0 for _ in range(m)] for _ in range(n)]
   # here after rotating 90 degree the column val of original matrix==row val of rotated matrix and colum of rotated become (n-1)-row val
    for i in range(m):
       for j in range(n):
           res[j][(n-1)-i]=mat[i][j]
    print(res)


mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

print(rotate_matrix(mat))
#time complexity= > O(N**2)
#space complexity= > O(N**2)



#optimal solution

# for transpose [i][j]=[j][i]
# but every time value of j>i so  
# if 
# i=0 ->j=1,2,3
#i=1 -> j=2,3
#i=2 ->j=3

#so 0->n-1
#   i+1->n

# time complexity for transpose ~O(N**2)
def transpose(mat):
    n=len(mat)
    for i in range(0,n-1):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    return mat
def rotate_90(mat):
    transpose(mat)
    for i in range(len(mat)): #time complexity O(N*N)
        mat[i].reverse()
    return mat    
mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
print(rotate_90(mat))


#time complexity= > O(2*N**2)
#space complexity= > O(1)

    
    
    
    
    
    