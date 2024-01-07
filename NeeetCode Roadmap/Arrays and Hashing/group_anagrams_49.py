def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    final_map = {}
    for string in strs:
        sorted_word = ''.join(sorted(string))
        if sorted_word not in final_map:
            final_map[sorted_word] = [string]
        else:
            final_map[sorted_word] += [string]
    return list(final_map.values())