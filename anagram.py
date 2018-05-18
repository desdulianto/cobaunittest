def isAnagram(string1, string2):
    s1 = list(string1.lower())
    s2 = list(string2.lower())
    s1.sort()
    s2.sort()
    return s1 == s2
