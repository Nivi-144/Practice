n = 5
# Top half
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
# Bottom half  
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
