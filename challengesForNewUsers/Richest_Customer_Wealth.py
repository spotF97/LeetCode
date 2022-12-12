
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maxWelth = 0
        for row in accounts:
            maxWelth = max(maxWelth, sum(row))
        
        return maxWelth