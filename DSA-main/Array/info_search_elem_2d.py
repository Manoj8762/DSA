'''
Search in a 2D Matrix
Problem Statement

You are given an m x n integer matrix with the following properties:

Each row is sorted in ascending order.
The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return:

True if target exists in matrix
otherwise False

'''


class Solution:
    
    #bruteforce approach
    def search_elem1(self,mat,target):
        if not mat or len(mat)==0:
            return -1
       
        for row in mat:
            for num in row:
                if num==target:
                    return True
        return -1
        
    
    #optimal approach
    def search_elem2(self,mat,target):
        if not mat or len(mat)==0:
            return -1
        rows=len(mat)
        cols=len(mat[0])
        left=0
        right=rows*cols-1 # it will create virtual idex of last element
        
        while left<=right:
            mid=(left+right)//2 # creates mid value
            
            row=mid // cols
            col=mid % cols
            
            num=mat[row][col]
            
            if target==num:
                return True
            elif target>num:
                left=mid+1
            else:
                left=mid-1
        return -1

solved=Solution()
m=[[0,1,2],
   [3,4,5],
   [6,7,8]]
print(solved.search_elem1(m,9))
print(solved.search_elem2(m,9))
            
            