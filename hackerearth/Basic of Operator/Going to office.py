d = int(input())
o1, o2, o3 = map(int, input().split())
c1, c2, c3, c4 = map(int, input().split())
x = o1 + (d-o2) * o3
y = c1 + (d/c2) * c3 + d * c4
if x > y:
    print("Classic Taxi")
else:
    print("Online Taxi")        
