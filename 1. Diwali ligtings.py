#Kickstart Practice Round 2 2017
from math import ceil
t= input()
for case in range(int(t)):
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    patt = input()
    patt_len = len(patt)
    i, j = input().split()
    i = int(i)
    j = int(j)
    count_b = patt.count('B')
    if count_b == 0:
        f.write('Case #{}: {}\n'.format(case + 1, 0))
        f.close()
        continue
    c1 = patt.count('B', (i%patt_len) -1, patt_len)
    c2 = patt.count('B', 0, (j%patt_len))
    c3 = count_b * ((j//patt_len) - (ceil(i/patt_len)))
    f.write('Case #{}: {}\n'.format(case + 1, c1 + c2 + c3))
    f.close()