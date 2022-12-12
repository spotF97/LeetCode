
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        l = []
        for i in range(1, n+1):

            fizz = i % 3 == 0
            buzz = i % 5 == 0

            if fizz and buzz:
                l.append("FizzBuzz")

            elif fizz:
                l.append("Fizz")

            elif buzz:
                l.append("Buzz")
            
            else:
                l.append(str(i))

        return l