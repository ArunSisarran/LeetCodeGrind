class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create a set becasue we are just checking of existence 
        # dont really need a hashmap because we dont need the pair
        # of values
        seen = set()

        # loop though the list
        for num in nums:

            # if the number is in the set already we know its duplicate
            if num in seen:
                return True

            # if its not then add it to the set
            seen.add(num)

        # if it breaks out of the for loop we know there are no duplicates
        return False
        
