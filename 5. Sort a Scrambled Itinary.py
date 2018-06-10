#Kickstart Practice Round 2018

for case in range(int(input())):
    N = int(input())
    dict = {}
    for flights in range(N):
        s = input()
        d = input()
        dict[s] = d
    keys = dict.keys()
    values = dict.values()
    source = [key for key in keys if key not in values][0]
    destination = [value for value in values if value not in keys][0]
    d= dict[source]
    s=''
    while(source != destination):
        s += source+'-'+dict[source]+" "
        source = dict[source]
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    f.write('Case #{}: {}\n'.format(case + 1, s))
    f.close()

#Both sets solved




