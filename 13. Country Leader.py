#Kickstart Practice Round 2017

for case in range(int(input())):
    n = int(input())
    names = []
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    for idx in range(n):
        names.append(input())
    max = float('-inf')
    leader = ''
    indexes = []
    for i, name in enumerate(names):
        length = len(set(name.replace(' ','')))
        if max < length:
            indexes = [i]
            max = length
        elif max == length:
            indexes.append(i)
            max = length
    leader = names[indexes[0]]
    if len(indexes)>1:
        for idx in indexes:
            if leader > names[idx]:
                leader = names[idx]
    print(leader)
    f.write('Case #{}: {}\n'.format(case + 1, leader))

f.close()