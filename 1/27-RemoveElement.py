# O(n)
from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            temp = nums[-1]
            nums[-1] = val
            nums[i] = temp
            nums.pop()
        else:
            i += 1
    return len(nums)
                
                
def main():
    array = [int(n) for n in input().split()]
    val = int(input())
    
    result = removeElement(array, val)
    print(result)
    
    
if __name__ == '__main__':
    main()