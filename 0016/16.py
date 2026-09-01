# Accepted: 08/31/2026
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans = int(1e9)
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                print("top of while: ", i, left, right, ans)
                print_pointers(nums, i, left, right)
                cmp = nums[i] + nums[left] + nums[right]
                if cmp == target:
                    return target
                if cmp < target:
                    left += 1
                else:
                    right -= 1
                if abs(cmp - target) < abs(ans - target):
                    ans = cmp

        return ans


def small_print_pointers(nums: list[int], idx: int, left: int, right: int):
    n = "["
    p = "["
    w = max(len(str(n)) for n in nums)
    if idx > 0:
        n += "..., "
        p += "..., "
    n += f"{nums[idx]:>{w}}, "
    p += f"{'^':^{w}}, "
    if left > idx + 1:
        n += "..., "
        p += "..., "
    n += f"{nums[left]:>{w}}, "
    p += f"{'^':^{w}}, "
    if right > left + 1:
        n += "..., "
        p += "..., "
    n += f"{nums[right]:>{w}}"
    p += f"{'^':^{w}}"
    if right < len(nums) - 1:
        n += ", ..."
        p += ", ..."
    n += "]"
    p += "]"
    print(n)
    print(p)


def print_pointers(nums: list[int], idx: int, left: int, right: int):
    if len(nums) > 10:
        return small_print_pointers(nums, idx, left, right)
    width = max(len(str(n)) for n in nums)

    print("[" + ", ".join(f"{n:>{width}}" for n in nums) + "]")

    print(
        "["
        + ", ".join(
            f"{'^':^{width}}" if i in (idx, left, right) else " " * width
            for i in range(len(nums))
        )
        + "]"
    )


class TestCase:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target


if __name__ == "__main__":
    s = Solution()
    from pathlib import Path

    tests: list[TestCase] = []
    test_file = Path(__file__).with_name("tests.txt")
    with test_file.open("r", encoding="utf-8") as f:
        g = f.read().splitlines()
        for i in range(1, len(g), 2):
            tests.append(TestCase(eval(g[i - 1]), int(g[i])))
    for t in tests:
        print(t.nums, "+", t.target, "=>", s.threeSumClosest(t.nums, t.target))
