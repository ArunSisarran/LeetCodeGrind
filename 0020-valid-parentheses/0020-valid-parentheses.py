'''
Create a hashmap with all pairs of parentheses
Create a stack
Loop through the input string 
Push opening parentheses to the stack
If a closing parentheses if found pop from the stack
If a closing parenthese is found but the top of the stack is not the opening parenthese False
If the stack is empty at the end return true else return false
'''



class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for char in s:
            if char in valid and stack:
                if stack and stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return False if stack else True

# O(n)
# O(n)