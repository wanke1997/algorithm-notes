"""
单点修改的线段树, 无需使用lazy tag

这个是区间修改带lazy tag的线段树的简化版本. 去除了lazy tag并支持单点修改

query: 大体框架和带lazy tag的线段树完全一样, 唯一的区别是移除了pushdown()函数
update: 变化在于base case, 当start==end==pos才需要修改tree[idx], 否则要么直接返回要么继续递归
"""

class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0]*(4*n)
    
    def update(self, pos: int, val: int) -> None:
        return self._update(pos, 0, self.n-1, 1, val)
    
    def _update(self, t_pos: int, start: int, end: int, idx: int, val: int) -> None:
        # a slight modification here
        if t_pos == start == end:
            self.tree[idx] += val
        elif end < t_pos or start > t_pos:
            return
        else:
            mid = (start+end) // 2
            self._update(t_pos, start, mid, 2*idx, val)
            self._update(t_pos, mid+1, end, 2*idx+1, val)
            self.tree[idx] = self.tree[2*idx] + self.tree[2*idx+1]
    
    def _query(self, t_s: int, t_e: int, start: int, end: int, idx: int) -> int:
        if t_s <= start <= end <= t_e:
            return self.tree[idx]
        elif t_s > end or start > t_e:
            return 0
        else:
            mid = (start+end) // 2
            left = self._query(t_s, t_e, start, mid, 2*idx)
            right = self._query(t_s, t_e, mid+1, end, 2*idx+1)
            return left+right
    
    def query(self, start: int, end: int) -> int:
        return self._query(start, end, 0, self.n-1, 1)