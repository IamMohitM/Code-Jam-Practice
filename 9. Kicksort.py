#Kickstart Round F 2017
for case in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    worst_case = 'YES'
    leng = len(l)
    while(leng>2):
        pivot = leng//2
        if leng%2==0:
            val = l[pivot - 1]
            del l[pivot - 1]
        else:
            val = l[pivot]
            del l[pivot]
        if l[0]>val:
            for vals in l:
                if vals < val:
                    worst_case = 'NO'
                    break;
        else:
            for vals in l:
                if vals>val:
                    worst_case = 'NO'
                    break;
        if worst_case == 'NO':
            break;
        leng = len(l)

    print(worst_case)
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    f.write('Case #{}: {}\n'.format(case + 1, worst_case))
    f.close()