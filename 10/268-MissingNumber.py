# O(n)
from typing import List
def missingNumber(nums: List[int]) -> int:
    return list(set(nums) ^ set(range(0, len(nums)+1)))[0]

def main():
    array = [int(n) for n in input().split()]
    
    result = missingNumber(array)
    print(result)
    
    
if __name__ == '__main__':
    main()