import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    s = max(ord(i) for i in input().strip())
    print(s - 96)   
