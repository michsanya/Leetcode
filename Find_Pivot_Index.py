"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to
the left of the index is equal to the sum of all the numbers strictly to
the index's right.
If the index is on the left edge of the array, then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        pivot_index = -1
        index = 0
        sum_left = 0
        sum_right = sum(nums[1:])
        for index in range(len(nums)-1):
            if sum_left == sum_right:
                return index
            else:
                sum_left += nums[index]
                sum_right -= nums[index+1]
                index += 1
        return pivot_index


