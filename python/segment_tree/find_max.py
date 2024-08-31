from typing import List, Optional


class SegmentTreeFindMax:
    """
    A segment tree that can find maximum value in any intervals from an array with O(logn) time complexity.
    """

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (self.n * 4)
        self.tags = [None] * (self.n * 4)
        self.INF = -(10**10)
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
            self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])

    def _pushdown(self, idx: int) -> None:
        """
        Push down operation. When the current node's lazy tag does not equal to None, update
        its children nodes' maximum values and their lazy tags, then reset the current node's lazy tag.

        Note that this class is to update maximum values with a specific value. We need to use the lazy tag
        to try to get the maximum value for children nodes, and then pass the possible maximum lazy tags to
        its children node. 
        """
        if self.tags[idx] is not None:
            self.tree[2 * idx] = max(self.tree[2 * idx], self.tags[idx])
            self.tree[2 * idx + 1] = max(self.tree[2 * idx + 1], self.tags[idx])
            if self.tags[2 * idx] is None:
                self.tags[2 * idx] = self.tags[idx]
            else:
                self.tags[2 * idx] = max(self.tags[2 * idx], self.tags[idx])
            if self.tags[2 * idx + 1] is None:
                self.tags[2 * idx + 1] = self.tags[idx]
            else:
                self.tags[2 * idx + 1] = max(self.tags[2 * idx + 1], self.tags[idx])
            self.tags[idx] = None

    def _query_helper(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int) -> int:
        # base case 1: when the current range is a sub range of target range, return current range's max value
        if cur_s >= target_s and cur_e <= target_e:
            return self.tree[idx]
        # base case 2: when the current range doesn't overlap with target range, return INF
        elif cur_s > target_e or cur_e < target_s:
            return self.INF
        else:
            mid = (cur_s + cur_e) // 2
            self._pushdown(idx)
            # find the max value of the left half range and right half range
            left = self._query_helper(target_s, target_e, cur_s, mid, 2 * idx)
            right = self._query_helper(target_s, target_e, mid + 1, cur_e, 2 * idx + 1)
            # get the max value from the left half and right half range
            return max(left, right)

    def update(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int, val: int) -> None:
        if cur_s >= target_s and cur_e <= target_e:
            """
            base case: when the current range is a sub range of the target range, just update 
            the max value in the range AND update its lazy tag with possible maximum value
            """
            self.tree[idx] = max(self.tree[idx], val)
            if self.tags[idx] is None:
                self.tags[idx] = val
            else:
                self.tags[idx] = max(self.tags[idx], val)
        elif cur_s > target_e or cur_e < target_s:
            return
        else:
            mid = (cur_s + cur_e) // 2
            # push down lazy tags for every range whose lazy tags don't equal to None
            self._pushdown(idx)
            self.update(target_s, target_e, cur_s, mid, 2 * idx, val)
            self.update(target_s, target_e, mid + 1, cur_e, 2 * idx + 1, val)
            # update the maximum values of current intervals with new values
            self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, start: int, end: int) -> Optional[int]:
        if start < 0 or end >= self.n:
            return None
        else:
            return self._query_helper(start, end, 0, self.n - 1, 1)


if __name__ == "__main__":
    arr = [10, 11, 12, 13, 14]
    instance = SegmentTreeFindMax(arr)
    # 1. query [2, 4] -> 14
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
    # 2, update [1, 3] with 100
    instance.update(1, 3, 0, instance.n - 1, 1, 100)
    # 3, update [0, 2] with 150
    instance.update(0, 2, 0, instance.n - 1, 1, 150)
    # 4. query [2, 4] -> 150
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
    # 4. query [3, 4] -> 100
    res = instance.query(3, 4)
    print("result [3, 4]: {}".format(res))
