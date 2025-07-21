class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use a set to check if a val occurs more than once
        seen = set()
        # loop through the array
        for num in nums:

            # if the val appeared before return True
            if num in seen:
                return True

            # add the current num to the set
            seen.add(num)

        # return false if no val repeated
        return False