class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []

        for i in range(1,9):
            curr = i
            for j in range(i+1,10):
                curr = curr * 10 + j

                if low <= curr <= high:
                    res.append(curr)
        return sorted(res)
