from typing import List, Optional


class SegmentTreeModifyVals:
    """
    A segment tree that adds/minuses the range with a specific value.

    e.g. supppse we have an array: [1, 2, 3, 4, 5], if we call instance.update(1, 3, 100),
    the array will become: [1, 102, 103, 104, 5]
    """

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (self.n * 4)
        self.tags = [0] * (self.n * 4)
        self._build(arr, 0, self.n - 1, 1)

    def _build(self, arr: List[int], start: int, end: int, idx: int) -> None:
        if start > end:
            return
        elif start == end:
            self.tree[idx] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, start, mid, 2 * idx)
            self._build(arr, mid + 1, end, 2 * idx + 1)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def _pushdown(self, idx: int, cur_s: int, cur_e: int, mid: int) -> None:
        """
        Push down operation. When the current node's lazy tag does not equal to zero, update
        its children nodes' range sum and their lazy tags, then reset the current node's lazy tag.

        Note that this class is to add/subtract the range value with a specific value, we just calculate
        the range sum by adding/suntracting as well, and add/subtract the lazy tags with the input value.
        """
        if self.tags[idx] != 0:
            self.tree[2 * idx] += self.tags[idx] * (mid - cur_s + 1)
            self.tree[2 * idx + 1] += self.tags[idx] * (cur_e - mid)
            self.tags[2 * idx] += self.tags[idx]
            self.tags[2 * idx + 1] += self.tags[idx]
            self.tags[idx] = 0

    def _query_helper(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int) -> int:
        # base case 1: when the current range is a sub range of target range, return current range sum
        if cur_s >= target_s and cur_e <= target_e:
            return self.tree[idx]
        # base case 2: when the current range doesn't overlap with target range, return 0
        elif cur_s > target_e or cur_e < target_s:
            return 0
        else:
            mid = (cur_s + cur_e) // 2
            self._pushdown(idx, cur_s, cur_e, mid)
            # find the range sum of left half range and right half range
            left = self._query_helper(target_s, target_e, cur_s, mid, 2 * idx)
            right = self._query_helper(target_s, target_e, mid + 1, cur_e, 2 * idx + 1)
            # sum them up
            return left + right

    def update(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int, val: int) -> None:
        if cur_s >= target_s and cur_e <= target_e:
            """
            base case: when the current range is a sub range of the target range, just
            update the range sum AND set the lazy tags for its subtree
            """
            self.tree[idx] += (cur_e - cur_s + 1) * val
            self.tags[idx] += val
        elif cur_s > target_e or cur_e < target_s:
            return
        else:
            mid = (cur_s + cur_e) // 2
            # push down lazy tags for every range whose lazy tags don't equal to zero
            self._pushdown(idx, cur_s, cur_e, mid)
            self.update(target_s, target_e, cur_s, mid, 2 * idx, val)
            self.update(target_s, target_e, mid + 1, cur_e, 2 * idx + 1, val)
            # update the value of current range sum with new values
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, start: int, end: int) -> Optional[int]:
        if start < 0 or end >= self.n:
            return None
        else:
            return self._query_helper(start, end, 0, self.n - 1, 1)


if __name__ == "__main__":
    arr = [10, 11, 12, 13, 14]
    instance = SegmentTreeModifyVals(arr)
    # 1. query [2, 4] -> 39
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
    # 2, update [1, 3] to add each element by 3
    instance.update(1, 3, 0, instance.n - 1, 1, 3)
    # 3. query [2, 4] -> 45
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
