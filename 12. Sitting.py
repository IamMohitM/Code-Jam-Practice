# Round D APAC Test 2017
import numpy as np
# dict = {(1, 2): 2}
dict = {(4,3):8}
for case in range(int(input())):
    rows, columns = input().split()
    rows = int(rows)
    columns = int(columns)
    arr = np.zeros((rows, columns))
    f = open('C:/Users/mohit/Desktop/output_file.txt', 'a')

    arr[0:2, 0:2] = 1
    row_count = 0
    # print(arr[0:4, 1:3])
    # print(arr)
    c_count = 2
    keys = dict.keys()
    if (rows, columns) in keys:
        f.write('Case #{}: {}\n'.format(case + 1, dict[(rows, columns)]))
        continue
    if (columns, rows) in keys:
        f.write('Case #{}: {}\n'.format(case + 1, dict[(columns, rows)]))
        continue
    while(row_count<rows):
        while(c_count<columns):
            if row_count < 2 and c_count >=2:
                if np.sum(arr[row_count, c_count - 2:c_count]) < 2:
                    arr[row_count][c_count] = 1
                    c_count += 1
                    continue
            if c_count < 2 and row_count>=2:
                if np.sum(arr[row_count-2: row_count, c_count]) < 2:
                    arr[row_count][c_count] = 1
                    c_count += 1
                    continue
            if row_count - 2 >= 0 and c_count - 2 >=0:
                if np.sum(arr[row_count-2:row_count, c_count])<2 and np.sum(arr[row_count,c_count-2:c_count])<2:
                    arr[row_count][c_count] = 1
                    c_count +=1
                    continue

            c_count +=1
        row_count+=1
        c_count = 0
    # print(arr)
    # print(int(np.sum(np.sum(arr))))
    dict[(rows, columns)] = int(np.sum(np.sum(arr)))
    f.write('Case #{}: {}\n'.format(case + 1, dict[(rows, columns)]))
    # print(arr)

print(dict)
f.close()
# {(1, 2): 2, (4, 5): 13, (5, 1): 4, (3, 2): 4, (4, 3): 7, (1, 3): 2, (5, 3): 9, (4, 2): 6, (5, 2): 8, (2, 2): 4, (1, 4): 3, (5, 5): 17,
# (3, 3): 5, (4, 4): 10, (1, 1): 1}
