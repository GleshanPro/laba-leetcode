# O(n * k log n), k - max word length.
from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        groups[str(sorted(word))].append(word)
    return list(groups.values())
                 
def main():
    array = [str(n) for n in input().split()]
    
    result = groupAnagrams(array)
    print(result)
    
    
if __name__ == '__main__':
    main()