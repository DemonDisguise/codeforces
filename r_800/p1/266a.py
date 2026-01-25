n = int(input())
s = input()

def uniq_stones(n, s):
    if n == 1:
        return 0
    elif n == 2:
        return 1 if s[0] == s[1] else 0
    else:
        ops = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                ops += 1
        return ops

print(uniq_stones(n, s))