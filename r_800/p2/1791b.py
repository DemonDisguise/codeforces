move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

for _ in range(int(input())):
    input()
    s = input().strip()
    
    x = y = 0
    for c in s:
        dx, dy = move[c]
        x += dx
        y += dy
        
        if x == 1 and y == 1:
            print("YES")
            break
    else:
        print("NO")
