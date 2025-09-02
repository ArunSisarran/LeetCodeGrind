class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        return max(seen, key=seen.get)
