from typing import List

"""
There are six versions of segment tree. 
1> Range sum and add values
2> Range sum and replace values
3> Range sum and keep previous values
4> Max/Min and add values
5> Max/Min and replace values
6> Max/Min and keep previous values

For each operations, please refer to the following comments
"""


class Summary:
    def _build(self, nums: List[int], start: int, end: int, idx: int) -> None:
        if start == end:
            self.tree[idx] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(nums, start, mid, 2 * idx)
            self._build(nums, mid + 1, end, 2 * idx + 1)
            """
            Two versions for _build operations
            1> range_sum tree, use "+"
            2> max/min tree, use max() or min()
            """
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def _pushdown(self, idx: int, s: int, mid: int, e: int) -> None:
        if self.lazy[idx]:
            """
            Note: for push down, the operations of tree and lazy tags will be the same. 
            
            Six versions for _pushdown operations
            1> range_sum tree and add values, use "+=" for both tree and children's lazy tags
            2> range_sum tree and replace values, update both children's lazy tags and tree using current values
            3> range_sum tree and keep previous values, update both tree and children's lazy tags using max() or min()
            4> max/min tree and add values, use "+=" for both tree and children's lazy tags
            5> max/min tree and replace values, update both children's lazy tags and tree using current values
            6> max/min tree and keep previous values, update both tree and children's lazy tags using max() or min()
            """
            self.lazy[2 * idx] = self.lazy[idx]
            self.lazy[2 * idx + 1] = self.lazy[idx]
            self.tree[2 * idx] = self.lazy[idx] * (mid - s + 1)
            self.tree[2 * idx + 1] = self.lazy[idx] * (e - mid)
            self.lazy[idx] = None

    def _query(self, t_s: int, t_e: int, s: int, e: int, idx: int) -> int:
        if s >= t_s and e <= t_e:
            return self.tree[idx]
        elif s > t_e or e < t_s:
            return 0
        else:
            mid = (s + e) // 2
            self._pushdown(idx, s, mid, e)
            left = self._query(t_s, t_e, s, mid, 2 * idx)
            right = self._query(t_s, t_e, mid + 1, e, 2 * idx + 1)
            """
            Two versions for _query operations
            1> range_sum tree, use "+" to return left and right range's sum
            2> max/min tree, use max() or min() to get the max or min values
            """
            return left + right

    def _update(self, t_s: int, t_e: int, s: int, e: int, idx: int, val: int) -> None:
        if s >= t_s and e <= t_e:
            """
            Note: for update, the operations of tree and lazy tags will be the same. 
            
            Six versions for base update operations
            1> range_sum tree and add values, use "+=" for both tree and children's lazy tags
            2> range_sum tree and replace values, update both children's lazy tags and tree using current values
            3> range_sum tree and keep previous values, update both tree and children's lazy tags using max() or min()
            4> max/min tree and add values, use "+=" for both tree and children's lazy tags
            5> max/min tree and replace values, update both children's lazy tags and tree using current values
            6> max/min tree and keep previous values, update both tree and children's lazy tags using max() or min()
            """
            self.tree[idx] = val * (e - s + 1)
            self.lazy[idx] = val
        elif s > t_e or e < t_s:
            return
        else:
            mid = (s + e) // 2
            self._pushdown(idx, s, mid, e)
            self._update(t_s, t_e, s, mid, 2 * idx, val)
            self._update(t_s, t_e, mid + 1, e, 2 * idx + 1, val)
            """
            Two versions for normal update operations
            1> range_sum tree, use "+" to return left and right range's sum
            2> max/min tree, use max() or min() to get the max or min values
            """
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.lazy = [None] * (self.n * 4)
        self._build(nums, 0, self.n - 1, 1)

    def update(self, index: int, val: int) -> None:
        self._update(index, index, 0, self.n - 1, 1, val)

    def sumRange(self, left: int, right: int) -> int:
        res = self._query(left, right, 0, self.n - 1, 1)
        return res
