# 
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums)-1
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            total = sum(triplet)
            if total == 0:
                result.append(triplet)
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while r > l and nums[r] == nums[r+1]:
                    r -= 1
            elif total < 0:
                l += 1
            elif total > 0:
                r -= 1
    return result

def main():
    array = [int(n) for n in input().split()]
    
    result = threeSum(array)
    print(result)
    
    
if __name__ == '__main__':
    main()