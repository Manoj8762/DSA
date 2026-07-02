
# brute force approach
def rotate_matrix(mat):
    n=len(mat)
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(0,n):
            result[j][n-1-i]=mat[i][j]
    return result


mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

print(rotate_matrix(mat))
#time complexity= > O(N**2)
#space complexity= > O(N**2)



#optimal solution

def transpose(mat,r):
   for i in range(0,r-1):
       for j in range(i+1,r):                   #time complexity= > O(N**2)
           mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

def rotate_matrix_90(mat):
    r=len(mat)
    c=len(mat[0])
    transpose(mat,r)
    
    
    for i in range(r):                  
        mat[i].reverse()                #time complexity= > O(N**2)
    
    return mat 

mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

print(rotate_matrix_90(mat))


#time complexity= > O(2*N**2)
#space complexity= > O(1    )

    
    
    
    
    
    