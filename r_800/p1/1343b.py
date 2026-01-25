for _ in range(int(input())):
    n = int(input())
    if n % 4 != 0:
        print("NO")
        continue
    else:
        print("YES")
        k = n // 2
        
        evens = [2 * i for i in range(1, k + 1)]
        odds = [2 * i - 1 for i in range(1, k)]
        odds.append(3 * k - 1)

        print(*(evens + odds))
        