'''
return the k most frequent elements from nums

use a hashmap to record all frequencies
put the hashmap values into a max heap
loop throught the heap and pop the first k elements
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        heap = []
        result = []

        for num in nums:
            frequency[num] += 1

        for num, freq in frequency.items():
            heapq.heappush(heap, (-freq, num))

        while len(result) < k:
            result.append(heapq.heappop(heap)[1])

        return result
        