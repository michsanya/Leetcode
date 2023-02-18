from unittest import TestCase
from Running_Sum_of_1d_Array import Solution


class TestSolution(TestCase):
    def test_running_sum_1(self):
        nums = [1, 2, 3, 4]
        ans = Solution().runningSum(nums)
        output = [1, 3, 6, 10]
        self.assertEqual(ans, output)

    def test_running_sum_2(self):
        nums = [3, 1, 2, 10, 1]
        ans = Solution().runningSum(nums)
        output = [3, 4, 6, 16, 17]
        self.assertEqual(ans, output)

    def test_running_sum_3(self):
        nums = [1, 1, 1, 1, 1]
        ans = Solution().runningSum(nums)
        output = [1, 2, 3, 4, 5]
        self.assertEqual(ans, output)
