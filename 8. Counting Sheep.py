#Qualification Round 2016 Code Jam
for case in range(int(input())):
    n = int(input())
    S = set()
    mul = 0
    for i in range(1, n*1000):
        mul = i * n
        for dig in str(mul):
            S.add(dig)
        if len(S) == 10:
            break
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    #
    #
    if len(S) == 10:
        f.write('Case #{}: {}\n'.format(case + 1, mul))
    else:
        f.write('Case #{}: {}\n'.format(case + 1, 'INSOMNIA'))

    f.close()

#Both Sets Correct