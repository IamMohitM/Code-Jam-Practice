# Practice Round - Kick Start 2019

def exp_power(l, i):
    pow = sum([el * ((index + 1) ** i) for index, el in enumerate(l)])
    return pow


def get_continguous_array(l):
    total_length = len(l)
    cont_array = [l[i: i + length] for length in range(1, total_length + 1, 1)
                  for i in range(total_length - length + 1)]
    return cont_array


def generate_A(A, n, x, y, c, d, e1, e2, f, i):
    if i == n:
        return A
    else:
        xi = ((c * x) + (d * y) + e1) % f
        yi = ((d * x) + (c * y) + e2) % f
        A.append((xi + yi) % f)
        return generate_A(A, n, xi, yi, c, d, e1, e2, f, i + 1)


cases = int(input()) + 1
file = open('Output/kickstart_small.txt', 'w')
for case in range(1, cases):
    n, k, x, y, c, d, e1, e2, f = map(int, input().split())
    A = [(x + y) % f]
    print(A)
    A = generate_A(A, n, x, y, c, d, e1, e2, f, 1)
    print(A)
    # A = generate_A(n, x, y, c, d, e1, e2, f)
    power = sum([exp_power(cont, i) for i in range(1, k + 1, 1)
                 for cont in get_continguous_array(A)])
    print(power)
    # print(f'Case #{case}: {power}')
    file.write(f'Case #{case}: {power}\n')

file.close()
