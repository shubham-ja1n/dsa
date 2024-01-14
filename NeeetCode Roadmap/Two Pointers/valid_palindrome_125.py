def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    string = ""
    for char in s:
        if char.isalnum():
            string += char.lower()
    
    return string == string[::-1]