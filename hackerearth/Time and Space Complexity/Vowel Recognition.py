T = input()
vowel = set('aeiouAEIOU')
for i in range(int(T)):
    S = input()
    Sum = 0
    for j in range(len(S)):

        if S[j] in vowel:
            Sum = Sum+((j+1)*(len(S)-j))
    print(Sum)
