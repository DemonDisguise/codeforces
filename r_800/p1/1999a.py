for _ in range(int(input())):
    n = int(input())
    total = 0
    while n:
        total += n % 10
        n //= 10
    print(total)