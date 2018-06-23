# Kickstart Round C 2017
for case in range(int(input())):
    ecr = input()
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    if len(ecr) % 2 == 1:
        f.write('Case #{}: {}\n'.format(case + 1, 'AMBIGUOUS'))
    else:
        E = [ord(char) - 65 for char in ecr]
        D = [None for char in ecr]
        D[1] = E[0]
        D[len(ecr) - 2] = E[len(ecr) - 1]
        for idx in range(3, len(ecr), 2):
            D[idx] = (E[idx - 1] - D[idx - 2]) % 26
        for idx in range(len(ecr) - 4, -1, -2):
            if D[idx] == None:
                D[idx] = (E[idx + 1] - D[idx + 2]) % 26
        dcr = ''.join([chr(id + 65) for id in D])
        f.write('Case #{}: {}\n'.format(case + 1, dcr))
        # print(dcr)

    f.close()