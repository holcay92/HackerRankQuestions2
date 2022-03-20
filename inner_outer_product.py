#Haldun Halil Olcay
import numpy

A = set(map(int, input().split()))

B = set(map(int, input().split()))

A = numpy.array(A)
B = numpy.array(B)

print(numpy.inner(A, B))

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print(numpy.outer(A, B))


