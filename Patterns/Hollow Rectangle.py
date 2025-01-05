'''
* * * * *
* _ _ _ *
* _ _ _ *
* * * * *
'''
row = 4
col = 5
for r in range(row):
    if r == 0 or r == row-1:
        for c in range(col):
            print("*", end=' ')
    else:
        print("*", end=' ')
        for i in range(col-2):
            print(' ', end=' ')
        print('*', end=' ')
    print('')