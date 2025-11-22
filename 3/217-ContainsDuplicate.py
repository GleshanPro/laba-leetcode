# O(n)
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
                 
def main():
    array = [int(n) for n in input().split()]
    
    result = containsDuplicate(array)
    print(result)
    
    
if __name__ == '__main__':
    main()