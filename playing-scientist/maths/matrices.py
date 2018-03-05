import numpy as np

print(np.matrix('1 2 3; 1 0 1; 2 1 0').dot(
    np.matrix('1 0 2; 2 1 1; 3 1 2')))
# matrix([[14,  5, 10],
#         [ 4,  1,  4],
#         [ 4,  1,  5]])

print(np.matrix('1 0 2; 2 1 3; 1 2 0').dot(
    np.matrix('1; 2; 3')))
# matrix([[ 7],
#         [13],
#         [ 5]])


A = np.matrix('0 0 1; 1 0 0; 0 1 0')
I3 = np.matrix('1 0 0; 0 1 0; 0 0 1')

i = 2

while not np.array_equal(A ** i, I3):
    i += 1

print(i)
# 3

B = np.matrix('0 1 0 0; -1 0 0 0; 0 0 0 1; 0 0 1 0')
I4 = np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')

i = 2

while not np.array_equal(B ** i, I4):
    i += 1

print(i)
# 4

c = 0

for i in range(10000):
    M = np.random.rand(3, 3)
    N = np.random.rand(3, 3)
    if np.array_equal(M.dot(N), N.dot(M)):
        c += 1

print(c/10000)
# ^^^^ BROKEN ^^^^
