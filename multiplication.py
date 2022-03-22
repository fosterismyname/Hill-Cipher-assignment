import numpy as np

def matrix_multiplication(cur_matrix):
    '''
    funсtion for matrix multiplication of 2 matrix and encoded matrix
    :param cur_matrix: matrix of 2 symbols of original text (1x2)
    :return: matrix of encoded symbols (1x2)
    '''
    result_matrix = []
    add_matrix = [[4,5],[3,4]] #key-matrix
    mult_matrix = np.matmul(cur_matrix,add_matrix)
    for i in range(0,len(mult_matrix),1):
        result_matrix.append(mult_matrix[i]%28)
    print(result_matrix[0])

