from typing import List

"""
Difference array is used to modify a range of numbers with O(1) time complexity. 
For difference array, it records the difference between nums[i] and nums[i-1]. 
That is, difference_array[i] = nums[i]-nums[i-1]. 

When we need to modify (plus or minus) the array, say that the interval starting at i
and ending at j (inclusive), we just need to modify the difference_array[i] and difference_array[j+1]. 
For example, if we need to add `offset` for every element between i and j index, then we need to
difference_array[i] += offset and difference_array[j+1] -= offset, and we have done!

Attention: we need to reverse modification for difference_array[j+1], not for difference_array[j]. We 
want to revert the elements starting at j+1, not j. 
"""


class DifferenceArray:
    def __init__(self, array: List[int]) -> None:
        self.array = array
        self.difference_array = [0] * len(array)
        self.difference_array[0] = array[0]
        for i in range(1, len(array)):
            self.difference_array[i] = self.array[i] - self.array[i - 1]

    def modify(self, start: int, end: int, val: int) -> None:
        self.difference_array[start] += val
        if end + 1 < len(self.difference_array):
            self.difference_array[end + 1] -= val

    def get_array(self) -> List[int]:
        res = [0] * len(self.difference_array)
        res[0] = self.difference_array[0]
        for i in range(1, len(self.difference_array)):
            res[i] = res[i - 1] + self.difference_array[i]
        self.array = res
        return res[:]


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    instance = DifferenceArray(array=array)
    instance.modify(1, 4, 10)
    res = instance.get_array()
    print(res)
    instance.modify(1, 4, -10)
    res = instance.get_array()
    print(res)
