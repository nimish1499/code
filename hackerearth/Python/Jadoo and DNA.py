s=input()
t=s.upper()
change={'G':'C','C':'G','T':'A','A':'U'}
g=['A','C','T','G']
for i in t:
    if i not in g:
        print("Invalid Input")
        exit()
for i in t:
    if i in change:
        print(change[i],end="")
    else:
        print('Invalid Input ')
        break
