'''
goal: given an integer array nums return the k most frequent elements

add all integers to a hashmap
integer will be the key and frequency will be the value
add all of those key value pairs to a head
pop the heap based off of how many k we need
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        heap = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        # push the key value pairs onto the heap
        # using -val to make it behave like a max value heap
        # this makes it so the highest frequency would be the smallest number
        # therefore being at the top of the heap
        for key, val in seen.items():
            heapq.heappush(heap, (-val, key))

        result = []
        # add the top k elements of the heap to the result array
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result