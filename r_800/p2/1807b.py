for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))

    even_sum = 0
    odd_sum = 0
    
    for i in a:
        if i & 1:
            odd_sum += i
        else:
            even_sum += i
    
    print("YES" if even_sum > odd_sum else "NO")
    