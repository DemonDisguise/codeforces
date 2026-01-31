import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = []
    for _ in range(8):
        row = input().strip()
        for ch in row:
            if ch != '.':
                word.append(ch)
    print("".join(word))
