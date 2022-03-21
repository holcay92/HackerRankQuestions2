#h.halil olcay
import numpy as np

N_M:int = list(map(int, input().split()))
if not N_M[0] >= 1: exit("constrain for N")
if not N_M[1] <= 1000: exit("constrain for M")

#print(N_M)
attributes = list()
for i in range(0, (N_M[0])):
    attributes.append(list(map(int, input().split())))
#print(attributes)
K = int(input())
if not 0 <= K < N_M[1]: exit("constrain for K")
attributes = np.sort(attributes, axis=K)
print(attributes)

