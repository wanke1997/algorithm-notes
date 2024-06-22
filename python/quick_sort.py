from typing import List, Dict, Optional
import random

class quickSort:
    def __init__(self, array: Optional[List[int]] = None) -> None:
        self.array = array
    
    def _partition(self, start: int, end: int) -> int:
        write = read = start+1
        while read <= end:
            # write all elements whose value is smaller or equal to pilot
            if self.array[read] <= self.array[start]:
                self.array[write], self.array[read] = self.array[read], self.array[write]
                write += 1
                read += 1
            else:
                read += 1
        self.array[start], self.array[write-1] = self.array[write-1], self.array[start]
        return write-1
    
    def sort(self, start: int, end: int) -> None:
        if start >= end:
            return
        else:
            pilot = self._partition(start, end)
            self.sort(start, pilot-1)
            self.sort(pilot+1, end)
            return


class testSuite:
    def generate_test_cases(self) -> Dict[str, List[int]]:
        test_cases = {
            "empty_list": [],
            "single_element": [42],
            "already_sorted": list(range(1, 11)),
            "reverse_sorted": list(range(10, 0, -1)),
            "all_elements_same": [7] * 10,
            "random_list": random.sample(range(1, 100), 10),
            "large_list": random.sample(range(1, 100000), 1000)
        }
        return test_cases

    def is_sorted(self, arr) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    # Function to run the sorting algorithm on each test case
    def run_tests(self, instance: quickSort) -> None:
        test_cases = self.generate_test_cases()
        
        for name, case in test_cases.items():
            print(f"Testing {name}...")
            array = case.copy()
            instance.array = array
            instance.sort(0, len(instance.array)-1)
            sorted_case = instance.array
            print("result: {}".format(self.is_sorted(sorted_case)))
            print("="*40)
                

if __name__ == "__main__":
    # array = [13,19,9,5,12,8,7,4,21,2,6,11]
    # instance = quickSort(array=array)
    # instance.sort(0, len(instance.array)-1)
    # print(instance.array)
    test = testSuite()
    instance = quickSort()
    test.run_tests(instance)