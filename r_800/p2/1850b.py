def solve():
    for _ in range(int(input())):
        n = int(input())
        res = 0
        cnt = -1
        for i in range(1, n + 1):
            a, b = map(int, input().split())
            if a <= 10 and b > cnt:
                res = i
                cnt = b
        print(res)

if __name__ == "__main__":
    solve()
