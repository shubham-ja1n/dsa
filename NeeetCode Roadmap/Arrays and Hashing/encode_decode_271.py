class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            while(str[j] != "#"):
                j = j + 1
            
            length = int(str[i:j])
            res.append(str[j+1: j+1+length])
            i = j+1+length
        return res