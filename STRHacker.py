#import ipdb
#ipdb.set_trace()
n = 3
l1 = list(map(chr, range(97, 123)))
x = l1[n - 1::-1] + l1[1:n]
m = len('-'.join(x))
for i in range(1, n):
    print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(m, '-'))
for i in range(n, 0, -1):
    print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(m, '-'))