"""
20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/description/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}":"{","]":"[",")":"("}

        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0