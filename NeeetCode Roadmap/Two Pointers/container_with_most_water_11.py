def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    volume = 0
    l = 0
    r = n-1
    while l < r: 
        if height[l] > height[r]:
            curr_volume = height[r] * (r-l)
            r = r-1
        elif height[l] < height[r]:
            curr_volume = height[l] * (r-l)
            l = l+1
        else:
            curr_volume = height[l] * (r-l)
            if height[l+1] > height[r-1]:
                l = l+1
            else:
                r = r-1
        volume = max(curr_volume, volume)
        
    return volume