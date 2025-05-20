# import numpy as np
#
# mat1 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
# mat2 = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
# print(np.matmul(mat1,mat2))
# # print(np.matmul(mat2,mat1))

def dot(v1, v2, total=0):
    """
    [a1]   [b1]
    [a2] * [b2] --> a1b1 + a2b2 + a3b3
    [a3]   [b3]
    :param v1: row vector
    :param v2: column vector
    :param total: to be initialized by the function
    :return: final value
    """
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

def transpose (mat):
    """
    1 2 3     1 4 7
    4 5 6 --> 2 5 8
    7 8 9     3 6 9
    :param mat: a matrix in the form of arrays like: this means
                                          [[1, 2, 3],
        [[1, 2, 3],[4, 5, 6],[7, 8, 9]] -->[4, 5, 6],
                                           [7, 8, 9]]
    """

    # mat_t = []
    # for i in range(len(mat[0])):
    #     row = []
    #     for j in range(len(mat)):
    #         row.append(mat[j][i])
    #     mat_t.append(row)

    mat_t = [[row[i] for row in mat] for i in range(len(mat[0]))]

    return mat_t

def matprod (m1, m2, final = []):
    m2_t = transpose(m2)

    for i in range(len(m1)):
        row = []
        for j in range(len(m2_t)):
            row.append(dot(m1[i], m2_t[j]))
        final.append(row)

    return final

mat1 = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
mat2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

print(matprod(mat1, mat2))