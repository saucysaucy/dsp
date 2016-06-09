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

count = 1
try:
    three_a = np.add(A, C)
    print('3.%i) \n%s' % (count, three_a),'\n')
    count+=1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1
try:
    three_b = np.subtract(A,np.transpose(C))
    print('3.%i) \n%s' % (count, three_b),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1
try:
    three_c = np.add(np.transpose(C), 3*D)
    print('3.%i) \n%s' % (count, three_c),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1
try:
    three_d = np.dot(B, A)
    print('3.%i) \n%s' % (count, three_d),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1
try:
    three_e = np.dot(B, np.transpose(A))
    print('3.%i) \n%s' % (count, three_e),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n\n')
    count += 1
    
# Optional

print('Optional Problems\n\n')

try:
    three_f = np.dot(B,C)
    print('3.%i) \n%s' % (count, three_f),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1

try:
    three_g = np.dot(C, B)
    print('3.%i) \n%s' % (count, three_g),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1

try:
    three_h = np.power(B,4)
    print('3.%i) \n%s' % (count, three_h),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count, '\n')
    count += 1

try:
    three_i = np.dot(A, np.transpose(A))
    print('3.%i) \n%s' % (count, three_i),'\n')
    count += 1
except:
    print('3.%i) \nnot defined' % count,'\n')
    count += 1

try:
    three_j = np.dot(np.transpose(D), D)
    print('3.%i) \n%s' % (count, three_j),'\n')
    count += 1
except:
    print('3.%s) \nnot defined')
    count += 1