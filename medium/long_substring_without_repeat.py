"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without duplicate characters.

Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m = charset size

1. Sliding Window Approach.
2. Optimized Sliding window
3. HashMap + Sliding window

What I learned:
* Sliding Window pattern is powerful for substring problems
* Two pointers: left and right define the current window
* Expand right to explore, shrink left to maintain constraint
* HashMap can store indices for optimization

Template:
def sliding_window(s):
    left = 0
    for right in range(len(s)):
        # Add s[right] to window

        # While constraint violated:
        while constraint_violated:
            # Remove s[left] from window
            left += 1

        # Update result
---------------------------------------------------------------------------

Visual Understanding
s = "abcabcbb"
     ↑
     left, right → "a" (length 1)

     ↑ ↑
     left right → "ab" (length 2)

     ↑   ↑
     left  right → "abc" (length 3)

     ↑     ↑
     left    right → "a" seen! Move left

       ↑   ↑
       left right → "bca" (length 3)

"""


def lengthOfLongestSubstring1(s):
  if len(s) == 0:
    return 0
  else:
    l = []
    ml = len(l)
    for i in range(0,len(s)):
      if s[i] in l:
        while s[i] in l:
          l.remove(l[0])
      l.append(s[i])
      ml = max(ml,len(l))
    return ml



def lengthOfLongestSubstring2(s):
  char_set = set()
  left = 0
  max_length = 0

  for right in range(len(s)):
    # If duplicate found, shrink window from left
    while s[right] in char_set:
      char_set.remove(s[left])
      left += 1

    # Add current character
    char_set.add(s[right])
    # Update max length
    max_length = max(max_length, right - left + 1)
  return max_length



def lengthOfLongestSubstring_optimized3(s):
  char_index = {}  # char -> last seen index
  left = 0
  max_length = 0
  for right in range(len(s)):
    # If character seen before and within current window
    if s[right] in char_index and char_index[s[right]] >= left:
      # Move left pointer to position after last occurrence
      left = char_index[s[right]] + 1
      # Update last seen index
      char_index[s[right]] = right

      # Update max length
      max_length = max(max_length, right - left + 1)
  return max_length

