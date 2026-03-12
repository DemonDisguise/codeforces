for _ in range(int(input())):
    n = int(input())
    s = input()

    f_b, l_b = -1, -1
    for i in range(n):
        if s[i] == 'B':
            if f_b == -1:
                f_b = i
            l_b = i
    print(l_b - f_b + 1)
