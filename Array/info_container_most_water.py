"""


Problem: Container With Most Water
Problem Statement

You are given an integer array height of length n.

There are n vertical lines drawn such that:

the two endpoints of the i-th line are:
(i, 0)
(i, height[i])

Find two lines that together with the x-axis form a container such that the container contains the maximum amount of water.

Return the maximum amount of water a container can store.

Important Notes
You may not slant the container.
The amount of water stored depends on:
Distance between lines (width)
Smaller height among the two lines
Formula

Area=min(height[i],height[j])×(j−i)

Example 1
Input
height = [1,8,6,2,5,4,8,3,7]
Output
49
Explanation

Choose:

line at index 1 → height 8
line at index 8 → height 7

Width:

8 - 1 = 7

Height used:

min(8,7) = 7

Water stored:

7×7=49

So maximum area = 49.

Example 2
Input
height = [1,1]
Output
1
Constraints
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
Expected Approach

Use:

Two Pointer Technique

Optimal complexity:

Time  : O(n)
Space : O(1)
    """
    
    
class Solution:
    def most_water(self,height):
        left=0
        right=len(height)-1
        
        max_water=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            
            area=width*h
            max_water=max(max_water,area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_water
    
solved=Solution()
a=[1,8,6,2,5,4,8,3,7]
b=solved.most_water(a)
print(b)

            