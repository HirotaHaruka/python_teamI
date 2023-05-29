

H, W, N = map(int, input().split())
b_c = [[0 for _ in range(W-2) ] for _ in range(H-2)]
for i in range(N):
    a, b = map(int, input().split())
    a, b = a-2, b-2
    for j in range(a-1,a+2):
        if j < 0 or j >= H-2: continue
        for k in range(b-1,b+2):
            if k < 0 or k >= W-2: continue
            b_c[j][k] += 1

import itertools
b_c = list(itertools.chain.from_iterable(b_c))

for i in range(10):
    print(b_c.count(i))
