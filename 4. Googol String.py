
T = int(input())
for case in range(T):
    k = int(input())
    s = '001'
    check = True
    while(check):
        x = s
        s += '0'
        for char in x[::-1]:
            if char == '0':
                s+='1'
            else:
                s+='0'
            if len(s)>=k:
                check = False
                break;
        # s = s+'0'+s[::-1].translate(str.maketrans('01', '10'))

    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    print('case ', case+1)
    print(s[k-1])
    f.write('Case #{}: {}\n'.format(case + 1, s[k-1]))
    f.close()

def googol(n):
    if n==2:
        return '001'
    elif n==1:
        return '0'
    elif n==0:
        return ''
    else:
        return googol(n-1) + '0' + googol(n)[::-1].translate(str.maketrans('01', '10'))