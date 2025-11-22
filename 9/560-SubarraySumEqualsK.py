# O(n)
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    result = 0
    counter = {0: 1}
    s = 0
    for n in nums:
        s += n
        result += counter.get(s-k, 0)
        counter[s] = counter.get(s, 0) + 1
    return result

def main():
    array = [int(n) for n in input().split()]
    k = int(input())
    
    result = subarraySum(array, k)
    print(result)
    
    
if __name__ == '__main__':
    main()