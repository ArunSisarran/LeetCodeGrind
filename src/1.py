class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # created hash map
        num_map = {}

        # loops through nums keep track of their index and value i = index, num = value
        # enumerate generates a pair of value from nums, (index, value) which is stored in i,num
        for i, num in enumerate(nums):
            # finds the complement of the number
            complement = target - num
            # checks if that complement is already in the hash map
            # if it is already in the hashmap returns the complement index and the current index
            if complement in num_map:
                return [num_map[complement], i]

            # if the complement is not the index add the pair of values into the hashmap
            num_map[num] = i
