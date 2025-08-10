class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            distance = sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (distance, point))

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result