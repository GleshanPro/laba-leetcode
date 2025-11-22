# O(m + n)
from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        i, j = 0, 0
        while True:
            # Check if one of array's empty - need to add all the elements of the other array to result.
            if m == 0:
                for a in range(j, len(nums2)): 
                    result.append(nums2[a])
                break
            if n == 0:                    # m - count of remaining elements of nums1
                for a in range(i, i + m): # m - important! nums1 also consists of zeros to have m + n length, don't add them.
                    result.append(nums1[a])
                break

            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                m -= 1
                i += 1
            else:
                result.append(nums2[j])
                n -= 1
                j += 1
        nums1[:] = result
        return nums1
                 
def main():
    array1 = [int(n) for n in input().split()]
    m = int(input())
    array2 = [int(n) for n in input().split()]
    n = int(input())
    
    result = merge(array1, m, array2, n)
    # result = merge([1,2,4,5,6,0], 5, [3], 1)
    print(result)
    
    
if __name__ == '__main__':
    main()