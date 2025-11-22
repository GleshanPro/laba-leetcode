# Time limit exceeded, but 73/83 tested passed.
# O(n * log n)
from typing import List
def longestConsecutive(nums: List[int]) -> int:
    maxLen = 0
    nums = set(nums)
    for n in nums:
        if n-1 not in nums:
            length = 1
            while n+1 in nums:
                n += 1
                length += 1
            maxLen = max(length, maxLen)
    return maxLen

def main():
    array = [int(n) for n in input().split()]
    
    result = longestConsecutive(array)
    # result = longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3])
    print(result)
    
    
if __name__ == '__main__':
    main()