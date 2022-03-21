import numpy as np
import math as mt


def Gcd_extended(num1, num2):  # расширенный алгоритм Евклида для нахождения обратной матрицы
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = Gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)


def CreateMatrix(dimension):
    matrix = np.array([[0] * dimension] * dimension, dtype=np.int32)
    for i in range(dimension):
        for j in range(dimension):
            matrix[i][j] = int(input("matrix[{0}][{1}] = ".format(i, j)))
    return matrix


def PrintMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


def ReverseDet(det, x, alphabetLength): #TODO CHANGE TO 29
    # аргументы: детерминант матрицы ключа и х, полученный от
    # расширенного алгоритма Евклида, и длина алфавита
    if (det < 0) and (x > 0): return x
    if (det > 0) and (x < 0): return alphabetLength + x
    if (det > 0) and (x > 0): return x
    if (det < 0) and (x < 0): return -x


нахождение матрицы алгебраических дополнений
def AdjMatrix(matrix, detMatrix):
    reverseMatrix = np.linalg.inv(matrix)
    tempMatrix = np.transpose(detMatrix * reverseMatrix)
    return tempMatrix


def modForMatrix(matrix, dimension, alphabetLength):
    for i in range(dimension):
        for j in range(dimension):
            if (matrix[i][j] > 0):
                temp = matrix[i][j]
                matrix[i][j] = temp - ((temp // alphabetLength) * alphabetLength)
            else:
                temp = -matrix[i][j]
                matrix[i][j] = -(temp - ((temp // alphabetLength) * alphabetLength))
    return matrix


def ReverseMatrix(matrix, dimension, alphabetLength):
    for i in range(dimension):
        for j in range(dimension):
            if (matrix[i][j] < 0):
                temp = matrix[i][j]
                matrix[i][j] = alphabetLength + temp
            else:
                continue
    return matrix


def RoundingMatrix(matrix, dimension):
    for i in range(dimension):
        for j in range(dimension):
            a = matrix[i][j]
            print("Before: ", a, matrix[i][j], sep=' ')
            if (a > ((a // 1) + 0.5)):
                matrix[i][j] = round(matrix[i][j])
                print("After: ", a, matrix[i][j], sep=' ')
            else:
                matrix[i][j] = round(matrix[i][j])
                print("After: ", a, matrix[i][j], sep=' ')

    return matrix


dimension = int(input("Какого порядка будет матрица? Введите: "))
alphabetLength = int(input("Введите длину алфавита: "))

matrix = CreateMatrix(dimension)
# matrix = [[0,12,29],[16,9,14],[9,8,13]]
PrintMatrix(matrix)
detMatrix = int(np.linalg.det(matrix)) + 1
print("Определитель матрицы ключа: ", detMatrix)

x = Gcd_extended(detMatrix, alphabetLength)[1]  # Returns the x which is a coefficient

reverseDet = ReverseDet(detMatrix, x, alphabetLength)
print(reverseDet)

print(AdjMatrix(matrix, detMatrix))

adjMatrix = modForMatrix(AdjMatrix(matrix, detMatrix), dimension, 37)
print(adjMatrix)

reverseMatrix = np.transpose(modForMatrix(reverseDet * adjMatrix, dimension, alphabetLength))
print(reverseMatrix)

reverseMatrixDone = ReverseMatrix(reverseMatrix, dimension, alphabetLength)
print(reverseMatrixDone)

'''done = RoundingMatrix(reverseMatrixDone, dimension)
print(round(done[0][0]))'''

# def gnomeSort(arr):
#     n = len(arr)
#     for i in range(1, n, 1):
#         if arr[i] < arr[i-1]:
#             temp = arr[i-1]
#             arr[i-1] = arr[i]
#             arr[i] = temp
#             for j in range(i, 1, -1):
#                 if arr[j] < arr[j - 1]:
#                     temp = arr[j - 1]
#                     arr[j - 1] = arr[j]
#                     arr[j] = temp
#     return arr

# def quickSort(arr):
#     n = len(arr)
#     base = arr[n]
#
# print(quickSort([1,8,6,10,15,4,9,2,6,3]))




