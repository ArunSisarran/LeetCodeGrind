'''
goal: given a list return the k most frequent numbers in that list

add all values in the list to a hashmap with their occurances
create a heap
add all hashmap key values to the heap
loop through the heap and pop the first k elements
return those elements
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        heap = []
        result = []

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        for key, val in seen.items():
            heapq.heappush(heap, (-val, key))

        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result