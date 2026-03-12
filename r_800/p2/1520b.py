for _ in range(int(input())):
    n = input().strip()
    length = len(n)

    count = 9 * (length - 1)
    
    base = int("1" * length)

    first_digit = int(n[0])
    
    cn = n[0] * length

    if n >= cn:
        count += first_digit
    else:
        count += first_digit - 1
    
    print(count)
    