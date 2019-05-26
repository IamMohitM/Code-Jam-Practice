import operator

for case in range(1, int(input()) + 1):
    n, r, c, row, col = map(int, input().split())
    instructions = input()

    passed_dict = {(row, col): True}
    straight = False

    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1),
                  'W': (0, -1)}

    pos = (row, col)
    count = 0
    next_pos = (0, 0)
    last_instruction = None
    while count < n:
        if straight:
            next_pos = tuple(map(operator.add, next_pos, directions[last_instruction]))
        else:
            instruct = instructions[count]
            next_pos = tuple(map(operator.add, pos, directions[instruct]))
        try:
            if passed_dict[next_pos] and not straight:
                straight = True
                last_instruction = instruct
        except KeyError:
            pos = next_pos
            passed_dict[next_pos] = True
            straight = False
            count += 1

    print('Case #{}: {} {}'.format(case, next_pos[0], next_pos[1]))
