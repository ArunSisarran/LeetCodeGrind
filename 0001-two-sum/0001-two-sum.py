class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i, num in enumerate(nums):
            complement = target - num

            if complement in map:
                return(map[complement], i)

            map[num] = i