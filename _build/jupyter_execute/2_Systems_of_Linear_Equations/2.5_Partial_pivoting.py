#!/usr/bin/env python
# coding: utf-8

# (partial-pivoting-section)=
# # Partial pivoting
# 
# In most practical applications of row reduction to solve a linear system we use computers to perform the calculations. Computers use floating point numbers to compute arithmetic operations which are not exact and can be prone to rounding errors. Consider the following linear system of equations
# 
# \begin{align}
#   \begin{pmatrix}0.0001 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}= 
#   \begin{pmatrix}1 \\ 2 \end{pmatrix}.
# \end{align}
# 
# Using Gaussian elimination to solve this system
# 
# \begin{align*}
#     & \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         1 & 1 & 2 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 1000R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         0 & -9999 & -9998 
#     \end{array} \right)
#     \begin{array}{l} \\  -\frac{1}{9999}R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         0 & 1 & 0.9998\dot{9}
#     \end{array} \right).
# \end{align*}
# 
# So $x_2 = 0.9998\dot{9}$. If we were to round this to four decimal places then $x_2 = 1.0000$ and using back substitution we have $x_1 = \dfrac{1}{0.0001}(1 - 1) = 0$. However, checking our solution with the original system we see that this does not satisfy the second equation $x_1 + x_2 = 2$. The problem is that our first pivot element of 0.0001 was small compared with the value below which produced large values when adding multiples of the pivot row to the other rows. 
# 
# To overcome this we can perform a row swap so that the pivot element is larger than the value below
# 
# \begin{align*}
#     & \left(\begin{array}{cc|c} 
#         0.0001 & 1 & 1 \\
#         1 & 1 & 2 
#     \end{array} \right)
#     \begin{array}{l} R_1 \leftrightarrow R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         1 & 1 & 2 \\
#         0.0001 & 1 & 1 
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - 0.0001 R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{cc|c} 
#         1 & 1 & 2 \\
#         0 & 0.9999 & 0.9998
#     \end{array} \right)
# \end{align*}
# 
# Solving using back substitution we have $x_2 = \dfrac{0.9998}{0.9999} = 0.9998\dot{9}$ which rounded to four decimal places is $x_2 = 1.0000$ as before. However, this time using back substitution we now have $x_1 = 2 - 1.0000 = 1.0000$ which is consistent with the original system. This process is called *partial pivoting* and it's where we perform a row swap to ensure that the pivot element has a larger absolute value from the elements in the column beneath the pivot.
# 
# ````{admonition} Definition: Gaussian elimination with partial pivoting
# :class: note
# :name: ge-pp-definition
# 
# To row reduce an $m \times n$ matrix $A$ to reduced row echelon form using Gaussian elimination with partial pivoting we do the following: 
# 
# 1. Initalise the pivot row to $i=1$ and pivot column to $k=1$
# 2. Swap the pivot row $i$ with the row below which has the largest absolute value element in the pivot column $k$ which is greater than the absolute value of the pivot element $|a_{ik}|$. 
# 3. If $a_{ik} = 0$ then set $k = k + 1$ and repeat step 2.
# 4. For each row $j = i+1 \ldots m$ beneath the pivot row subtract the pivot row $i$ multiplied by $\dfrac{a_{jk}}{a_{ik}}$ from row $j$. 
# 5. Set $i = 1 + 1$ and $k = k + 1$ and repeat steps 2 to 4 until $i > m$ or $k > n$.
# ````
# 
# ````{admonition} Example 2.5
# :class: seealso
# :name: partial-pivoting-example
# 
# Solve the system of linear equations using Gaussian elimination with partial pivoting. 
# 
# \begin{align*}
#     \begin{array}{rcl}
#         x_1 - x_2 + 3x_3 &=& 13, \\
#         4x_1 - 2x_2 + x_3 &=& 15, \\
#         -3x_1 - x_2 + 4x_3 &=& 8.
#     \end{array}
# \end{align*}
# 
# ```{dropdown} Solution
# \begin{align*}
#     & \left(\begin{array}{ccc|c} 
#         1 & -1 & 3 & 13 \\
#         4 & -2 & 1 & 15\\
#         -3 & -1 & 4 & 8
#     \end{array} \right) 
#     \begin{array}{l} R_1 \leftrightarrow R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         1 & -1 & 3 & 13 \\
#         -3 & -1 & 4 & 8
#     \end{array} \right)
#     \begin{array}{l} \\  R_2 - \frac{1}{4}R_1 \\[1pt]  R_3 + \frac{3}{4}R_1 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{1}{2} & \frac{11}{4} & \frac{37}{4} \\
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4}
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 \leftrightarrow R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4} \\
#         0 & -\frac{1}{2} & \frac{11}{4} & \frac{37}{4}
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - \frac{1}{5}R_2 \end{array} \\ \\
#     \longrightarrow \quad &
#     \left( \begin{array}{ccc|c}
#         4 & -2 & 1 & 15\\ 
#         0 & -\frac{5}{2} & \frac{19}{4} & \frac{77}{4} \\
#         0 & 0 & \frac{9}{5} & \frac{27}{5}
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - \frac{1}{5}R_2 \end{array}
# \end{align*}
# Solving for $x_3$, $x_2$ and $x_1$ using back substitution
# \begin{align*}
#     x_3 &= \frac{5}{9}\left( \frac{27}{5} \right) = 3, \\
#     x_2 &= -\frac{2}{5} \left( \frac{77}{4} - \frac{19}{4}(3)\right) = -2, \\
#     x_1 &= \frac{1}{4}( 15 + 2(-2) - 3) = 2. 
# \end{align*}
#  
# ```
# ````

# ## Python code
# 
# The Python code below defines the function `gelimpp()` that uses Gaussian elimination with partial pivoting to determine the row echelon form of a matrix `A`. 

# In[1]:


def gelimpp(A):    
    
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
        for i in range(row + 1, nrows):
            if i != row and A[row,col] != 0:
                A[i,:] -= A[i,col] / A[row,col] * A[row,:]
        
        # Move to next column
        col += 1
                       
    return A


# This has been used to determine the row echelon form of the coefficient matrix from [example 2.5](partial-pivoting-example).

# In[2]:


import sympy as sym

# Define coefficient matrix and constant vector
A = sym.Matrix([[1, -1, 3], 
                [4, -2, 1], 
                [-3, -1, 4]])
b = sym.Matrix([[13], [15], [8]])

# Form augmented matrix
Ab = A.row_join(b)
display(Ab)

# Calculate row echelon form using Gaussian elimination with partial pivoting
Ab = gelimpp(Ab)
display(Ab)


# The solution of the system of linear equations is then calculated using the function `backsub()` (from [Gaussian elimination](backsub-code)).

# In[3]:


def backsub(A):
    m = A.shape[0]
    x = A[:,-1]
    for i in range(m - 1, -1, -1):
        for j in range(i + 1, m):
            x[i] -= A[i,j] * x[j]

        x[i] /= A[i,i]
    
    return x


# In[4]:


# Calculate solution using back substitution
x = backsub(Ab)
display(x)

