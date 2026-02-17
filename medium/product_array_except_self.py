"""
https://leetcode.com/problems/product-of-array-except-self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Time Complexity: O(n)
Space Complexity: O(1)

Calculate Prefix Product and Suffix Product. Multiply left prefix and right suffix of i element.

Approach: Two pass - left products then right products

"""





def pref_product(arr):
    n = len(arr)
    pre_arr = [0]*n
    pre_arr[0] = arr[0]

    for i in range(1,n):
        pre_arr[i] = arr[i] * pre_arr[i-1]
    return pre_arr 



def suf_product(arr):
    n = len(arr)
    suf_arr = [0]*n
    suf_arr[-1] = arr[-1]

    for i in range(n-2,-1,-1):
        suf_arr[i] = arr[i] *suf_arr[i+1]
    return suf_arr 


def productExceptSelf1(nums):
        pre = pref_product(nums)
        suf = suf_product(nums)
        nums[0] = suf[1]
        nums[-1] = pre[-2]

        for i in range(1,len(nums)-1):
            nums[i] = pre[i-1]*suf[i+1]
        
        return nums


def productExceptSelf2(nums):
    n = len(nums)
    result = [1] * n

    # First pass: calculate left products
    # result[i] = product of all elements to the left of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Second pass: multiply by right products
    # result[i] *= product of all elements to the right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result
