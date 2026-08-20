from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        speed = high

        while low < high:
            s=0
            speed = low + (high-low)//2

            for x in piles:
                s+=ceil(x/speed)
            if s>h:
                low = speed + 1
            else:
                high = speed
        
        return low



        