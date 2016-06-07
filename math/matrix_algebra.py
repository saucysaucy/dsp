import numpy as np
import sys
import traceback

# Matrix Algebra
A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
mew = np.matrix('6 2 -3 5')
nu = np.matrix('3 5 -1 4')
omega = np.matrix('1; 8; 0; 5')

# Write Dimwnsions
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
two_d = np.tensordot(mew, nu)
two_e = np.linalg.norm(mew)

print(
    '2.1) %s' % str(two_a),
    '2.2) %s' % str(two_b),
    '2.3) %s' % str(two_c),
    '2.4) %s' % str(two_d),
    '2.5) %s' % str(two_e)
    )
    

# Evaluate each of the following expressions, if it is defined; else fill in with ”not defined.” Do your work by hand on scratch paper.

try:
    three_a = np.add(A, C)
    print('3.%i) \n%s' % (count,three_a))
except:
    print('not defined')
try:
    three_b = np.subtract(A,np.transpose(C))
    print('3.%i) \n%s' % (count,three_b))
except:
    print('not defined')
try:
    three_c = np.add(np.transpose(C), 3*D)
    print('3.%i) \n%s' % (count,three_c))
except:
    print('not defined')
try:
    three_d = np.multiply(B, A)
    print('3.%i) \n%s' % (count,three_d))
except:
    print('not defined')
try:
    three_e = np.multiply(B, np.transpose(A))
    print('3.%i) \n%s' % (count,three_e))
except:
    print('not defined')
    
    #or
    #print(sys.exc_info()[3])
    
# Optional
three_f = np.multiply(B,C) 
three_g = np.multiply(C, B) 
three_h = np.power(B,4)
three_i = np.dot(A, np.transpose(A)) 
three_j = np.dot(np.transpose(D), D)

print (
    three_f,
    three_g,
    three_h,
    three_i,  
    three_j 
    )