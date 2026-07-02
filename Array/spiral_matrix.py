def spiral_matrix1(mat):
    if not mat or len(mat[0])==0:
        return []
    left,right=0,len(mat)-1
    top,bottom=0,len(mat[0])-1
    
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            print(mat[top][i], end=' ')
        top+=1
        
        for i in range(top,bottom+1):
            print(mat[i][right],end=' ')
        right-=1
        
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(mat[bottom][i],end=' ')
            bottom-=1
            
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(mat[i][left],end=' ')
            left+=1
mat=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]    
print(spiral_matrix1(mat))



def spiral_matrix2(mat):
    if not mat or not mat[0]:
            return []
    left=0
    top=0
    right=len(mat)-1
    bottom=len(mat[0])-1
    result=[]
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            result.append(mat[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(mat[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(mat[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(mat[i][left])
            left+=1
    return result
mat=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]    
print(spiral_matrix2(mat))




def spiral(a):
    if not a or len(a)==0:
        return []
    left,right=0,len(a)-1
    top,bottom=0,len(a[0])-1
    
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            print(a[top][i],end=' ')
        top+=1
        
        for i in range(top,bottom+1):
            print(a[i][right],end=' ')
        right-=1
        
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(a[bottom][i],end=' ')
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(a[i][left],end=' ')
            left+=1
    return
mat=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]    
print(spiral(mat))
                

