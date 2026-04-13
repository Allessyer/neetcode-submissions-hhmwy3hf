class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if len(stack) == 0:
                stack.append(b)
            else:
                cond1 = stack[-1] == '[' and b == ']'
                cond2 = stack[-1] == '(' and b == ')'
                cond3 = stack[-1] == '{' and b == '}'

                if cond1 or cond2 or cond3:
                    stack.pop()
                else:
                    stack.append(b)

        if len(stack) == 0:
            return True
        else:
            return False