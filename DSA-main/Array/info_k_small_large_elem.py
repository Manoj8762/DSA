#bruteforce technique
class Solution:
    
    def kthSmallest(self, arr, k):

        arr.sort()

        return arr[k - 1]

    def kthLargest(self, arr, k):

        arr.sort()

        return arr[len(arr) - k]
    
    
# optimal using heapq    

import heapq

class Solution:

    # Kth Smallest Element
    def kthSmallest(self, arr, k):

        max_heap = []

        for num in arr:

            heapq.heappush(max_heap, -num)

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return -max_heap[0]



    # Kth Largest Element
    def kthLargest(self, arr, k):

        min_heap = []

        for num in arr:

            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
    