# Accepted: 01/13/2026
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Find bounds
        y_bottom = float(min(square[1] for square in squares))
        y_top = float(max(square[1] + square[2] for square in squares))

        total_area = sum(square[2] * square[2] for square in squares)
        target_area = total_area / 2.0

        # Binary search for the horizontal line position
        # Use iteration limit instead of absolute precision
        for _ in range(100):  # log2(10^9) ≈ 30, so 100 is more than enough
            if y_top - y_bottom < 1e-10:  # Add this check back for simple cases
                break

            y_mid = (y_bottom + y_top) / 2.0
            area_below = 0.0

            for square in squares:
                x, y, l = square

                if y + l <= y_mid:
                    # Square completely below the line
                    area_below += l * l
                elif y < y_mid < y + l:
                    # Square intersected by the line
                    # Rectangle below: width=l, height=(y_mid - y)
                    area_below += l * (y_mid - y)
                # If y >= y_mid, square is completely above, contributes 0

            if area_below < target_area:
                y_bottom = y_mid
            else:
                y_top = y_mid

        return round((y_bottom + y_top) / 2.0, 5)


class BestSolution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        diff = defaultdict(int)
        for _, y, l in squares:
            total_area += l * l
            diff[y] += l
            diff[y + l] -= l
            print(diff)

        area = 0
        s = 0
        for y, y2 in pairwise(sorted(diff)):
            s += diff[y]
            area += s * (y2 - y)
            if area * 2 >= total_area:
                return y2 - (area * 2 - total_area) / (s * 2)
        return -1


if __name__ == "__main__":
    # solution = Solution()
    solution = BestSolution()
    result = solution.separateSquares([[0, 0, 1], [2, 2, 1]])
    print(f"Result: {result}")

    result2 = solution.separateSquares([[0, 0, 2], [1, 1, 1]])
    print(f"Result2: {result2}")

    # result3 = solution.separateSquares(
    #     [
    #         [639, 968, 150],
    #         [724, 925, 23],
    #         [438, 868, 55],
    #         [354, 712, 92],
    #         [923, 973, 92],
    #         [810, 920, 45],
    #         [637, 898, 283],
    #         [149, 961, 263],
    #         [111, 727, 17],
    #         [471, 590, 162],
    #     ]
    # )
    # print(f"Result3: {result3}")

    # result4 = solution.separateSquares(
    #     [
    #         [522261215, 954313664, 225462],
    #         [628661372, 718610752, 10667],
    #         [619734768, 941310679, 44788],
    #         [352367502, 656774918, 289036],
    #         [860247066, 905800565, 100123],
    #         [817623994, 962847576, 71460],
    #         [691552058, 782740602, 36271],
    #         [911356, 152015365, 513881],
    #         [462847044, 859151855, 233567],
    #         [672324240, 954509294, 685569],
    #     ]
    # )
    # print(f"Result4: {result4}")
