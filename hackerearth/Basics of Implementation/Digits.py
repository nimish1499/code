sample,numberofdig = input().split()
data = list(map(int,sample))
size = int(len(data))
n = int(numberofdig)
times = 0

for i in range(0,size,1):
    if times == n:
        break
    elif data[i] != 9:
        data[i] = 9
        times+=1

num = int(''.join(map(str,data))) 
print(num)
