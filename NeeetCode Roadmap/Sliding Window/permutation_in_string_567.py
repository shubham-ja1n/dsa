def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        return False
    alphabets_s1 = {}
    alphabets_s2 = {}
    for i in range(len(s1)):
        alphabets_s1[s1[i]] = 1 + alphabets_s1.get(s1[i], 0)
        alphabets_s2[s2[i]] = 1 + alphabets_s2.get(s2[i], 0)
    
    left = 0
    for right in range(len(s1), len(s2)):
        if alphabets_s1 == alphabets_s2:
            return True
        alphabets_s2[s2[left]] -= 1
        if alphabets_s2[s2[left]] == 0:
            del alphabets_s2[s2[left]]
        alphabets_s2[s2[right]] = 1 + alphabets_s2.get(s2[right], 0)
        left += 1
    return alphabets_s1 == alphabets_s2