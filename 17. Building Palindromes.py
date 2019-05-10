letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for case in range(int(input())):
    n, Q = map(int, input().split())
    blocks = input()
    count = 0
    for q in range(Q):
        l, r = map(int, input().split())
        if l==r:
            count+=1
            continue
        block = blocks[l - 1:r]
        counter = [block.count(val) % 2 == 0 for val in letters]
        if all(counter) or len(counter) - sum(counter) == 1:
            count += 1

    print('Case #{}: {}'.format(case + 1, count))
