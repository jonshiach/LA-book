#!/usr/bin/env python
# coding: utf-8

# 
# # Matrices
# 
# 
# <span style="font-size:20pt;">Examples</span>
# 
# ``````{div} full-width
# 
# - **Dimension of a matrix: $\text{no. rows} \times \text{no. columns}$**
# 
# ````{admonition} Example 1.1
# :class: seealso
# :name: matrix-dimension-example
# 
# Determine the dimensions of the following matrices:
# 
# &emsp; (i) &emsp; $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# &emsp; (ii) &emsp; $B = \begin{pmatrix} a & b \\ c & d \\ e & f \end{pmatrix}$
# &emsp; (iii) &emsp; $C = \begin{pmatrix} \sin(x) & \ln(x) & \cos(x+1) \end{pmatrix}$
# &emsp; (iv) &emsp; $D = \begin{pmatrix} 0 \end{pmatrix}$
# ````
# 
# - **Matrix indexing:** $a_{ij} = \text{element in row }i\text{ and column }j$
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
# &emsp; (ii) &emsp; $a_{13}$
# &emsp; (iii) &emsp; $[A]_{21}$
# &emsp; (iv) &emsp; $A[2,2]$
# `````
# 
# - **Matrix addition/subtraction:** $[A \pm B]_{ij} = a_{ij} \pm b_{ij}$
# 
# ````{admonition} Example 1.3
# :class: seealso
# :name: matrix-addition-example
# 
# Evaluate the following:
# 
# &emsp; (i) &emsp; $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$
# &emsp; (ii) &emsp; $\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix} - \begin{pmatrix} 7 \\ -11 \\ -13 \end{pmatrix}$
# &emsp; (iii) &emsp; $\begin{pmatrix} 1 & 3 & 5 \\ 7 & 9 & 11 \end{pmatrix} + \begin{pmatrix}2 & 3 \\ 5 & 7 \end{pmatrix}$
# ````
# 
# - **Scalar multiplication of a matrix:** $[kA]_{ij} = ka_{ij}$
# 
# `````{admonition} Example 1.4
# :class: seealso
# :name: scalar-multiplication-of-matrices-example
# 
# Evaluate the following:
# 
# &emsp; (i) &emsp; $2 \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$
# &emsp; (ii) &emsp; $\dfrac{1}{2} \begin{pmatrix} 0 & -1 \\ 3 & 2 \\ 4 & -2 \end{pmatrix}$
# &emsp; (iii) &emsp; $\dfrac{1}{3} \begin{pmatrix}1 & 6 & 4 \\ 0 & 3 & -1 \end{pmatrix}$
# &emsp; (iv) &emsp; $101 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} - 99 \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$
# `````
# 
# - **Matrix multiplication:** $[AB]_{ij} = \displaystyle\sum_{k=1}^p a_{ik}b_{kj}$ where $p$ is the number of columns in $A$ and the number of rows in $B$
# 
# ````{admonition} Example 1.5
# :class: seealso
# :name: matrix-multiplication-example
# 
# Given the matrices
# \begin{align*}
#     A &= \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}, &
#     B &= \begin{pmatrix} 2 & 3 \\ 1 & 5 \end{pmatrix}, &
#     C &= \begin{pmatrix} 1 & 1 & 0 \\ 3 & -2 & 1 \end{pmatrix}, &
#     D &= \begin{pmatrix} 1 \\ 3 \end{pmatrix}.
# \end{align*}
# 
# calculate the following (where possible):
# 
# &emsp; (i) &emsp; $AB$
# &emsp; (ii) &emsp; $BC$
# &emsp; (iii) &emsp; $CD$
# ````
# 
# ````{admonition} Example 1.6
# :class: seealso
# :name: matrix-exponents-example
# 
# Given the matrix 
# $
#     A = \begin{pmatrix} 1 & 0 \\ 3 & 2 \end{pmatrix},
# $
# evaluate:
# 
# &emsp; (i) &emsp; $A^2$
# &emsp; (ii) &emsp; $A^3$
# &emsp; (iii) &emsp; $A^5$
# 
# ````
# 
# - **Transpose of a matrix:** $[A^\mathrm{T}]_{ij}=a_{ji}$
# 
# ````{admonition} Example 1.7
# :class: seealso
# :name: matrix-transpose-example
# 
# Evaluate the following:
# 
# &emsp; (i) &emsp; $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}^\mathrm{T}$
# &emsp; (ii) &emsp; $\begin{pmatrix} 1 & 0 & -2 \\ 3 & -4 & 1 \end{pmatrix}^\mathrm{T}$
# &emsp; (iii) &emsp; $\begin{pmatrix}2 & 3 & 5 \end{pmatrix}^\mathrm{T}$
# 
# ````
# 
# - **Identity matrix:** $[I]_{ij} = \begin{cases} 1 & i = j, \\ 0 & \text{elsewhere} \end{cases}$
# 
# ````{admonition} Example 1.8
# :class: seealso
# :name: identity-matrix-example
# 
# Given the matrices $A = \begin{pmatrix} 1 & 0 \\ -2 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 2 \\ 4 & 3 \\ -2 & 1 \end{pmatrix}$ evaluate:
# 
# 
# &emsp; (i) &emsp; $IA$
# &emsp; (ii) &emsp; $AI$
# &emsp; (iii) &emsp; $IB$
# 
# ````
# 
# - **Symmetric matrix:** $[A]_{ij} = [A]_{ji}$
# 
# ````{admonition} Example 1.9
# :class: seealso
# :name: symmetric-matrix-example
# 
# Which of the following matrices are symmetric matrices?
#     
# &emsp; (i) &emsp; $A=\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$
# &emsp; (ii) &emsp; $B=\begin{pmatrix} 2 & 0 & -3 \\ 0 & 5 & 7 \\ -3 & 7 & 1 \end{pmatrix}$
# &emsp; (iii) &emsp; $C=\begin{pmatrix} 2 & 4 \\ 3 & 2 \end{pmatrix}$
# ````
# 
# - **Determinant of a $2\times 2$ matrix:** $\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$
# 
# ````{admonition} Example 1.10
# :class: seealso
# :name: 2x2-determinant-example
# 
# Calculate the following determinants
# 
# &emsp; (i) &emsp; $\begin{vmatrix} 5 & 2 \\ 3 & 4 \end{vmatrix}$
# &emsp; (ii) &emsp; $\det \begin{pmatrix} a & b \\ ka & kb \end{pmatrix}$
# &emsp; (iii) &emsp; $\begin{vmatrix} 5 & 0 \\ 0 & 2 \end{vmatrix}$
# 
# ````
# 
# - **Minor:** $M_{ij} = $ the determinant of the matrix formed by omitting row $i$ and column $j$
# ````{admonition} Example 1.11
# :class: seealso
# :name: minor-example
# 
# Given the matrix $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix},$ calculate:
# 
# &emsp; (i) &emsp; $M_{11}$
# &emsp; (ii) &emsp; $M_{12}$
# &emsp; (iii) &emsp; $M_{13}$
# ````
# 
# - **Cofactor:** $C_{ij} = (-1)^{i+j}M_{ij}$
# - **Determinant of an $n\times n$ matrix:** $\det(A) = \displaystyle\sum_{i=1}^n a_{ik} C_{ik} = \displaystyle\sum_{j=1}^n a_{kj} C_{kj}$
# 
# ````{admonition} Example 1.12
# :class: seealso
# :name: nxn-determinant-example
# 
# Calculate the determinant of the matrix 
# 
# \begin{align*}
#     \begin{pmatrix} 1 & 0 & 4 \\ 2 & 5 & 6 \\ 4 & 5 & 2 \end{pmatrix},
# \end{align*}
# 
# by expanding along:
# 
# &emsp; (i) &emsp; row 1
# &emsp; (ii) &emsp; column 3
# 
# ````
# 
# ````{admonition} Example 1.13
# :class: seealso
# :name: 4x4-determinant-example
# 
# Calculate the determinant of the $4\times 4$ matrix 
#    
# $$\begin{pmatrix} 1 & -1 & 4 & 3 \\ 2 & 0 & 5 & -3 \\ 1 & 2 & 4 & 5 \\ 2 & 0 & -2 & 4 \end{pmatrix}.$$
# ````
# 
# - **Inverse matrix:** $A^{-1}$ such that $A^{-1}A = AA^{-1} = I$
# 
# ````{admonition} Example 1.14
# :class: seealso
# :name: inverse-matrix-example-1
# 
# Given the two matrices
# $A = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ and
# $B = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix},$ 
# show that $B$ is the inverse of $A$. 
# ````
# 
# - **Adjoint of a matrix:** $[\operatorname{adj}(A)]_{ij} = (-1)^{i+j}M_{ij}$
# 
# ````{admonition} Example 1.15
# :class: seealso
# :name: adjoint-example
# 
# Calculate the adjoint of the following matrices:
# 
# &emsp; (i) &emsp; $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$
# &emsp; (ii) &emsp; $\begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$
# &emsp; (iii) &emsp; $\begin{pmatrix} 1 & 0 & 3 \\ 4 & -2 & 1 \\ 2 & 1 & 3 \end{pmatrix}$
# 
# ````
# 
# - **Adjoint-determinant formula:** $A^{-1} = \dfrac{\operatorname{adj}(A)}{\det(A)}$
# 
# ````{admonition} Example 1.16
# :class: seealso
# :name: matrix-inverse-example-2
# 
# Calculate the inverses of the following matrices if they exist:
# 
# &emsp; (i) &emsp; $A = \begin{pmatrix}1 & 0 \\ 3 & 2\end{pmatrix}$
# &emsp; (ii) &emsp; $B = \begin{pmatrix} 1 & 2 & 0 \\ -2 & 1 & 1 \\ 1 & 0 & 3 \end{pmatrix}$
# &emsp; (iii) &emsp; $C = \begin{pmatrix}1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$
# 
# ````
# 
# ````{admonition} Example 1.17
# :class: seealso
# :name: matrix-algebra-example
# 
# Solve the following matrix equations for $X$:
# 
# &emsp; (i) &emsp; $2X = A$
# &emsp; (ii) &emsp; $kX + A = I$
# &emsp; (iii) &emsp; $A(X + B) = C$
# 
# ````
# 
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# `````{admonition} Exercise 1.1
# :class: note
# :name: ex1.1
# 
# Write down the $3 \times 3$ matrix $A$ whose entries are given by $a_{ij} = i+j.$
# `````
# 
# `````{admonition} Exercise 1.2
# :class: note
# :name: ex1.2
# 
# Write down the $4 \times 4$ matrix $B$ whose entries are given by $b_{ij} = (-1)^{i+j}.$
# `````
# 
# `````{admonition} Exercise 1.3
# :class: note
# :name: ex1.3
# 
# Write down the $4 \times 4$ matrix $C$ whose entries are given by 
# \begin{align*}
#     c_{ij} = 
#     \begin{cases}
#     -1, & i>j, \\
#     0, & i=j, \\
#     1, & i<j. \\
#     \end{cases}
# \end{align*}
# `````
# 
# `````{admonition} Exercise 1.4
# :class: note
# :name: ex1.4
# 
# Given the matrices
# \begin{align*}
#     A &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}, &
#     B &= \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix}, &
#     C &= \begin{pmatrix} 5 \\ 9 \end{pmatrix}, &
#     D &= \begin{pmatrix} 1 & 1 & 3 \\ 4 & -2 & 3 \end{pmatrix}, \\
#     E &= \begin{pmatrix} 1 & 2 \\ 0 & 6 \\ -2 & 3 \end{pmatrix} &
#     F &= \begin{pmatrix} 1 & -2 & 4 \end{pmatrix}, &
#     G &= \begin{pmatrix} 4 & 2 & 3 \\ -2 & 6 & 0 \\ 0 & 7 & 1 \end{pmatrix}, &
#     H &= \begin{pmatrix} 1 & 0 & 1 \\ 5 & 2 & -2 \\ 2 & -3 & 4 \end{pmatrix}.
# \end{align*}
# 
# Calculate the following where possible:
# 
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 2
# (a) &emsp; $A + B$
# ```
# 
# ```{grid-item}
# :columns: 2
# (b) &emsp; $B + C$
# ```
# 
# ```{grid-item}
# :columns: 2
# (c) &emsp; $A^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (d) &emsp; $C^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (e) &emsp; $D + E^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (f) &emsp; $3B - A$
# ```
# 
# ```{grid-item}
# :columns: 2
# (g) &emsp; $E + F^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (h) &emsp; $(F^\mathrm{T})^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (i) &emsp; $2(G + H)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (j) &emsp; $A^\mathrm{T} + B^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (k) &emsp; $(A + B)^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (l) &emsp; $-G$
# ```
# ````
# `````
# 
# `````{admonition} Exercise 1.5
# :class: note
# :name: ex1.5
# 
# Using the matrices from [exercise 1.4](ex1.4) calculate the following where possible:
# 
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 2
# (a) &emsp;  $AB$
# ```
# 
# ```{grid-item}
# :columns: 2
# (b) &emsp;  $BA$
# ```
# 
# ```{grid-item}
# :columns: 2
# (c) &emsp;  $AC$
# ```
# 
# ```{grid-item}
# :columns: 2
# (d) &emsp;  $CA$
# ```
# 
# ```{grid-item}
# :columns: 2
# (e) &emsp;  $C^\mathrm{T}C$
# ```
# 
# ```{grid-item}
# :columns: 2
# (f) &emsp;  $CC^\mathrm{T}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (g) &emsp;  $DE$
# ```
# 
# ```{grid-item}
# :columns: 2
# (h) &emsp;  $GH$
# ```
# 
# ```{grid-item}
# :columns: 2
# (i) &emsp;  $A(DE)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (j) &emsp;  $(AD)E$
# ```
# 
# ```{grid-item}
# :columns: 2
# (k) &emsp;  $A^3$
# ```
# 
# ```{grid-item}
# :columns: 2
# (l) &emsp;  $G^4$
# ```
# ````
# `````
# 
# `````{admonition} Exercise 1.6
# :class: note
# :name: ex1.6
# 
# Using the matrices from [exercise 1.4](ex1.4) calculate the following:
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 2
# (a) &emsp;  $\det(A)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (b) &emsp;  $|B|$
# ```
# 
# ```{grid-item}
# :columns: 2
# (c) &emsp;  $\det(3A)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (d) &emsp;  $\det(G)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (e) &emsp;  $\operatorname{adj}(B)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (f) &emsp;  $\operatorname{adj}(H)$
# ```
# 
# ```{grid-item}
# :columns: 2
# (g) &emsp;  $A^{-1}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (h) &emsp;  $B^{-1}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (i) &emsp;  $G^{-1}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (j) &emsp;  $(AB)^{-1}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (k) &emsp;  $B^{-1}A^{-1}$
# ```
# 
# ```{grid-item}
# :columns: 2
# (l) &emsp;  $(DE)^{-1}$
# ```
# ````
# `````
# 
# `````{admonition} Exercise 1.7
# :class: note
# :name: ex1.7
# 
# Using [the properties of determinants](properties-of-determinants-theorem) and solutions from [exercise 1.6](ex1.6) where necessary, find the determinants for the following matrices.
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 3
# (a) &emsp;  $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (b) &emsp;  $\begin{pmatrix} 4 & 2 \\ 1 & -3 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (c) &emsp;  $\begin{pmatrix} 1 & 0 \\ -1 & 0 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (d) &emsp;  $\begin{pmatrix} 4 & 2 & 3 \\ -4 & 12 & 0 \\ 0 & 7 & 1 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (e) &emsp;  $\begin{pmatrix} 1 & 2 & 3 \\ -1 & -2 & -3 \\ 2 & 4 & 4 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (f) &emsp;  $\begin{pmatrix} 1 & 2 & 1 \\ -3 & -6 & 1 \\ 2 & 4 & 4 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (g) &emsp;  $\begin{pmatrix} 1 & 2 & 3 \\ -1 & -2 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
# ```
# 
# ```{grid-item}
# :columns: 3
# (h) &emsp;  $\begin{pmatrix} 3 & 6 \\ -1 & 3 \end{pmatrix}$
# ```
# ````
# `````
# 
# ````{admonition} Exercise 1.8
# :class: note
# :name: ex1.8
# 
# Prove that adding a multiple of a row or column to another row or column does not change the value of the determinant for a $2\times 2$ matrix.
# 
# ````
# 
# `````{admonition} Exercise 1.9
# Given the matrices
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & -3 \\ 4 & 2 \end{pmatrix}, &
#     B &= \begin{pmatrix} 3 & 0 \\ -1 & 5 \end{pmatrix},
# \end{align*}
# 
# solve the following equations for $X$.
# 
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 3
# (a) &emsp; $5X = A$
# ```
# 
# ```{grid-item}
# :columns: 3
# (b) &emsp; $X + A = I$
# ```
# 
# ```{grid-item}
# :columns: 3
# (c) &emsp; $2X - B = A$
# ```
# 
# ```{grid-item}
# :columns: 3
# (d) &emsp; $XA = I$
# ```
# 
# ```{grid-item}
# :columns: 3
# (e) &emsp; $BX = A$
# ```
# 
# ```{grid-item}
# :columns: 3
# (f) &emsp; $A^2 = X$
# ```
# 
# ```{grid-item}
# :columns: 3
# (g) &emsp; $X^2 = B$
# ```
# 
# ```{grid-item}
# :columns: 3
# (h) &emsp; $(X + A)B = I$
# ```
# ````
# 
# `````
# 
# `````{admonition} Exercise 1.10
# :class: note
# :name: ex1.10
# 
# Use Python and SymPy to calculate the solutions to exercises [1.4](ex1.4) to [1.6](ex1.6).
# 
# `````
# 
# ``````
# 
