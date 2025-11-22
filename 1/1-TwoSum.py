# O(n)
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    complements = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [i, complements[complement]]
        complements[num] = i

    return [0, 0]
    
def main():
    array = [int(n) for n in input().split()]
    target = int(input())
    
    result = twoSum(array, target)
    print(result)
    
    
if __name__ == '__main__':
    main()