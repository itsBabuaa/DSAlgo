row = 6
#col = 6
for r in range(1, row+1):
    for _ in range(row - r):
        print(' ', end='')
    for star in range(r):
        print('*', end=' ')
    print('')
for r in range(1, row+1):
    for _ in range(r):
        print(' ', end='')
    for star in range(row - r):
        print('*', end=' ')
    print('')