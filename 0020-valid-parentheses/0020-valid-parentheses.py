'''
goal: given a list of parentheses determine if they are valid

every opening parentheses must have a closing parentheses
create a stack
if its an opening parentheses add it to the stack
if we find a closing parentheses pop the opening from the stack
if there is anything left in the stack after we loop through list its not valid
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a hashmap with all the opening and closing pairs
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            # check if the current char is in the hashmap
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            # if its not a closing char add it to the stack
            else:
                stack.append(char)

        return True if not stack else False