# Kickstart Round G 2017
facts = {1:1}
def factorial(n):
    if n in facts.keys():
        return facts[n]
    else:
        facts[n] = n * factorial(n-1)
        return facts[n]

for case in range(int(input())):
    a, n, p = input().split()
    a = int(a)
    n = int(n)
    p = int(p)
    # while (n > 1):
    #     fact = fact * n
    #     n -= 1
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    if a%p==0:
        f.write('Case #{}: {}\n'.format(case + 1, 0))
    else:
        rem = (a**factorial(n))%p
        f.write('Case #{}: {}\n'.format(case + 1, rem))

    f.close()

