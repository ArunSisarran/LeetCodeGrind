class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # in case any prefix sum from the start equals k        
        prefix_sum = {0: 1}
        total_sum = 0
        count = 0

        for num in nums:
            # add the current number to our sum variable
            total_sum += num

            # if sum - k is in the hashmap, increment count
            # by the value stored in that key
            if total_sum - k in prefix_sum:
                count += prefix_sum[total_sum - k]

            # add the sum as a key
            prefix_sum[total_sum] = prefix_sum.get(total_sum, 0) + 1

        return count