import math
def minEatingSpeed(self, piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    l, r = 1, max(piles)
    k = r
    while l <= r:
        mid = (l+r) // 2

        timetaken = 0

        for value in piles:
            timetaken += math.ceil(value/mid)
        
        if timetaken > h:
            l = mid+1
        else:
            k = min(k, mid)
            r = mid-1
    return k