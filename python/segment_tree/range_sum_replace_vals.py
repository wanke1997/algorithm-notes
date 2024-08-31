from typing import List


class RangeSumReplaceVals:
    """
    A segment tree that replaces the range with a specific value.

    e.g. supppse we have an array: [1, 2, 3, 4, 5], if we call instance.update(1, 3, 100),
    the array will become: [1, 100, 100, 100, 5]
    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n + 1)
        self.tags = [None] * (4 * self.n + 1)
        self._build(nums, 0, self.n - 1, 1)

    def _build(self, nums: List[int], start: int, end: int, idx: int) -> None:
        if start == end:
            self.tree[idx] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(nums, start, mid, 2 * idx)
            self._build(nums, mid + 1, end, 2 * idx + 1)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def _pushdown(self, idx: int, s: int, e: int, mid: int) -> None:
        """
        Push down operation. When the current node's lazy tag is not None, update
        its children nodes' range sum and their lazy tags, then reset the current node's lazy tag.

        Note that this class is to update the range value with a specific value, we just calculate
        the range sum using multiplication, and replace the lazy tags with the input value.
        """
        if self.tags[idx] is not None:
            self.tree[2 * idx] = self.tags[idx] * (mid - s + 1)
            self.tree[2 * idx + 1] = self.tags[idx] * (e - mid)
            self.tags[2 * idx] = self.tags[2 * idx + 1] = self.tags[idx]
            self.tags[idx] = None

    def _update_helper(self, target_s: int, target_e: int, s: int, e: int, idx: int, val: int) -> None:
        if s >= target_s and e <= target_e:
            """
            base case: when the current range is a sub range of the target range, just
            update the range sum AND set the lazy tags for its subtree
            """
            self.tree[idx] = val * (e - s + 1)
            self.tags[idx] = val
        elif e < target_s or s > target_e:
            return
        else:
            mid = (s + e) // 2
            # push down lazy tags for every range whose lazy tags are not None
            self._pushdown(idx, s, e, mid)
            self._update_helper(target_s, target_e, s, mid, 2 * idx, val)
            self._update_helper(target_s, target_e, mid + 1, e, 2 * idx + 1, val)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def _query(self, target_s: int, target_e: int, s: int, e: int, idx: int) -> int:
        # base case 1: when the current range is a sub range of target range, return current range sum
        if s >= target_s and e <= target_e:
            return self.tree[idx]
        # base case 2: when the current range doesn't overlap with target range, return 0
        elif e < target_s or s > target_e:
            return 0
        else:
            mid = (s + e) // 2
            # push down lazy tags for every range whose lazy tags are not None
            self._pushdown(idx, s, e, mid)
            # find the range sum of left half range and right half range
            left = self._query(target_s, target_e, s, mid, 2 * idx)
            right = self._query(target_s, target_e, mid + 1, e, 2 * idx + 1)
            # sum them up
            return left + right

    def update(self, left: int, right: int, val: int) -> None:
        self._update_helper(left, right, 0, self.n - 1, 1, val)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(left, right, 0, self.n - 1, 1)


if __name__ == "__main__":
    arr = [10, 11, 12, 13, 14]
    instance = RangeSumReplaceVals(arr)
    # 1. query [2, 4] -> 39
    res = instance.sumRange(2, 4)
    print("result [2, 4]: {}".format(res))
    # 2, update elements [1, 3] with 100
    instance.update(1, 3, 100)
    # 3. query [2, 4] -> 214
    res = instance.sumRange(2, 4)
    print("result [2, 4]: {}".format(res))
