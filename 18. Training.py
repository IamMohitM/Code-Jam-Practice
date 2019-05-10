import sys

for case in range(1, int(input()) + 1):
    n, p = map(int, input().split())
    skills = map(int, input().split())

    skills = sorted(skills)
    length = len(skills)
    minimum = float('inf')
    for index in range(p - 1, length, 1):
        hours = 0
        for win in range((index - p) + 1, index, 1):
            hours += skills[index] - skills[win]
            # if hours>=minimum:
            #     break
        if minimum > hours:
            minimum = hours

    print('Case #{}: {}'.format(case, minimum))
    sys.stdout.flush()