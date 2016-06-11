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

# Write Dimwnsions

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
    sep='\n')
    

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
    yield np.power(B,4)
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