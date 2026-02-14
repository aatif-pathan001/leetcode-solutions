"""
Two Sum - LeetCode Easy
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

Time Complexity

First solution: O(n²) - nested loops iterate through the array twice
Second solution: O(n) - single pass through the array

Space Complexity

First solution: O(1) - only uses a list to store result
Second solution: O(n) - uses a hash map to store seen numbers

Performance Comparison
For an array of 10,000 elements:

First: ~50 million operations (worst case)
Second: ~10,000 operations (worst case)

The second solution is ~5000x faster on large inputs!

** Searching through the Dictionary (Hash Table) in the second solution is much faster than searching through the list. **

"""

def twoSum1(nums, target):
        indice = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff = target - nums[i]
                if diff  == nums[j]:
                    indice.append(i)
                    indice.append(j)
                    break
        return indice


def twoSum2(nums, target):
        track = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in track:
                return [track[comp], i]
            track[num] = i
