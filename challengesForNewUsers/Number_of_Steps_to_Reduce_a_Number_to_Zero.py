

class Solution:
    def numberOfSteps(self, num: int) -> int:
        for step in range(num+1):
            if num == 0:
                return step

            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
