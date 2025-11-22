# O(n + m) 
from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
                 
def main():
    array1 = [int(n) for n in input().split()]
    array2 = [int(n) for n in input().split()]
    
    result = intersection(array1, array2)
    print(result)
    
    
if __name__ == '__main__':
    main()