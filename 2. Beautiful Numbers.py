t = input()
for case in range(int(t)):
    n = int(input())
    print(n)
    max = n-1
    max_one = 2
    for base in range(2, n//2):
        if base>=n or n%base==0:
            continue
        x = n;
        list = []
        check = 1
        # print('base ', base)
        while(x>base):
            rem = x%base
            # print('rem ', rem)
            if rem != 1:
                check = 0
                break
            list.append(rem)
            x = x//base
            # print('quo ', x)

        if check == 0 or x!=1:
            continue;
        else:
            list.append(1)
            print(list)
            if len(list) > max_one:
                max = base
                max_one = len(list)
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    f.write('Case #{}: {}\n'.format(case + 1, max))
    f.close()
    print('Case #{}: {}'.format(case + 1, max))


