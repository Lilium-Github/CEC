import numpy

a = numpy.array([[1,2,3],
                [4,5,6]])

b = numpy.array([[10,11,12],
                [13,14,15]])

c = a + b # any given number in matrix c is equal to the sum of the numbers in that same position in matrices a and b

#print(c) 

d = b - a

#print(d) # any given number in matrix d is equal to the difference of the numbers in that same position in matrices b and a

scalar = 15

e = a * scalar

#print(e)

f = [[-2,3],
     [1,-4],
     [6,0]]

g = [[-1, 3],
     [-2, 4]]

     # should be [-4,6][7,-13][-6,18]

print(numpy.matmul(f,g))

h = numpy.array([[1, 3],
     [2, 5]])

print("Numpy Matrix is\n", h)

determinant = numpy.linalg.det(h)

print("\nDeterminant of given 2x2 matrix:")
print(int(determinant))