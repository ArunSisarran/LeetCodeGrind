'''
idea:
use a hashmap that holds a list that way you can store the value and timestamp with 
the key.
'''
from collections import defaultdict
class TimeMap:

    def __init__(self):
        # create the hashmap that will store the value and timestamp
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # create a values variable that holds a list of the current values of the given key
        values = self.hashmap[key]

        l, r = 0, len(values) - 1
        # binary search to check if the timestamps are <= the timestamp provided, if 
        # no timestamp is <= it returns an empty string 
        while l <= r:
            m = l + (r - l) // 2

            # check if the index m in the list has a timestamp that is <= given timestamp
            # if it does move the left pointer to after it to find any other values that may
            # be <= the given timestamp and then update the result variable
            if values[m][1] <= timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)