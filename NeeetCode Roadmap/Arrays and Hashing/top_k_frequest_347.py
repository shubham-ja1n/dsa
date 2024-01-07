def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hash = {}
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    
    sorted_values = sorted(list(hash.values()))[-k:]
    result = []
    for key in hash:
        if hash[key] in sorted_values:
            result.append(key)
    
    return result