"""
Link: https://leetcode.com/problems/container-with-most-water/description/

Problem: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
         Find two lines that together with the x-axis form a container, such that the container contains the most water.
         Return the maximum amount of water a container can store.


Approach: Two Pointers
  - Running two pointers from both ends of the container.
  - calculating the area.
  - moving the pointer with a smaller value.
  - running for the length of the heights array. ( The number of steps to cover all the elements of the height array will always be equal to the number of elements present. i.e. len(height)

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0

        for i in range(len(height)):
            area = min(height[left],height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left]> height[right]:
                right -=1
            else:
                left += 1

        return max_area



def maxArea2(height):
    """
    Time: O(n) - single pass with two pointers
    Space: O(1) - only two variables

    Pattern: Two pointers from ends, move shorter one
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        # Update maximum
        max_area = max(max_area, current_area)

        # Move the pointer with smaller height
        # (moving taller one can only decrease area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
