class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                top_value = int(stack.pop())
                second_value = int(stack.pop())
                stack.append(second_value + top_value)
                print(second_value + top_value)

            elif token == "-":
                top_value = int(stack.pop())
                second_value = int(stack.pop())
                stack.append(second_value - top_value)
                print(second_value - top_value)

            elif token == "*":
                top_value = int(stack.pop())
                second_value = int(stack.pop())
                stack.append(second_value * top_value)
                print(second_value * top_value)

            elif token == "/":
                top_value = int(stack.pop())
                second_value = int(stack.pop())
                stack.append(second_value / top_value)
                print(second_value / top_value)

            else:
                stack.append(token)

        return int(stack.pop())