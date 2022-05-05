import numpy as np


def deCasteljau(P, t):
    """
    The deCastelJau algorithm. Creates a bezier curve at P.
    """
    n = len(P)
    Q = np.zeros((n, 2))
    Pvecs = []

    for i in range(n):
        Q[i] = P[i]
    for k in range(1, n):
        for i in range(0, n-k):
            Q[i] = (1-t)*Q[i] + t*Q[i+1]
            tmp = Q[i]
            Pvecs.append([tmp[0], tmp[1]])
            
    return Q[0], Pvecs

def compositeBézier(P, t):
    """
    Creates a composite bezier curve.
    """
    for i in range(len(P)):
        if (i <= t and t <= i + 1):
            return deCasteljau(P[i], t-i)[0]


def interpolate_periodic(A,V):

    n = 3
    m = len(A)-1

    A = np.array(A)
    V = np.array(V)

    P = []

    for i in range(1, m):
        row = [A[i-1], 1/n * V[i-1] + A[i-1], -1/n * V[i] + A[i], A[i]]
        P.append(np.array(row).tolist())

    extrarow = [A[m], 1/n * V[m] + A[m], -1/n * V[0] + A[0], A[0]]
    P.append(np.array(extrarow).tolist())

    return P

def point_velocity(A, sharpness = 1):
  """
  Creates a vector between Ai, Ai+1. Since this vector is the derivative of the
  bezier curve, we can scale the velocity down by the sharpness input. Making
  it less curvy.
  """
  V = [[A[i][0] - A[i-1][0], A[i][1] - A[i-1][1]] for i in range(1, len(A))]
  V.append([A[0][0] - A[len(A)-1][0], A[0][1] - A[len(A)-1][1]])
  V = 1/sharpness * np.array(V)
  return V.tolist()

