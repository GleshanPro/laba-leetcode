# O(n+m)
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
                 
def main():
    s = input()
    t = input()
    
    result = isAnagram(s, t)
    print(result)
    
    
if __name__ == '__main__':
    main()