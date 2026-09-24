class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = defaultdict(int)
        heap = [] 

        for num in nums:
            map[num] += 1

        for num, count in map.items():
            heapq.heappush(heap, (-count, num))

        result = []
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result