# Kickstart Round E 2017

for case in range(int(input())):
    target = input()
    count = 0
    clip = ''
    start_index = 0
    end_index = 1
    length = 1
    clipboard = ''
    # mid_index = end_index
    while (clip != target):
        mid_index = start_index + length
        if target[start_index:start_index + length] not in clip:
            if length > 1:
                clip += target[start_index:start_index + length - 1]
                if clipboard == target[start_index:start_index + length - 1] or len(clipboard) == 0:
                    count +=1
                else:
                    count+=2
                if len(target[start_index:start_index + length - 1])>1:
                    clipboard = target[start_index:start_index + length - 1]
                start_index = start_index + length - 1
            else:
                clip += target[start_index:start_index + length]
                count+=1
                if len(target[start_index:start_index + length])>1:
                    clipboard = target[start_index:start_index + length]
                # clipboard = target[start_index:start_index + length ]
                start_index = start_index + length
            # clip+=target[start_index:mid_index]
            length = 1
            print('clip', clip)
            print('cliboard', clipboard)
            print('count is ', count)
            # count += 1
        else:
            if length + 1 == len(target):
                clip += target[start_index:start_index + length - 1]
                if clipboard == target[start_index:start_index + length - 1] or len(clipboard) == 0:
                    count += 1
                else:
                    count += 2
                # print(clip)
            else:
                length += 1
    # f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')
    # f.write('Case #{}: {}\n'.format(case + 1, count))
    # f.close()
    print('Final Count', count)
