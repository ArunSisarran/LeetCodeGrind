'''
goal: given a list of nums return the k most frequent elements

create a hashmap
populate the hashmap with each value and how many time it appears
create a heap
create a result list
add all key value pairs to the heap
pop the first k elements of the heap into the result list
return the result list
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
        