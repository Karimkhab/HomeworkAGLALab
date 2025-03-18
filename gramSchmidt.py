import numpy as np


def normalize(v):
    return v / np.linalg.norm(v)

def gramSchmidt(a, b, c, d):

    A = np.array(a, dtype=float)
    q1 = normalize(A)

    B = np.array(b, dtype=float) - (np.dot(b, A) / np.dot(A, A)) * A
    q2 = normalize(B)

    C = np.array(c, dtype=float) - (np.dot(c, A) / np.dot(A, A)) * A - (np.dot(c, B) / np.dot(B, B)) * B
    q3 = normalize(C)

    D = np.array(d, dtype=float) - (np.dot(d, A) / np.dot(A, A)) * A - (np.dot(d, B) / np.dot(B, B)) * B - (
                np.dot(d, C) / np.dot(C, C)) * C
    q4 = normalize(D)

    return q1, q2, q3, q4


a = [1, -1, 0]
b = [1, 1, -2]
c = [1, 1, 1]
d = [0, 1, 1]

q1, q2, q3, q4 = gramSchmidt(a, b, c, d)
print( q1)
print(q2)
print(q3)
print(q4)
