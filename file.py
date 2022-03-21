# Full print statement initiation
# print(*objects, sep=' ', end='\n', flush=False)
# Flush defines if we create a log file or no

# a = int(input("Enter a number: "))
# print('The previous number is ', a-1, ', the next number is ', a+1, sep='')

#
# num = int(input('Whats the year?\n'))
# if 4 == 0 and 100 != 0 or 400 == 0:
#     print('True')
# else:
#     print('False')

# Break and continue, full "for" cycle initialization

# for i in range (0,10,3):
#     print(i)
#     if i != 6:
#         continue
#     else:
#         print("Work ended")

# Working with arrays
# We're working not with values but with adresses of these values
# a = [1,2,3]
# b = [4,5,6]
# a.remove(2)
# print(a)
# a.append(7)
# b = a.copy
# b = [1,2,3] - assignment by value and bot by reference
# Can be initialized using 'list' function
# a = list('lorem ipsum')
# print(a)

# Dictionaries (tuples) - not ordered, can't be accessed using indexes
# c = {'a': 1, 'b': 3}
# print (c['a'])
# Can be initialized using 'tuple' function
# a = tuple('hello')
# print(a)
# import math
# a = int(input())
# hours = math.floor(a/60)
# minutes = a - hours * 60
# while hours>=24:
#     hours = hours-24
# print(hours, ":", minutes)

# TASK 1
# N = int(input('Total number of cards: '))
# cont = input('Enter numbers of cards you havent managed to lose yet: ')
# s = cont.split(' ')
# sint = (list(map(int, s)))
# print(sint)
# for i in range(1, N+1):
#     if (i not in sint ):
#         print("The number of the lost card is ", i)
#
# TASK 2
# counter1 = 1
# counter2 = 0
# i = 0
# s = input("Enter a number sequence: ")
# for i in range(1, len(s)):
#     if (s[i] == s[i - 1]):
#         counter1 += 1
#     else:
#         if counter1 > counter2:
#             counter2 = counter1
#         counter1 = 1
#     i += 1
# print(counter2)


# TASK 3
# a = int(input('A: '))
# b = int(input('B: '))
# c = int(input('C: '))
# d = int(input('D: '))
# e = int(input('E: '))
# if (a*b <=d*e or c*b <= d*e or a*c <= d*e ):
#    print('Yes')
# else:
#    print('no')

# Function defenition

# def sum1 (a, b, c, *num):
#     ''' result of the addition of variables '''
#     d = 0
#     s = 0
#     for i in num:
#         d+=i
#
#
# print(sum(a, b, c, *d))

# TIMUS 2078

# pins = input().split(' ')
# pinsArr = [int(x) for x in pins]
# max = 0
# min = 0
# for i in range(0, len(pinsArr)):
#     min += pinsArr[i]
#     if i < 8 and pinsArr[i] == 10 and pinsArr[i+1] != 10:
#         max += pinsArr[i+1]
#     if i < 8 and pinsArr[i] == 10 and pinsArr[i+1] == 10 and pinsArr[i+2] <= 10:
#         max += pinsArr[i+1]
#         max += pinsArr[i+2]
#     if i == 7 and pinsArr[i] == 10 and pinsArr[i+1] == 10 and pinsArr[i+2] > 10:
#         max += pinsArr[i+1]+10
#     if i == 8 and pinsArr[i] == 10 and pinsArr[i+1] <= 20:
#         max += pinsArr[i+1]
#     if i == 8 and pinsArr[i] == 10 and pinsArr[i+1] > 20:
#         max += 10
#         min += 10
# max += min
# print(min, max)

# TIMUS 1820

# n, k = map(int, input().split())
# time = 0
# if k >= n:
#     time += 2
# else:
#     if (n*2) % k == 0:
#         time += (n * 2) / k
#     else:
#         time += (n * 2) / k + 1
# print(int(time))

# Hanoi Towers

# def hanoi_tower(n, A, B, C):
#    '''
#    Defines the movements of disks in order to move them from the starting to the finishing rod
#     :param n: number of disks
#     :param A: first rod
#     :param B: second rod
#     :param C: third rod
#     '''
#     if n == 1:
#         print('transfer the disk 1 from rod ', A, 'to', B)
#         return
#     hanoi_tower(n - 1, A, C, B)
#     print('transfer the disk', n, 'from', A, 'to', B)
#     hanoi_tower(n - 1, C, B, A)
# number = int(input())
# hanoi_tower(number, 'A', 'B', 'C')


# Bubble sort
# def bubbleSort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Shaker sort

lst = [3,6,1,5,2,4,7]


# Merge sort

#     function
#     merge(left, right) is
#     var
#     result := empty
#     list
#
#     while left is not empty and right is not empty do
#     if first(left) ≤ first(right) then
#     append
#     first(left)
#     to
#     result
#     left := rest(left)
#
# else
# append
# first(right)
# to
# result
# right := rest(right)
#
# // Either
# left or right
# may
# have
# elements
# left;
# consume
# them.
# // (Only one of the following loops will actually be entered.)
# while left is not empty do
# append
# first(left)
# to
# result
# left := rest(left)
# while right is not empty do
# append
# first(right)
# to
# result
# right := rest(right)
# return result

# Insertion sort

# list = [5,9,4,2,3,6,1,7]
# def sorting_again(list):
#     n = len(list)
#     for i in range(1, n, 1):
#         if list[i] < list[i-1]:
#             temp = list[i]
#             list.pop(i)
#             for i in range(i, 0, -1):
#                 if list[i-1] < temp:
#                     list[i] = temp
#     print(list)


# TIMUS 2001
# a = []
# b = []
# for i in range(3):
#     s = input().split()
#     a += [int(s[0])]
#     b += [int(s[1])]
# print(a[0] - a[2], b[0] - b[1])
#
#
#
#
# TIMUS 1800
#
#
# from math import sqrt
# def fraction(n):
#     '''
#     returns fractional part of the input
#     '''
#     return (n - int(n))
#
# def check(l, h, w):
#     '''
#     returns the side on which the sandwich will fall
#     :param l: length
#     :param h: height
#     :param w: angle velocity
#     :return: side
#     '''
#     if l/2 > h:			# No rotating
#         return "butter"
#     t = (2*(h - l/2)/981)**0.5
#     Two cases based on the "guarters"
    # if (fraction(w*sqrt(2*(h-l/2)/981)/60)>=0 and (fraction(w*sqrt(2*(h-l/2)/981)/60)<=1/4)) or ((fraction(w*sqrt(2*(h-l/2)/981)/60)>=3/4) and (fraction(w*sqrt(2*(h-l/2)/981)/60)<=1)):
    #     return "butter"
    # else:
    #     return "bread"
#
#
# l, h, w = map(int, input().split())
# print(check(l, h, w))
#
# TIMUS 2012
#
# f = int(input())
# left = max(0, 12 - f)
# timeLeft = 240 - left * 45
# if timeLeft >= 0:
#     print("YES")
# else:
#     print("NO")
#
# TIMUS 1506
# n, k = map(int, input().split())
# k = (n + k - 1)//k
# s = list(map(int, input().split()))
# for j in range(k):
#     for i in range(j, n, k):
#         print("{:4}".format(int(s[i])), end = '')
#     print()


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




