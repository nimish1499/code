t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    sum1=sum(a)
    m=n%sum1
    if(m==0):
        m=sum1
    for j in range(7):
        m=m-a[j]
        if(m<=0):
            if(j==0):
                print ('MONDAY')
            elif(j==1):
                print ('TUESDAY')
            elif (j==2):
                print ('WEDNESDAY')
            elif (j==3):
                print ('THURSDAY')
            elif (j==4):
                print ('FRIDAY')
            elif (j==5):
                print ('SATURDAY')
            else:
                print ('SUNDAY')
            break
