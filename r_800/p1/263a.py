import sys

m = []
for i in range(5):
    m.append(list(map(int, input().split())))

def find_1(m):
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                print(abs(2 - i) + abs(2 - j))  
                sys.exit()  

find_1(m) 