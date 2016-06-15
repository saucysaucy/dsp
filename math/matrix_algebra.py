import numpy as np
np.set_printoptions(linewidth=500)

# Matrix Algebra
A = np.array([
    [1, 2, 3],
    [2, 7, 4,]])
B = np.array([[1, -1],
             [0, 1]])
C = np.array([[5, -1],
             [9,1],
             [6, 0]])
D = np.array([[3, -2, -1],
             [1, 2, 3]])
mew = np.array([6, 2, -3, 5])
nu = np.array([3, 5, -1, 4])
omega = np.array([[1],
                 [8],
                 [0],
                 [5]])

# Write Dimensions

print('\nMatrix and Vector Dimentions\n')

print(
    'Shape of A is: %s' % str(A.shape),
    'Shape of B is: %s' % str(B.shape),
    'Shape of C is: %s' % str(C.shape),
    'Shape of D is: %s' % str(D.shape),
    'Shape of mew is: %s' % str(mew.shape),
    'Shape of nu is: %s' % str(nu.shape),
    'Shape of omega is: %s' % str(omega.shape),
    sep='\n'
    )

#  Perform the following operations

alpha = 6

two_a = np.add(mew, nu)
two_b = np.subtract(mew, nu)
two_c = np.multiply(alpha, mew)
two_d = np.vdot(mew, nu)
two_e = np.linalg.norm(mew)

print('\n'
    '2.1) %s' % str(two_a),
    '2.2) %s' % str(two_b),
    '2.3) %s' % str(two_c),
    '2.4) %s' % str(two_d),
    '2.5) %s' % str(two_e),
    sep = '\n')

# Evaluate each of the following expressions, if it is defined; else fill in with ”not defined.” Do your work by hand on scratch paper.

print('\nEvaluating Expressions\n')

def three_a(A,C):
    yield np.add(A, C)
def three_b(A,C):
    yield np.subtract(A,np.transpose(C))
def three_c(C,D):
    yield np.add(np.transpose(C), 3*D)
def three_d(B,A):
    yield np.dot(B, A)
def three_e(B,A):
    yield np.dot(B, np.transpose(A))

def three_f(B,C):
    yield np.dot(B,C)
def three_g(C,B):
    yield np.dot(C, B)
def three_h(B):
    yield np.linalg.matrix_power(B,4)
def three_i(A):
    yield np.dot(A, np.transpose(A))
def three_j(D):
    yield np.dot(np.transpose(D), D)

count = 1
for i in [three_a(A,C), three_b(A,C), three_c(C,D), three_d(B,A), three_e(B,A), three_f(B,C), three_g(C,B), three_h(B), three_i(A), three_j(D)]:
    try:
        i = tuple(i)
        print('3.%i) \n%s' % (count, i),'\n')
        count+=1
    except:
        print('3.%i) \nnot defined' % count,'\n')
        count+=1


"""
Matrix and Vector Dimentions

Shape of A is: (2, 3)
Shape of B is: (2, 2)
Shape of C is: (3, 2)
Shape of D is: (2, 3)
Shape of mew is: (4,)
Shape of nu is: (4,)
Shape of omega is: (4, 1)

2.1) [ 9  7 -4  9]
2.2) [ 3 -3 -2  1]
2.3) [ 36  12 -18  30]
2.4) 51
2.5) 8.60232526704

Evaluating Expressions

3.1)
not defined

3.2)
(array([[-4, -7, -3],
       [ 3,  6,  4]]),)

3.3)
(array([[14,  3,  3],
       [ 2,  7,  9]]),)

3.4)
(array([[-1, -5, -1],
       [ 2,  7,  4]]),)

3.5)
not defined

3.6)
not defined

3.7)
(array([[ 5, -6],
       [ 9, -8],
       [ 6, -6]]),)

3.8)
(array([[ 1, -4],
       [ 0,  1]]),)

3.9)
(array([[14, 28],
       [28, 69]]),)

3.10)
(array([[10, -4,  0],
       [-4,  8,  8],
       [ 0,  8, 10]]),)

"""