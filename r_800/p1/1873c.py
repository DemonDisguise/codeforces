for _ in range(int(input())):
    n = 10
    res = 0
    for i in range(10):
        s = input()
        for j in range(10):
            if s[j] == 'X':
                res += min(i, j, n - 1 - i, n - 1 - j) + 1
    print(res) 
               