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
        