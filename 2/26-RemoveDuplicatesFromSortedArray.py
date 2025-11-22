# O(n)
from typing import List
def removeDuplicates(nums: List[int]) -> int:
    result = []
    prev = -101     # -100 <= nums[i] <= ... and array is sorted in non-decreasing order
    i = 0
    while i < len(nums):
        if nums[i] != prev:
            result.append(nums[i])
            prev = nums[i]
        i += 1
        
    nums[:] = result
    return nums
                 
def main():
    array = [int(n) for n in input().split()]
    
    result = removeDuplicates(array)
    print(result)
    
    
if __name__ == '__main__':
    main()