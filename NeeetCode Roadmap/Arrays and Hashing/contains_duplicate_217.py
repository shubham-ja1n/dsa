def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    my_hash = {}
    for num in nums:
        if num in my_hash:
            return True
        else:
            my_hash[num] = 1
    return False