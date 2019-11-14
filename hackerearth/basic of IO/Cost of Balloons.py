t=int(input())
for i in range(t):
    G,P=input().split()
    n=int(input())
    first=[]
    second=[]
    for j in range(n):
        first_element,second_element = input().split()
        first.append(int(first_element))
        second.append(int(second_element))
        sum_1 = 0
        sum_2 = 0
    for k in range(n):
        sum_1 = sum_1+first[k]
        sum_2 = sum_2+second[k]
        if sum_1 >= sum_2:
            if int(G) >= int(P): 
                cost = (int(G)*sum_2+int(P)*sum_1)
            else: 
                cost = (int(G)*sum_1+int(P)*sum_2)
        else:
            if int(G) >= int(P): 
                cost = (int(P)*sum_2+int(G)*sum_1)
            else: 
                cost = (int(P)*sum_1+int(G)*sum_2)
    print(cost)
