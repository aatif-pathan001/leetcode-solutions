"""
Valid Anagram - LeetCode Easy
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s

Python offers two primary ways to count elements: the built-in count() method available for sequence types (strings, lists, and tuples), 
and the Counter class from the collections module for more advanced frequency counting. 

* count() method is a built-in function for strings, lists, and tuples
* collections.Counter class is a powerful dictionary subclass used to count the frequency of all hashable elements in an iterable, 
returning a dictionary-like object where elements are keys and their counts are values. 
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


def isAnagram3(s, t):
        if (len(s) != len(t)):
             return False

        s_map, t_map = {}, {}

        for i in range(len(s)): #  single loop is run for two
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        return s_map == t_map

from collections import Counter
def isAnagram4(s, t):
        return Counter(s) == Counter(t)
 
