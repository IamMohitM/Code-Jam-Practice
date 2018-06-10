#Kickstart Round B 2017
t = int(input())
for case in range(t):
    N = int(input())
    l =list(map(int, input().split()))
    total = 0
    for i in range(N):
        print('l[i] = ', l[i])
        for size in range(2, N-i+1):
            print('size = ', size)
            for j in range(i+1, N):
                for s in range(1, size - j):
                    total += l[j+s] - l[i]
               # total += l[size + j - 2] - l[i]

    print(total % (10 ** 9 + 7))
    # f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    # f.write('Case #{}: {}\n'.format(case + 1, total%(10**9+7)))
    # f.close


















    # for ind in range(2, N+1):
    #     print('working')
    #     total += sum(max(comb) - min(comb) for comb in combinations(l, ind))
    # print(total%(10**9+7))
    # f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    # f.write('Case #{}: {}\n'.format(case + 1, total%(10**9+7)))
    # f.close