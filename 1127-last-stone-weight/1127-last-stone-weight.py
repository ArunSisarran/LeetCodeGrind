'''
array of nums
take the two biggest nums
x <= y
if x == y both nums get popped from array
else x gets popped and y = y - x
find what the last number in the array would be

use a minheap to keep track of all the weights
heap pop len(heap) and len(heap) - 1
do the check
push the new value back
loop until the len(heap) == 1
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x != y:
                new = y - x
                heapq.heappush(heap, -new)

        return -heap[0] if heap else 0