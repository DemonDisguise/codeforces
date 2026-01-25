import math

n, m = map(int, input().split())

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_next_prime(n):
    i = n + 1
    while True:
        if is_prime(i):
            return i
        else:
            i += 1

print("YES" if get_next_prime(n) == m else "NO")
