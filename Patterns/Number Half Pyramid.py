'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''
row = 6
#col = 6
for r in range(row):
    for i in range(r + 1):
        print(i+1, end=' ')
    print('')