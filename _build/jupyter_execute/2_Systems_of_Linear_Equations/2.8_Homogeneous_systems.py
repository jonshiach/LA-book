#!/usr/bin/env python
# coding: utf-8

# (homogeneous-systems-section)=
# # Homogeneous systems
# 
# ````{admonition} Definition: Homogeneous systems
# :class: note
# :name: homogeneous-system-definition
# 
# A **homogeneous** system of linear equations is of the form $A\mathbf{x} = \mathbf{0}$, i.e.,
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn}
#     \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = 
#     \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}.
# \end{align*}
# ````
# 
# A homogeneous system always as the **trivial** solution $\mathbf{x} = \mathbf{0}$ so a homogeneous system is always consistent. If $\mathbf{x} = \mathbf{0}$ is not the only solution then the system is indeterminate and there will be infinitely many non-trivial solutions. 
# 
# When a homogeneous system is solved by Gaussian elimination, the column of zeros on the right of the partition in the augmented matrix remains unchanged at each stage, since none of the three types of elementary row operations can introduce a non-zero entry in this column. Hence we can save time by omitting this column, instead we simply apply elementary row operations to the coefficient matrix until the row echelon form or reduced row echelon form is obtained, but then remember to restore the zeros to the right-hand sides of the simplified equations at the end.
# 
# `````{admonition} Example 2.9
# :class: seealso
# :name: homogeneous-systems-example
# 
# Solve the following homogeneous system of linear equations using Gauss-Jordan elimination
# 
# \begin{align*}
#     x_1 + 2x_3 - x_5 &= 0, \\
#     2x_1 + 4x_3 - 2x_4 + 4x_5 &= 0, \\
#     x_2 + x_3 +2x_4 &= 0.
# \end{align*}
# 
# ````{dropdown} Solution
# 
# Applying elementary row operations to the coefficient matrix
# 
# \begin{align*}
#     & \begin{pmatrix}
#         1 & 0 & 2 & 0 & -1 \\
#         2 & 0 & 4 & -2 & 4 \\
#         0 & 1 & 1 & 2 & 0
#     \end{pmatrix}
#     \begin{array}{l} \\ R_2 - 2R_1 \\ \phantom{x} \end{array} \\[1em]
#     \longrightarrow \quad &
#     \begin{pmatrix}
#         1 & 0 & 2 & 0 & -1 \\
#         0 & 0 & 0 & -2 & 6 \\
#         0 & 1 & 1 & 2 & 0
#     \end{pmatrix}
#     \begin{array}{l} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\[1em]
#     \longrightarrow \quad &
#     \begin{pmatrix}
#         1 & 0 & 2 & 0 & -1 \\
#         0 & 1 & 1 & 2 & 0 \\
#         0 & 0 & 0 & -2 & 6 
#     \end{pmatrix}
#     \begin{array}{l} \\ \\ -\frac{1}{2} R_3 \end{array} \\[1em]
#     \longrightarrow \quad &
#     \begin{pmatrix}
#         1 & 0 & 2 & 0 & -1 \\
#         0 & 1 & 1 & 2 & 0 \\
#         0 & 0 & 0 & 1 & -3 
#     \end{pmatrix}
#     \begin{array}{l} \\ R_2 - 2R_3 \\ \phantom{x} \end{array} \\[1em]
#     \longrightarrow \quad &
#     \begin{pmatrix}
#         1 & 0 & 2 & 0 & -1 \\
#         0 & 1 & 1 & 0 & 6 \\
#         0 & 0 & 0 & 1 & -3 
#     \end{pmatrix}
# \end{align*}
# 
# The coefficient matrix is now in reduced row echelon form so we can form the augmented matrix
# 
# \begin{align*}
#     \left( \begin{array}{ccccc|c}
#         1 & 0 & 2 & 0 & -1 & 0 \\
#         0 & 1 & 1 & 0 & 6 & 0 \\
#         0 & 0 & 0 & 1 & -3 & 0
#     \end{array} \right)
# \end{align*}
# 
# Here we have 5 variables and, since columns 3 and 5 do not have pivots, 2 free parameters which are $x_3$ and $x_5$. Let $r = x_3 $ and $s = x_5$ then solving for $x_1$, $x_2$ and $x_4$ by back substitution we have
# 
# \begin{align*}
#     x_4 &= 3s, \\
#     x_2 &= -6s - r, \\
#     x_1 &= s - 2r.
# \end{align*}
# ````
# `````

# In[1]:


def rref(A):    
    
    # Loop through rows of A
    nrows, ncols = A.shape
    col = 0
    for row in range(nrows):
        
        # Swap current row if pivot element is zero
        pivotrow = row
        while A[pivotrow,col] == 0:
            pivotrow += 1
            if pivotrow == nrows:
                pivotrow, col = row, col + 1
                if col == ncols:
                    break
        
        A[row,:], A[pivotrow,:] = A[pivotrow,:], A[row,:]
        
        # Perform partial pivoting (swap pivot row if there is a larger value in the pivot column)
        for i in range(row + 1, nrows):
            if abs(A[i,col]) > abs(A[row,col]):
                A[row,:], A[i,:] = A[i,:], A[row,:]
        
        # Row reduce non-pivot rows
        display(A)
        for i in range(nrows):
            if i != row and A[row,col] != 0:
                A[i,:] -= A[i,col] / A[row,col] * A[row,:]
                
        # Divide pivot row by pivot
        A[row,:] /= A[row,col]
        
        # Move to next column
        col += 1
                       
    return A


import sympy as sym

A = sym.Matrix([[1, 0, 2, 0, -1], 
                [2, 0, 4, -2, 4], 
                [0, 1, 1, 2, 0]])
display(A)
display(rref(A))

