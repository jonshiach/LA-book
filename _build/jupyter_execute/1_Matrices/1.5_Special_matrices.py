#!/usr/bin/env python
# coding: utf-8

# # Special matrices
# 
# ## Diagonal matrix
# 
# ```{admonition} Definition: Diagonal matrix
# :class: note
# :name: diagonal-matrix-definition
# 
# The **main diagonal** of an $n \times n$ square matrix $A$ are the elements along the diagonal from the top-left element $a_{11}$ to the bottom right element $a_{nn}$. A **diagonal matrix** is a square matrix whose elements are all zero apart from those on the main diagonal, meaning $a_{ij} = 0$ for all $i\neq j$
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & 0 & \cdots & 0 \\
#         0 & a_{22} & \ddots & \vdots \\
#         \vdots & \ddots & \ddots & 0 \\
#         0 & \cdots & 0 & a_{nn}
#     \end{pmatrix}.
# \end{align*}
# ```
# 
# For example
# 
# \begin{align*}
#     &\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, &
#     &\begin{pmatrix} 3.7 & 0 & 0 \\ 0 & 12 & 0 \\ 0 & 0 & 2.1 \end{pmatrix}, &
#     &\begin{pmatrix} x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z \end{pmatrix}.
# \end{align*}
# 
# ## Zero matrix
# 
# Similarly to $0$ being a neutral element with respect to addition of real numbers, an $m \times n$ matrix of zeros plays the role of a neutral element for addition of matrices.
# 
# ```{admonition} Definition: Zero matrix
# :class: note
# :name: zero-matrix-definition
# 
# A **zero matrix** (or **null matrix**) is an $m \times n$ matrix $\mathbf{0}_{m \times n} = \mathbf{0}$ where all the entries are zero, that is $[\mathbf{0}]_{ij} = 0$ for all $i$ and $j$
# ```
# 
# For example
# \begin{align*}
#     \mathbf{0}_{2 \times 2} &= \begin{pmatrix}0 & 0 \\ 0 & 0 \end{pmatrix}, &
#     \mathbf{0}_{2 \times 3} &= \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, &
#     \mathbf{0}_{3 \times 1} &= \begin{pmatrix}0 \\ 0 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# ```{admonition} Theorem: Addition of a zero matrix
# :class: important
# :name: zero-matrix-theorem
# 
# For any $m \times n$ matrix $A$ and $\mathbf{0} = \mathbf{0}_{m \times n}$
# 
# $$A + \mathbf{0} = \mathbf{0} + A = A.$$
#  
# Thus zero matrices are **neutral elements with respect to matrix addition**.
# ```
# 
# ### Python code
# 
# The SymPy code for generating an $m \times n$ zero matrix is `sym.zeros(m, n)`. The Python code below generates the zero matrices given above

# In[1]:


import sympy as sym

zeros_2x2 = sym.zeros(2)
display(zeros_2x2)

zeros_2x3 = sym.zeros(2, 3)
display(zeros_2x3)

zeros_3x1 = sym.zeros(3, 1)
display(zeros_3x1)


# ## The identity matrix
# 
# ```{admonition} Definition: The identity matrix
# :class: note
# :name: identity-matrix-definition
# 
# The **identity matrix** is denoted by $I_n$ is an $n\times n$ diagonal matrix where the elements on the main diagonal are all 1, i.e.,
# 
# \begin{align*}
#     [I]_{ij} = \begin{cases} 1, & i = j, \\ 0, & i\neq j. \end{cases}
# \end{align*}
# ```
# 
# For example
# \begin{align*}
#     I_2 &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, &
#     I_3 &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, &
#     I_4 &= \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
# \end{align*}
# 
# It is common to omit the subscript as it should be clear what the dimensions are from the context.
# 
# ```{admonition} Theorem: Properties of the identity matrix
# :class: important
# :name: properties-of-the-identity-matrix
# 
# - For any $m\times n$ matrix $A$, $I_m A = A I_n$;
# - For any $n\times n$ square matrix $A$, $IA=AI=A$.
# 
# Thus for square matrices $I$ is an identity element with respect to matrix multiplication.
# ```
# 
# ````{admonition} Example 1.8
# :class: seealso
# :name: identity-matrix-example
# 
# Given the matrices $A = \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 2 \\ 4 & 3 \\ -2 & 1 \end{pmatrix}$ evaluate:
# 
# 
# &emsp; (i) &emsp; $IA$
# 
# &emsp; (ii) &emsp; $AI$
# 
# &emsp; (iii) &emsp; $IB$
# 
# ```{dropdown} Solution
# 
# &emsp; (i) 
# \begin{align*}
#     IA &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix} 
#     = \begin{pmatrix} 1 + 0 & 0  + 0 \\ 0 - 2 & 0 + 3 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}
# \end{align*}
#         
# &emsp; (ii) 
# \begin{align*}
#     AI &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
#     = \begin{pmatrix} 1 + 0 & 0 + 0 \\ -2 + 0 & 0 + 3 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}
# \end{align*}
#         
# &emsp; (iii)
# \begin{align*}
#     IB &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 4 & 3 \\ -2 & 1 \end{pmatrix} 
#     = \begin{pmatrix} 1 + 0 + 0 & 2 + 0 + 0 \\ 0 + 4 + 0 & 0 + 3 + 0 \\ 0 + 0 - 2 & 0 + 0 + 1 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 & 2 \\ 4 & 3 \\ -2 & 1 \end{pmatrix}
# \end{align*}
# ```
# ````
# 
# ### Python code
# 
# The Python code for generating an $n \times n$ identity matrix is `sym.eye(n)`. The code below calculates the solution to [example 1.8](identity-matrix-example).

# In[2]:


import sympy as sym

A = sym.Matrix([[1, 0], [-2, 3]])
B = sym.Matrix([[1, 2], [4, 3], [-2, 1]])

# (i)
IA = sym.eye(2) * A
print("(i) IA =")
display(IA)

# (ii) 
AI = A * sym.eye(2)
print("(ii) AI =")
display(AI)

# (iii)
IB = sym.eye(3) * B
print("(iii) IB =")
display(IB)


# ## Symmetric matrix
# 
# ```{admonition} Definition: Symmetric matrix
# :class: note
# :name: symmetric-matrix-definition
# 
# A **symmetric matrix** is a square matrix $A$ where $A=A^\mathrm{T}$, i.e.,
# 
# $$[A]_{ij} = [A]_{ji},$$ 
# 
# for all $i$ and $j$. It is called a symmetric matrix because the values of the elements are 'symmetric' about the main diagonal
# 
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{12} & a_{11} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{1n} & a_{2n} & \cdots & a_{nn}
#     \end{pmatrix}
# \end{align*}
# ````
# 
# ````{admonition} Example 1.9
# :class: seealso
# :name: symmetric-matrix-example
# 
# Which of the following matrices are symmetric matrices?
#     
# 
# &emsp; (i) &emsp; $A=\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $B=\begin{pmatrix} 2 & 0 & -3 \\ 0 & 5 & 7 \\ -3 & 7 & 1 \end{pmatrix}$
# 
# &emsp; (iii) &emsp; $C=\begin{pmatrix} 2 & 4 \\ 3 & 2 \end{pmatrix}$
# 
# ```{dropdown} Solution
# 
# &emsp; (i) &emsp; $A=\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ is a symmetric matrix since 
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}^\mathrm{T} = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = A.
# \end{align*}
#         
# &emsp; (ii) &emsp; $B = \begin{pmatrix} 2 & 0 & -3 \\ 0 & 5 & 7 \\ -3 & 7 & 1 \end{pmatrix}$ is a symmetric matrix since 
# 
# \begin{align*}
#     \begin{pmatrix} 2 & 0 & -3 \\ 0 & 5 & 7 \\ -3 & 7 & 1 \end{pmatrix}^\mathrm{T} = \begin{pmatrix} 2 & 0 & -3 \\ 0 & 5 & 7 \\ -3 & 7 & 1 \end{pmatrix} = B.
# \end{align*}
#         
# &emsp; (iii) &emsp; $C = \begin{pmatrix} 2 & 4 \\ 3 & 2 \end{pmatrix}$ is not a symmetric matrix since $[C]_{12} \neq [C]_{21}$. 
# 
# ```
# ````
# 
# ### Python code
# 
# The code below calculates the solution to [example 1.9](symmetric-matrix-example).

# In[3]:


# (i)
A = sym.Matrix([[1, 2], [2, 1]])
print(f"(i) Symmetric: {A == A.T}")

# (ii)
B = sym.Matrix([[2, 0, -3], [0, 5, 7], [-3, 7, 1]])
print(f"(ii) Symmetric: {B == B.T}")

# (iii)
A = sym.Matrix([[2, 4], [3, 2]])
print(f"(iii) Symmetric: {A == A.T}")

