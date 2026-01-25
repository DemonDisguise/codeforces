# Parity: Both sums even OR both sums odd
# Even number: does not change parity of a sum
# Odd number: flips parity of sum
# 

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd = sum(x % 2 for x in a)
    even = n - odd

    if odd > 0 and even >= 0:
        if odd % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")