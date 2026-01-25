n = int(input())

def is_lucky(n):
    l = 0
    while n > 0:
        num = n % 10
        if num == 4 or num == 7:
            l += 1
        n //= 10

    if l == 0:
        return "NO"
    
    while l > 0:
        num = l % 10
        if num == 4 or num == 7:
            l //= 10
        else:
            return "NO"
    return "YES"

print(is_lucky(n))