'''
task : find all sub arrays that add up to target

use a hashmap to store all seen values and how many times we have seen them
loop through the array and sum up each new element with the previous
take the complement of the sum
sum - k
if that complement is in the hashmap we know we can make a subarray
add to the counter as many times as we are able to make the target number
return the counter

hashmap is oringally populated with 0 to handle the case where a subarray is the first element
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        sum = count = 0

        for i in nums:
            sum += i
            complement = sum - k

            if complement in seen:
                count += seen[complement]

            seen[sum] = seen.get(sum, 0) + 1

        return count