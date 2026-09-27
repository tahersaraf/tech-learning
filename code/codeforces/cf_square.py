"""
https://codeforces.com/contest/2167/problem/A
"""

def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        sticks = input().split()
        
        if len(set(sticks)) == 1:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()