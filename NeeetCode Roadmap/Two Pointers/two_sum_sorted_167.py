def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(numbers) - 1

    while l<r:
        curr_sum = numbers[l]+numbers[r]
        if curr_sum == target:
            return [l+1,r+1]
        elif curr_sum > target:
            r = r-1
        else:
            l = l+1