"""
Valid Anagram - LeetCode Easy
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s
"""


def isAnagram1(s, t):
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        return (a == b)

def isAnagram2(s, t):
        chars = {}
        for char in s:
            chars[char] = chars.get(char,0) + 1
        
        for char in t:
            if char not in chars:
                return False
            chars[char] -= 1
            if chars[char] <0:
                return False

        """flag = True
        for v in chars.values():
            if v != 0:
                flag = False
                """
        return all(v == 0 for v in chars.values())


def isAnagram3(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
             return False

        s_map, t_map = {}, {}

        for i in range(len(s)): #  single loop is run for two
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        return s_map == t_map
