mcnt = 0
ccnt = 0

for _ in range(int(input())):
    m, c = map(int, input().split())
    
    mcnt += m > c
    ccnt += c > m

print(
    "Mishka" if mcnt > ccnt else
    "Chris" if ccnt > mcnt else
    "Friendship is magic!^^"
)
    