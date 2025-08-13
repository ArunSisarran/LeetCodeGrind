'''
U: given an unsorted array of integer, return the length of the most numbers in sequence

M: We could use some kind of two pointer approach where we gradually move along the array checking if the n+1 element is exactly 1 bigger than the n element, and increment a counter variable everytime we do this.

I: First we sort the array that way it is easier for our two pointer to find numbers that consecurtively follow each other, then we use the two pointers to check if the n + 1 element is 1 bigger than the n element and then increment our counter vatiable. Once we are done with the array we can return our counter variable. Have two counter variables, one that keeps track of the current length and one that keeps track of the max length, then call the max function on those two variables and return the bigger one.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # declaration of variables and sorting the array
        nums_sorted = sorted(nums)
        max_length = 0
        current_length = 1
        print(nums_sorted)

        # early stopping if the array is empty
        if not nums:
            return 0

        # loop until the second to last element in the array
        for i in range(len(nums_sorted) - 1):
            
            

            # check if the next element is the same as the current element and skip it
            if nums_sorted[i + 1] == nums_sorted[i]:
                continue

            # check the absoulte values of the adjacent elements to see if they are in sequence
            elif abs(nums_sorted[i + 1] - nums_sorted[i]) == 1:

                # if they are increment the current length variable
                current_length += 1
            else:
                # if they are not in sequence update the max length variable to 
                # keep track of our current longest length
                max_length = max(current_length, max_length)
                print(current_length)
                current_length = 1

        # return the bigger of the two variables
        return max(current_length, max_length)