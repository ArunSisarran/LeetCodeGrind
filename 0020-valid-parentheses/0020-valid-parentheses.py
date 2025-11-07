'''
return true or false if the string contains a valid set of parentheses

make a hashmap that contains closing and its respecitve opening parentheses
make a stack
push to the stack all the opening parentheses
pop from the stack once it sees the closing parentheses
if the stack is empty at the end its valid else its not
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char in pairs and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    stack.append(char)

        print(stack)
        return False if stack else True
