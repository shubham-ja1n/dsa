def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_hash = {}
    for i, num in enumerate(nums):
        if target-num in my_hash:
            return [my_hash[target-num], i]
        else: 
            my_hash[num] = i