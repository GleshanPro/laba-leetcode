# O(log n) 
def isHappy(n: int) -> bool:
    seen = set()
    while n not in seen:
        seen.add(n)
        result = 0
        while n > 0:
            result += (n % 10) ** 2
            n //= 10
        if result == 1:
            return True
        n = result
    return False
                 
def main():
    n = int(input())
    
    result = isHappy(n)
    print(result)
    
    
if __name__ == '__main__':
    main()