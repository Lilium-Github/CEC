import numpy

def lilyRotate(inMatrix): #rotates a 2x2 matrix clockwise once
    newMatrix = numpy.array([[0, 0],[0, 0]])

    newMatrix[0,0] = inMatrix[0,1]
    newMatrix[0,1] = inMatrix[1,1]
    newMatrix[1,1] = inMatrix[1,0]
    newMatrix[1,0] = inMatrix[0,0]

    return newMatrix

matthew = numpy.array([[1, 3],
                       [2, 5]])

print(lilyRotate(matthew))
