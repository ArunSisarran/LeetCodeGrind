class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create empty hash map
        map = {}

        # loop through nums and add num as the key and the frequency of num as the value
        for num in nums:
            map[num] = map.get(num, 0) + 1

        # now sort all the items in the hashmap
        # the lamba function is saying for each pair x get the value at index 1 which is the frequency
        # the reverse = True part is saying to have it sorted in decending order
        sorted_elements = sorted(map.items(), key=lambda x: x[1], reverse=True)

        # return the first k values in the sorted list
        # this way of writing it is called list comprehension
        return [item[0] for item in sorted_elements[:k]]
