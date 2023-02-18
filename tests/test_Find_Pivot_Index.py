from unittest import TestCase

from Find_Pivot_Index import Solution


class TestSolution(TestCase):
    def test_pivot_index_1(self):
        nums = [1, 7, 3, 6, 5, 6]
        out = 3
        ans = Solution().pivotIndex(nums)
        self.assertEqual(ans, out)

    def test_pivot_index_2(self):
        nums = [1, 2, 3]
        out = -1
        ans = Solution().pivotIndex(nums)
        self.assertEqual(ans, out)

    def test_pivot_index_3(self):
        nums = [2, 1, -1]
        out = 0
        ans = Solution().pivotIndex(nums)
        self.assertEqual(ans, out)
