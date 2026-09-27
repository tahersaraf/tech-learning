"""
2351. First Letter to Appear Twice

https://leetcode.com/problems/first-letter-to-appear-twice/description/
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for letter in s:
            if letter in seen:
                return letter
            seen.append(letter)