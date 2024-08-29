from typing import List, Optional

class SegmentTreeBasic:
    def __init__(self, arr: List[int]) -> None:
        self.n = len(arr)
        self.segment_tree = [0]*(4*self.n)
        self._build(arr, 0, self.n-1, 1)
    
    # build a segment tree, the space should be 4*n
    # note that n is the length of the array imported
    def _build(self, arr: List[int], start: int, end: int, idx: int) -> None:
        if start == end:
            self.segment_tree[idx] = arr[start]
            return arr[start]
        else:
            mid = (start+end)//2
            self._build(arr, start, mid, 2*idx)
            self._build(arr, mid+1, end, 2*idx+1)
            self.segment_tree[idx] = self.segment_tree[idx*2] + self.segment_tree[idx*2+1]
        
    def query(self, start: int, end: int) -> Optional[int]:
        if start < 0 or end >= self.n:
            return None
        else:
            return self._helper(start, end, 0, self.n-1, 1)
    
    def _helper(self, target_start: int, target_end: int, cur_start: int, cur_end: int, idx: int) -> int:
        # base case 1: when current interval doesn't overlap with target interval, just return 0
        if cur_end < target_start or cur_start > target_end:
            return 0
        # base case 2: when current interval is a sub interval of the query interval, 
        # just return the interval sum of the current interval
        if target_start <= cur_start and target_end >= cur_end:
            return self.segment_tree[idx]
        # general case: partially overlap, divide the interval into two parts and do recursive calculations
        else:
            mid = (cur_start+cur_end)//2
            left = self._helper(target_start, target_end, cur_start, mid, 2*idx)
            right = self._helper(target_start, target_end, mid+1, cur_end, 2*idx+1)
            return left+right
        

if __name__ == "__main__":
    arr = [10,11,12,13,14]
    instance = SegmentTreeBasic(arr)
    print(instance.segment_tree)
    # 1. query: [0, 4]
    res = instance.query(0, 4)
    print("result [0, 4]: {}".format(res))
    # 2. query: [2, 4]
    res = instance.query(2, 4)
    print("result [2, 4]: {}".format(res))
    # 3. query: [1, 3]
    res = instance.query(1, 3)
    print("result [1, 3]: {}".format(res))
    # 4. query: [0, 5], out of boundary
    res = instance.query(0, 5)
    print("result [0, 5]: {}".format(res))