'''
goal: return the amount of subarrays that can sum up to k

observation: 
similar to two sum?
need to find n elements that sum up to k

Input: nums = [1,2,3], k = 3
Output: 2

1 + 2
3

make a hashmap
start with 0 in hashmap if first elem is a subarray
create a counter var to store the total
loop through the array continually summing up each new elemnt
take the complement sum - k
check if the complement is in the hashmap
if it is in hashmap increment counter as based on the amount of times its appeared 
if not in the hashmap add the current sum as the key and the amount of times it appears as value
return the counter

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        counter = sum = 0

        for i in nums:
            sum += i
            complement = sum - k

            if complement in seen:
                counter += seen[complement]
            
            seen[sum] = seen.get(sum, 0) + 1
        return counter