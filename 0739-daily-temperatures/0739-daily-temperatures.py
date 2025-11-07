'''
given an array of temps, return an array that represents the number of 
days that pass until a higher temp is found

use a stack and a result array of 0s
the result array is for the case where there are no hotter days
push to the stack the index of the temp we are tracking
check if the next temps are hotter than the temp we are tracking
if it is hotter pop from the stack (which is the index number)
do current index postion (hotter temp) - temp we were tracking index
this tells us how many days passed until there was a hotter temp
replace the index in the result array with the new value
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # fill result array with 0's for the case where it is no hotter days
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # while the stack exists and the current temp is greater than the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # index is the index of the temp we were tracking
                index = stack.pop()
                # replace that index in result with the current positon (the hotter temp index) - the temp we were tracking index
                res[index] = i - index
            stack.append(i)

        return res
