"""
    Link: https://leetcode.com/problems/group-anagrams/

    Problem Statement:
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

    Time Complexity: O(n * k log k) where n = number of strings, k = max length
    Space Complexity: O(n * k)

    Approach: Use a sorted string as a key in hash map
    All anagrams will have the same sorted form  
"""



def groupAnagrams1(strs):
  h_t = {}
  for word in strs:
    w = list(word)
    w.sort()
    sw = ''.join(w)
    if sw not in h_t.keys():
      h_t[sw] = []
      l = h_t[sw]
      l.append(word)
      h_t[sw] = l
      
  out = [ val for val in h_t.values()]
  return out

def groupAnagrams2(strs):
  from collections import defaultdict
  
  anagrams = defaultdict(list)
  
  for word in strs:
    # Sort the word to create key
    # All anagrams have same sorted form
    key = ''.join(sorted(word))
    anagrams[key].append(word)
    
  return list(anagrams.values())

