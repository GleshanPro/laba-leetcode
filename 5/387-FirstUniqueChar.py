# O(n)
from collections import Counter
def firstUniqChar(s: str) -> int:
    freq = Counter(s)
    for i, num in enumerate(s):
        if freq[num] == 1:
            return i
    return -1
                 
def main():
    s = input()
    
    result = firstUniqChar(s)
    print(result)
    
    
if __name__ == '__main__':
    main()