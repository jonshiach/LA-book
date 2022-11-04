#!/usr/bin/env python
# coding: utf-8

# (basic-arithmetic-operations-section)=
# # Basic arithmetic operations
# 
# So far, we have given a fancy name to a rectangular array of objects and showed how we can index its elements. Now we are going to fully develop an algebra for matrices. A system, where there are operations of addition and multiplication and necessarily rules that accompany them. This system resembles that of real numbers but we will see some differences and new concepts. For simplicity, we are going to assume that the entries of our matrices are numbers, however the developed theory applies to a broader range of objects.
# 
# ## Matrix equality
# 
# ````{admonition} Definition: Matrix equality 
# :class: note
# :name: matrix-equality-definition
# 
# We say that an $m \times n$ matrix $A$ and an $p \times q$ matrix $B$ are **equal** and write $A = B$ if and only if **both** of the following conditions are satisfied:
# 
# - they have the same dimensions, in other words $m = p$ and $n = q$;
# - for all $1 \leq i \leq m$ and $1 \leq j \leq n$, $a_{ij} = b_{ij}$.
# ````
# 
# For example, consider the following matrices
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, &
#     B &= \begin{pmatrix} 1 & 2 & 5 \\ 3 & 4 & 6 \end{pmatrix}, &
#     C &= \begin{pmatrix} 3^0 & \sqrt{4} \\ 1 + 2 & 2^2 \end{pmatrix}.
# \end{align*}
# 
# Here $A \neq B$ since $A$ has 2 columns and $B$ has 3 columns. However, $A=C$ because both $A$ and $C$ have the same number of rows and columns and all of the corresponding elements are equal.
# 
# ### Python code
# 
# To determine whether two SymPy matrices are equal we use the `==` operator.

# In[1]:


import sympy as sym

A = sym.Matrix([[1, 2], [3, 4]])
B = sym.Matrix([[1, 2, 5], [3, 4, 6]])
C = sym.Matrix([[3 ** 0, sym.sqrt(4)], [1 + 2, 2 ** 2]])

AequalB = A == B
AequalC = A == C
BequalC = B == C
print(f"A = B: {AequalB}")
print(f"A = C: {AequalC}")
print(f"B = C: {BequalC}")


# (matrix-addition-section)=
# ## Matrix addition
# 
# ````{admonition} Definition: Matrix addition and subtraction 
# :class: note
# :name: matrix-addition-definition
# 
# Let $A$ and $B$ be two $m \times n$ matrices. The addition or subtraction of two $m \times n$ matrices $A$ and $B$ is an $m \times n$ matrix $A \pm B$ defined by:
# 
# $$[A \pm B]_{ij} = a_{ij} \pm b_{ij},$$
#     
# where $1 \leq i \leq m$ and $1 \leq j \leq n$.
# \begin{align*}
#     \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn}
#     \end{pmatrix} \pm 
#     \begin{pmatrix}
#         b_{11} & b_{12} & \cdots & b_{1n} \\
#         b_{21} & b_{22} & \cdots & b_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         b_{m1} & b_{m2} & \cdots & b_{mn}
#     \end{pmatrix} \\
#     =
#     \begin{pmatrix}
#         a_{11} \pm b_{11} & a_{12} \pm b_{12} & \cdots & a_{1n} \pm b_{1n} \\
#         a_{21} \pm b_{21} & a_{22} \pm b_{22} & \cdots & a_{2n} \pm a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} \pm b_{m1} & a_{m2} \pm b_{m2} & \cdots & a_{mn} \pm b_{mn}
#     \end{pmatrix}.
# \end{align*}
# ````
# 
# The addition and subtraction of two matrices of different sizes is **not defined**.
# 
# ````{admonition} Theorem: Properties of matrix addition
# :class: important
# :name: properties-of-matrix-addition-theorem
# 
# For all $m \times n$ matrices $A,B$ and $C$, the following conditions are satisfied:
# 
# - matrix addition is commutative, i.e., $A + B = B + A$;
# - matrix addition is associative, i.e., $A + (B + C) = (A + B) + C$.
# ````
# 
# `````{admonition} Example 1.3
# :class: seealso
# :name: matrix-addition-example
# 
# Evaluate the following:
# 
# &emsp; (i) &emsp; $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} - \begin{pmatrix} 7 \\ -11 \\ -13 \end{pmatrix}$
# 
# &emsp; (iii) &emsp; $\begin{pmatrix} 1 & 3 & 5 \\ 7 & 9 & 11 \end{pmatrix} + \begin{pmatrix}2 & 3 \\ 5 & 7 \end{pmatrix}$
# 
# 
# ````{dropdown} Solution
# 
# &emsp; (i) &emsp; $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1 + 5 & 2 + 6 \\ 3 + 7 & 4 + 8 \end{pmatrix}= \begin{pmatrix}6 & 8 \\ 10 & 12 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} - \begin{pmatrix} 7 \\ -11 \\ -13 \end{pmatrix} = \begin{pmatrix}2 - 7 \\ 3 + 11 \\ 5 + 13 \end{pmatrix} = \begin{pmatrix} -5 \\ 14 \\ 18\end{pmatrix}$
# 
# &emsp; (iii) &emsp; undefined since the left matrix is $2\times 3$ and the right matrix is $2\times 2$
# ````
# `````
# 
# ### Python code
# 
# The Python command for calculating the sum of two matrices `A` and `B` is simply `A + B`. The Python code below calculates the solution to question &emsp; (i) from [example 1.3](matrix-addition-example).

# In[2]:


A = sym.Matrix([[1, 2], [3, 4]])
B = sym.Matrix([[5, 6], [7, 8]])

AplusB = A + B
display(AplusB)


# (scalar-multiplication-of-matrices)=
# ## Scalar multiplication of matrices
# 
# ````{admonition} Definition: Scalar multiplication 
# :class: note
# :name: scalar-multiplication-of-a-matrix-definition
# 
# The scalar multiplication of an $m \times n$ matrix by a scalar is calculated by multiplying each element in the matrix by the scalar
# 
# \begin{align*}
#     k[A]_{ij} = ka_{ij}, \qquad i = 1, \ldots, m, \quad j = 1, \ldots, n.
# \end{align*}
# 
# \begin{align*}
#     k \begin{pmatrix}
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{m1} & a_{m2} & \cdots & a_{mn}
#     \end{pmatrix} = 
#     \begin{pmatrix}
#         ka_{11} & ka_{12} & \cdots & ka_{1n} \\
#         ka_{21} & ka_{22} & \cdots & ka_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         ka_{m1} & ka_{m2} & \cdots & ka_{mn}
#     \end{pmatrix}
# \end{align*}
# ````
# 
# ````{admonition} Theorem: Properties of scalar multiplication of matrices
# :class: important
# :name: properties-of-scalar-multiplication-of-matrices-theorem
# 
# Let $A$ and $B$ be two $m \times n$ matrices and $k$ and $\ell$ are scalars, then
# 
# - scalar multiplication is commutative: $kA=Ak$;
# - scalar multiplication is distributive over matrix addition: $k(A + B) = kA + kB$;
# - scalar multiplication is distributive over scalar addition: $(k+\ell)A = kA + \ell A$;
# - scalar multiplication is associative: $k(\ell A) = (k \ell)A$;
# - multiplication by $-1$ gives the additive inverse: $(-1)A = -A$.
# 
# ````
# 
# `````{admonition} Example 1.4
# :class: seealso
# :name: scalar-multiplication-of-matrices-example
# 
# Evaluate the following:
# 
# 
# &emsp; (i) &emsp; $2 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $\dfrac{1}{2} \begin{pmatrix} 0 & -1 \\ 3 & 2 \\ 4 & -2 \end{pmatrix}$
# 
# &emsp; (iii) &emsp; $\dfrac{1}{3} \begin{pmatrix}1 & 6 & 4 \\ 0 & 3 & -1 \end{pmatrix}$
# 
# &emsp; (iv) &emsp; $101 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - 99 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$
# 
# ````{dropdown} Solution
# 
# &emsp; (i) &emsp; $2 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix}2 & 4 \\ 6 & 8 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $\dfrac{1}{2} \begin{pmatrix} 0 & -1 \\ 3 & 2 \\ 4 & -2 \end{pmatrix} =  \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{3}{2} & 1 \\ 2 & -1 \end{pmatrix}$
# 
# &emsp; (iii) &emsp; $\dfrac{1}{3} \begin{pmatrix}1 & 6 & 4 \\ 0 & 3 & -1 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} & 2 & \frac{4}{3} \\ 0 & 1 & -\frac{1}{3} \end{pmatrix}$
# 
# &emsp; (iv) &emsp; $101\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - 99 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = 2 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} =  \begin{pmatrix} 2 & 4 \\ 0 & 2 \end{pmatrix}$
# 
# ````
# `````
# 
# ### Python code
# 
# The command for multiplying a SymPy matrix `A` by a scalar `k` is simply `k * A`. The following code calculates the solutions [example 1.4](scalar-multiplication-of-matrices-example).

# In[3]:


# (i)
A = sym.Matrix([[1, 2], [3, 4]])
print("(i)")
display(2 * A)

# (ii)
B = sym.Matrix([[0, -1], [3, 2], [4, -2]])
print("(ii)")
display(B / 2)

# (iii)
C = sym.Matrix([[1, 6, 4], [0, 3, -1]])
print("(iii)")
display(1/3 * C)

# (iv)
D = sym.Matrix([[1, 2], [0, 1]])
print("(iv)")
display(101 * D - 99 * D)

