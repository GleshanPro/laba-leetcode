# O(m + n)
from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    freq1 = Counter(nums1)
    freq2 = Counter(nums2)
    for num in set(nums1):
        for i in range(min(freq1[num], freq2[num])):
            result.append(num)
    return result
                 
def main():
    array1 = [int(n) for n in input().split()]
    array2 = [int(n) for n in input().split()]
    
    result = intersect(array1, array2)
    print(result)
    
    
if __name__ == '__main__':
    main()