n = int(input())

def beautiful_year(n):
    while len(set(str(n))) != 4:
        n += 1
    return n

print(beautiful_year(n + 1))