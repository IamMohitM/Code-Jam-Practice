#Qualification Round 2016 Code Jam
f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
for case in range(int(input())):
    n = int(input())
    S = set()
    mul = 0
    for i in range(1, n*100):
        mul = i * n
        S=S.union(str(mul))
        if len(S) == 10:
            break
    if len(S) == 10:
        f.write('Case #{}: {}\n'.format(case + 1, mul))
    else:
        f.write('Case #{}: {}\n'.format(case + 1, 'INSOMNIA'))

f.close()
#Both Sets Correct