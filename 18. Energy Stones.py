for case in range(int(input())):
    n = int(input())
    seconds, energy, loss = zip(*[map(int, input().split()) for i in range(n)])

    time_taken = seconds[0]
    total_energy = energy[0]

    for ind in range(1, n):
        l = loss[ind] * seconds[ind-1]
        e = energy[ind] - l
        if e > 0:
            total_energy += e
        time_taken+=seconds[ind]

    print('Case #{}: {}'.format(case+1, total_energy))
