def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    hash = {}
    max_length = 0
    for right in range(len(s)):
        if s[right] in hash:
            left = max(hash[s[right]] + 1, left)
        hash[s[right]] = right
        max_length = max(max_length, right-left+1)
    
    return max_length