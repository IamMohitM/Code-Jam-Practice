import sys


def manh_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def min_delivery(x, y, ones):
    return min([manh_dist(x, y, x1, y1) for (x1, y1) in ones])


for case in range(1, int(input()) + 1):
    rows, columns = map(int, input().split())
    grid = [list(map(int, list(input()))) for row in range(rows)]

    if all([all(x) for x in grid]):
        print('Case #{}: {}'.format(case, 0))
        continue

    ones = [(x, y) for x in range(rows) for y in range(columns) if grid[x][y] == 1]
    dist = []
    for row in range(rows):
        for column in range(columns):
            if (row, column) not in ones:
                new_one = ones[:]
                new_one.append((row, column))

                min_del = [min_delivery(r1, c2, new_one) for r1 in range(rows)
                           for c2 in range(columns) if (r1, c2) != (row, column)]

                dist.append(max(min_del))

    print('Case #{}: {}'.format(case, min(dist)))

    sys.stdout.flush()
