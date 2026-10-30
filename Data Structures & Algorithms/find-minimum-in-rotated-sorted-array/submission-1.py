
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 搜索区间 [left, right]，答案始终在这个区间里
        left, right = 0, len(nums) - 1

        # 区间里还有至少两个元素时继续缩小
        # 用 < 而不是 <=：因为下面有 right = mid，用 <= 会死循环
        while left < right:
            # 向下取整，保证 mid < right，不会拿 right 和自己比
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # mid 比最右边还大 → mid 在“大的那段”
                # 最小值一定在 mid 右边，mid 本身不可能是答案
                left = mid + 1
            else:
                # nums[mid] < nums[right] → mid 到 right 是升序的
                # 最小值在 mid 或它左边；mid 可能就是答案，不能跳过
                right = mid

        # left == right，区间只剩一个元素，就是最小值
        return nums[left]