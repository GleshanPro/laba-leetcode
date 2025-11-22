# O(n)
from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result
                 
def main():
    array = [int(n) for n in input().split()]
    
    result = singleNumber(array)
    print(result)
    
    
if __name__ == '__main__':
    main()