# O(n log n)
from collections import Counter
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    return [freq[0] for freq in Counter(nums).most_common(k)]

def main():
    array = [int(n) for n in input().split()]
    k = int(input())
    
    result = topKFrequent(array, k)
    print(result)
    
    
if __name__ == '__main__':
    main()