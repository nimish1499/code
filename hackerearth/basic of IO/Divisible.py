def solve(A):
    first = [A[i][0] for i in range(N//2)]
    second = [A[i][-1] for i in range(N//2, N)]
    st = ''.join(first)+''.join(second)
    if int(st) % 11 == 0:
        return 'OUI'
    else:
        return 'NON'


N = int(input())
A = input().split()[:N]

out_ = solve(A)
print(out_)
