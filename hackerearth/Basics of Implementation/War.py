t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = max(a)
    d = max(b)
    if c > d:
        print("Bob")
    if c < d:
        print("Alice")        
    if c == d:
        print("Tie")        
