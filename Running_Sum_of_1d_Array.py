from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array = []
        for i in range(len(nums)):
            sum_array.append(sum(nums[:(i + 1)]))
        return sum_array


