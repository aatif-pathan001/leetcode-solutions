"""
https://leetcode.com/problems/contains-duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

set:-  unstructured (no-indexing) and unique values. Set operations are powerful for uniqueness checks

Time Complexity: O(n)
Space Complexity: O(n)

"""



def containsDuplicate(nums):
        return len(set(nums)) != len(nums) 
