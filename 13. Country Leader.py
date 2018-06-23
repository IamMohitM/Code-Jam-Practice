#Kickstart Practice Round 2017

f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
for case in range(int(input())):
    n = int(input())
    names = []
    max = float('-inf')
    leader = ''
    count = 0
    for idx in range(n):
        name = input()
        length = len(set(name.replace(' ', '')))
        if max < length:
            count = 1
            max = length
            leader = name
            names = [name]
        elif max == length:
            count +=1
            names.append(name)
    if count>1:
        for name in names:
            if leader > name:
                leader = name
    print(leader)
    f.write('Case #{}: {}\n'.format(case + 1, leader))

f.close()