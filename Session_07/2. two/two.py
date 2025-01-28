print('start')
N = 5
i = 0
while i < N:
    print('Outer Loop start with i: ', i)
    j = i
    while j < N:
        print(f'i: {i}, j: {j}')
        j = i + 1
    i = i + 1
print('end')
