#!/usr/bin/env python
# coding: utf-8

# (definition-of-a-matrix-section)=
# # Definition
# 
# A **matrix** (plural **matrices**) is a rectangular array of elements which can be numbers, mathematical expressions, symbols, or even other matrices. Matrices are arranged in rows and columns and enclosed by parentheses (or sometimes square brackets), for example
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 2 & 3 \\
#         4 & 5 & 6
#     \end{pmatrix}.
# \end{align*}
#     
# This matrix contains 6 elements arranged in 2 (horizontal) rows and 3 (vertical) columns.
# 
# ````{admonition} Definition: Dimension of a matrix
# :class: note
# :name: dimension-of-a-matrix-definition
# 
# The dimension or size of a matrix is defined to be **rows** $\times$ **columns**, where 'rows' is the number of horizontal rows and 'columns' the number of vertical columns of said matrix. If rows $=$ columns we say that the matrix is a square matrix.
# \begin{align*}
#     &\,\,\,\begin{matrix} \leftarrow & \!\!\text{columns}\!\! & \rightarrow \end{matrix} \\
#     \begin{matrix} \uparrow \\ \text{rows} \\ \downarrow \end{matrix}
#     &\begin{pmatrix}
#         \square & \square & \cdots & \square \\
#         \square & \square & \cdots & \square \\
#         \vdots & \vdots & \ddots & \vdots \\
#         \square & \square & \cdots & \square
#     \end{pmatrix}
# \end{align*}
# ````
# 
# ````{admonition} Example 1.1
# :class: seealso
# :name: matrix-dimension-example
# 
# Determine the dimensions of the following matrices:
# 
# &emsp; (i) &emsp; $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# 
# &emsp; (ii) &emsp; $B = \begin{pmatrix} a & b \\ c & d \\ e & f \end{pmatrix}$
# 
# &emsp; (iii) &emsp; $C = \begin{pmatrix} \sin(x) & \ln(x) & \cos(x+1) \end{pmatrix}$
# 
# &emsp; (iv) &emsp; $D = \begin{pmatrix} 0 \end{pmatrix}$
# 
# ```{dropdown} Solution
# 
# &emsp; (i) &emsp; $2\times 2 $
# 
# &emsp; (ii) &emsp; $3\times 2$
# 
# &emsp; (iii) &emsp; $1 \times 3$
# 
# &emsp; (iv) &emsp; $1 \times 1$
# ```
# ````
# 
# ## Python code
# 
# To define and perform operations on matrices in Python we can use the [SymPy](https://www.sympy.org/en/index.html) library (short for *symbolic Python*) library. A matrix can then be defined using the `sym.Matrix` command, for example

# In[1]:


import sympy as sym

A = sym.Matrix([[1, 2], [3, 4]])
display(A)


# Note that the matrix is defined using square brackets and each row is contained within another pair of square brackets. Commas separate elements in the same row and the different rows of a matrix. 
# 
# The command for determining the number of rows and columns of a matrix `A` is `A.shape` which returns a 2-tuple containing. The following code defines the matrix $A$ from [example 1.1](matrix-dimension-example) and outputs its dimensions

# In[2]:


nrows, ncols = A.shape
print(f"The matrix A is an {nrows} x {ncols} matrix")


# (indexing-a-matrix-section)=
# ## Indexing a matrix
# 
# Matrices are typically labeled using uppercase characters (e.g. $A$) and the elements of a matrix are labeled with the corresponding lowercase character (e.g. $a$). Individual entries of a matrix are **indexed** using two subscript indices: $a_{ij}$ where $i$ corresponds to the row number reading from top to bottom and $j$ is the column number reading from left to right. 
# 
# For example, let $A$ be an $m\times n$ matrix then
# 
# $$A = \begin{pmatrix}
#   a_{11} & a_{12} & \cdots & a_{1n} \\
#   a_{21} & a_{22} & \cdots & a_{2n} \\
#   \vdots & \vdots & \ddots & \vdots \\
#   a_{m1} & a_{m2} & \cdots & a_{mn} 
# \end{pmatrix}.$$
# 
# Some alternate notation includes
# 
# $$a_{ij} = [A]_{ij} = A[i,j].$$
# 
# `````{admonition} Example 1.2
# :class: seealso
# :name: matrix-indexing-example
# 
# Given the matrix 
# $A = \begin{pmatrix}
#     2 & 0 & -3 \\
#     1 & 7 & 4 
# \end{pmatrix},$ 
# 
# write down the following elements:
# 
# &emsp; (i) &emsp; $a_{11}$
# 
# &emsp; (ii) &emsp; $a_{13}$
# 
# &emsp; (iii) &emsp; $[A]_{21}$
# 
# &emsp; (iv) &emsp; $A[2,2]$
# 
# ````{dropdown} Solution
# 
# &emsp; (i)  &emsp; $a_{11} = 2$
# 
# &emsp; (ii) &emsp; $a_{13} = -3$
# 
# &emsp; (iii) &emsp; $[A]_{21} = 1$
# 
# &emsp; (iv) &emsp; $A[2,2] = 7$
#     
# ````
# `````
# 
# ### Python code
# 
# Matrices and arrays in Python are indexed using the syntax `A[i,j]` which returns the value of the element in row `i` and column `j`. 
# 
# ```{important}
# Python is a **zero indexing** language which means indexing starts at zero. So to index the element $a_{23}$ we would use `a[1,2]` i.e., remember to subtract 1 from the indices.
# ```
# 
# The following code defines the matrix $A$ from [example 1.2](matrix-indexing-example) and outputs the values of the indexed elements. 

# In[3]:


A = sym.Matrix([[2, 0, -3], [1, 7, 4]])
display(A)

print(f"(i)   a_11 = {A[0,0]}")
print(f"(ii)  a_13 = {A[0,2]}")
print(f"(iii) [A]_21 = {A[1,0]}")
print(f"(iv)  A[2,2] = {A[1,1]}")

