#! /usr/bin/python3

import numpy as np


def generate_matrix(n):
    """
    Parameters
    ----------
        n : int
            Rank of the square matrix
    Returns
    -------
        2DArray
            Return a rank n square matrix
    """
    x = np.arange(0, n, 1)
    y = np.arange(1, n + 1, 1)
    xx, yy = np.meshgrid(x, y)
    ut = np.triu(xx ** 2 + yy)
    lt = np.tril(yy ** 2 - xx, k=-1)
    return ut + lt


def complete_matrix(mat, n, m):
    """
    Parameters
    ----------
        mat : 2DArray
            square matrix to complete
        n : int
            number of row in the matrix
        m : int
            number of column in the matrix
    Return
    -------
        2DArray
            Return the matrix completed with rows
    """
    x = np.arange(0, m, 1)[::-1]
    y = np.arange(m ** 2 + 1, m ** 2 + 1 + m * (n - m), m)
    xx, yy = np.meshgrid(x, y)
    return np.concatenate((mat, xx + yy))


def complete_matrix_transpose(mat, n, m):
    """
    Parameters
    ----------
        mat : 2DArray
            square matrix to complete
        n : int
            number of row in the matrix
        m : int
            number of column in the matrix
    Return
    -------
        2DArray
            Return the matrix completed with columns
    """
    x = np.arange(0, n, 1)
    y = np.arange(n ** 2 + 1, n ** 2 + 1 + n * (m - n), n)
    xx, yy = np.meshgrid(x, y)
    return np.concatenate((mat, (xx + yy).T), 1)


def generate_matrix_assignment(n, m):
    """
    Parameters
    ----------
        n : int
            number of row in the matrix
        m : int
            number of column in the matrix
    Return
    -------
        2DArray
            Return the matrix completed
    """
    minsize = n
    if m < minsize:
        minsize = m
    matrix = generate_matrix(minsize)
    if n > m:
        return complete_matrix(matrix, n, m)
    if m > n:
        return complete_matrix_transpose(matrix, n, m)
    return matrix


if __name__ == '__main__':
    while True:
        try:
            n = int(input("Enter N : "))
            m = int(input("Enter M : "))
            if n <= 0 or m <= 0:
                raise ValueError
            break
        except ValueError:
            print("N and M must be integers greater than 0")
            continue
    print(generate_matrix_assignment(n, m))
