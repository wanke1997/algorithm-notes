from typing import List, Optional


class SegmentTree:
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
        if self.tags[idx] != 0:
            self.tree[2 * idx] += self.tags[idx] * (mid - cur_s + 1)
            self.tree[2 * idx + 1] += self.tags[idx] * (cur_e - mid)
            self.tags[2 * idx] += self.tags[idx]
            self.tags[2 * idx + 1] += self.tags[idx]
            self.tags[idx] = 0

    def _query_helper(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int) -> int:
        if cur_s >= target_s and cur_e <= target_e:
            return self.tree[idx]
        elif cur_s > target_e or cur_e < target_s:
            return 0
        else:
            mid = (cur_s + cur_e) // 2
            self._pushdown(idx, cur_s, cur_e, mid)
            left = self._query_helper(target_s, target_e, cur_s, mid, 2 * idx)
            right = self._query_helper(target_s, target_e, mid + 1, cur_e, 2 * idx + 1)
            return left + right

    def update(self, target_s: int, target_e: int, cur_s: int, cur_e: int, idx: int, val: int) -> None:
        if cur_s >= target_s and cur_e <= target_e:
            self.tree[idx] += (cur_e - cur_s + 1) * val
            self.tags[idx] += val
        elif cur_s > target_e or cur_e < target_s:
            return
        else:
            mid = (cur_s + cur_e) // 2
            self._pushdown(idx, cur_s, cur_e, mid)
            self.update(target_s, target_e, cur_s, mid, 2 * idx, val)
            self.update(target_s, target_e, mid + 1, cur_e, 2 * idx + 1, val)
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, start: int, end: int) -> Optional[int]:
        if start < 0 or end >= self.n:
            return None
        else:
            return self._query_helper(start, end, 0, self.n - 1, 1)


if __name__ == "__main__":
    arr = [10, 11, 12, 13, 14]
    instance = SegmentTree(arr)
    # 1. query [2, 4] -> 39
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
    # 2, update [1, 3] to add each element by 3
    instance.update(1, 3, 0, instance.n - 1, 1, 3)
    # 3. query [2, 4] -> 45
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
