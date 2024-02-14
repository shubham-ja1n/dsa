def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if t == "":
        return ""
    
    l = 0
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    have, need = 0, len(countT.keys())
    res, resLen = (-1,-1), float('inf')

    for r in range(len(s)):
        window[s[r]] = 1 + window.get(s[r], 0)

        if s[r] in countT and window[s[r]] == countT[s[r]]:
            have += 1

        while have == need:
            if (r-l+1) < resLen:
                res = (l, r)
                resLen = r-l+1
            window[s[l]] -= 1

            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    
    l, r = res
    return s[l:r+1] if not resLen == float('inf') else ""