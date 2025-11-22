# O(n)
from typing import List
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    existing = set(nums)
    missing = (i for i in range(1, len(nums)+1) if i not in existing)
            
    return list(missing)
                
                
def main():
    array = [int(n) for n in input().split()]
    
    result = findDisappearedNumbers(array)
    print(result)
    
    
if __name__ == '__main__':
    main()