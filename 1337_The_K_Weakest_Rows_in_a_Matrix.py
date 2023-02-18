from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        result = []
        for row in mat:
            soldiers_in_row = 0
            for cell in row:
                soldiers_in_row += cell
            rows.append(soldiers_in_row)

        rang = rows[:]
        rang.sort()
        for num in rang:
            i = rows.index(num)
            result.append(i)
            rows[i] = -1

        return result[:k]


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

print(Solution().kWeakestRows(mat, 3))
