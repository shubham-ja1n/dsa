def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums =set(nums)
    longest = 0
    for val in nums:
        if val-1 not in nums:
            count = 0
            while (val+count) in nums:
                count += 1
            if count > longest:
                longest = count
    return longest