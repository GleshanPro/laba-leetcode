from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    indices = {}
    for i, num in enumerate(nums):
        if num in indices:
            if abs(i - indices[num]) <= k:
                return True
        indices[num] = i
    return False
                 
def main():
    array = [int(n) for n in input().split()]
    k = int(input())
    
    result = containsNearbyDuplicate(array, k)
    print(result)
    
    
if __name__ == '__main__':
    main()