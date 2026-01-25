n = int(input())
x = list(map(int, input().split()))

print("HARD" if x.count(1) else "EASY")
