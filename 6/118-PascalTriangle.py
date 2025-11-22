# O(n^2)
from typing import List
def generate(numRows: int) -> List[List[int]]: 
    result = [[1]]
    while numRows > 1:
        result.append([1] + [result[-1][i] + result[-1][i+1] for i in range(len(result[-1]) - 1)] + [1])
        numRows -= 1
    
    return result     
                
def main():
    n = int(input())
    
    result = generate(n)
    print(result)
    
    
if __name__ == '__main__':
    main()