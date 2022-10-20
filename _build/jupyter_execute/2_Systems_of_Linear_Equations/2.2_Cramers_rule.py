#!/usr/bin/env python
# coding: utf-8

# # Cramer's rule
# 
# ```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Gabriel_Cramer.jpg/220px-Gabriel_Cramer.jpg
# ---
# width: 200px
# alt: Gabriel Cramer
# figclass : margin
# ---
# [Gabriel Cramer (1704 - 1752)](https://en.wikipedia.org/wiki/Gabriel_Cramer)
# ```
#      
# **Cramer's rule**, named after Swiss mathematician [Gabriel Cramer](https://en.wikipedia.org/wiki/Gabriel_Cramer), is an explicit rule for calculating the solution to a system of linear equations using determinants. We saw in the section on [determinants](determinant-section) that the solution to the system of linear equations
# 
# \begin{align*}
#     \begin{pmatrix} a & b \\ c & d \end{pmatrix}
#     \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} =
#     \begin{pmatrix} e \\ f \end{pmatrix}
# \end{align*}
# 
# is 
# 
# \begin{align*}
#     x_1 &= \frac{de - bf}{ad - bc}, &
#     x_2 &= \frac{af - ce}{ad - bc}.
# \end{align*}
# 
# We can recognise that the solution to both variables includes the determinant of the coefficient matrix, $ad - bc$, in the denomimator. But what about the numerator? If we consider the solution to $x_1$ then in $de - bf$ we can see that the constant values $e$ and $f$ are included and we have the subtraction of two products which is similar to the determinant of a $2 \times 2$ matrix, i.e.,
# 
# \begin{align*}
#     de - bf = \begin{vmatrix} e & b \\ f & d \end{vmatrix}.
# \end{align*}
# 
# Doing similar for the solution to $x_2$ we see that the numerator is
# 
# \begin{align*}
#     af - ce = \begin{vmatrix} a & e \\ c & f \end{vmatrix}.
# \end{align*}
# 
# These determinants are simply the coefficient matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with first and second columns replaced by the constant vector $\begin{pmatrix} e \\ f \end{pmatrix}$ for $x_1$ and $x_2$ respectively. This can be extended to larger systems to give us Cramer's rule.
# 
# 
# 
# ````{admonition} Theorem: Cramer's rule
# :class: important
# :name: cramers-rule-theorem
# 
# The solution to a non-singular linear system of equations of the form $A\mathbf{x}=\mathbf{b}$ can be calculated using Cramer's rule which is
# 
# ```{math}
# :label: cramers-rule-equation
# 
# x_i = \frac{\det(A_i)}{\det(A)},
# ```
# 
# where $A_i$ is a matrix obtained by replacing column $i$ of $A$ with $\mathbf{b}$.
# 
# ````
# 
# **Proof** (from [Proof Wiki](https://proofwiki.org/wiki/Cramer%27s_Rule))
# 
# *The solution to a system of linear equations $A \mathbf{x} = \mathbf{b}$ can be calculated using $\mathbf{x} = A^{-1} \mathbf{b}$ where $A^{-1}$ is the inverse of the coefficient matrix $A$. The [adjoint-determinant formula](adjoint-determinant-formula-definition) for calculating the inverse is*
# 
# \begin{align*}
#     A^{-1} = \frac{\operatorname{adj}(A)}{\det(A)},
# \end{align*}
# 
# *so*
# 
# \begin{align*}
#     \mathbf{x} =  \frac{1}{\det(A)} \operatorname{adj}(A) \mathbf{b}.
# \end{align*}
# 
# *Since $\operatorname{adj}(A) = C^T$ where $C$ is the matrix of [co-factors](cofactor-definition)*
# 
# \begin{align*}
#     C^T = \begin{pmatrix} 
#         C_{11} & C_{21} & \cdots & C_{n1} \\
#         C_{12} & C_{22} & \cdots & C_{n2} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         C_{1n} & C_{2n} & \cdots & C_{nn}
#     \end{pmatrix}.
# \end{align*}
# 
# *then for the $i$ element of $\mathbf{x}$ using the [definition of matrix multiplication](matrix-multiplication-definition) we have*
# 
# \begin{align*}
#     x_i = \frac{1}{\det(A)} \sum_{j=1}^n C_{ji} b_j
# \end{align*}
# 
# *In Cramer's rule, $A_i$ is the matrix formed by replacing column $i$ of $A$ with $\mathbf{b}$*
# 
# \begin{align*}
#     A_i = \begin{pmatrix}
#         a_{11} & \cdots & a_{1,i-1} & b_1 & a_{1,i+1} & \cdots & a_{1n} \\
#         a_{21} & \cdots & a_{2,i-1} & b_2 & a_{2,i+1} & \cdots & a_{2n} \\
#         \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
#         a_{n1} & \cdots & a_{n,i-1} & b_n & a_{n,i+1} & \cdots & a_{nn}
#     \end{pmatrix}.
# \end{align*}
# 
# *Since removing the $i$th column from both $A$ and $A_i$ (the one with the $b$ values) results in the same matrix then the cofactors of $A_i$ are the same as the cofactors of $A$. If we calculate $\det(A_i)$ by expanding along the $i$th column of $A_i$ then*
# 
# \begin{align*}
#     \det(A_i) = b_1 C_{1i} + b_2 C_{2i} + \cdots + b_n C_{ni} = \sum_{j=1}^n C_{ji} b_j,
# \end{align*}
# 
# *so $x_i = \dfrac{\det(A_i)}{\det(A)}$.*<div style="text-align: right"> &#9633; </div>
# 
# 
# ````{admonition} Example 2.3
# :class: seealso
# :name: cramers-rule-example
# 
# Solve the following systems of linear equations using Cramer's rule
# 
# &emsp; (i) &emsp; $\begin{array}{rl}
#     3x_1 - 2x_2 &= -4, \\
#     x_1 - 3x_2 &= 1.
# \end{array}$
# 
# &emsp; (ii) &emsp; $\begin{array}{rl}
#     -2x_1 - 3x_2 - x_3 &= -5, \\
#     -4x_1 + 4x_2 + 3x_3 &= -20, \\
#     -3x_1 &= -12.
# \end{array}$
# 
# ```{dropdown} Solution
# 
# (i) &emsp; $A = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$
# 
# \begin{align*}
#     x_1 &= \frac{
#     \begin{vmatrix} -4 & -2 \\ 1 & -3 \end{vmatrix}}
#     {\begin{vmatrix} 3 & -2 \\ 1 & -3 \end{vmatrix}} = \frac{14}{-7} = -2,  \\
#     \\
#     x_2 &= \frac{\begin{vmatrix} 3 & -4 \\ 1 & 1 \end{vmatrix}}{-7} = 
#     \frac{7}{-7} = -1.
# \end{align*}
# 
# Check solution:
# 
# \begin{align*}
#     A\mathbf{x} = \begin{pmatrix} 3 & -2 \\ 1 & -3 \end{pmatrix}
#     \begin{pmatrix} -2 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} -4 \\ 1 \end{pmatrix} = \mathbf{b} \qquad \checkmark
# \end{align*}
# 
# (ii) &emsp; $A = \begin{pmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -5 \\ -20 \\ -12 \end{pmatrix}$
# 
# \begin{align*}
#     x_1 &= \frac{
#     \begin{vmatrix}-5 & -3 & -1 \\ -20 & 4 & 3 \\ -12 & 0 & 0 \end{vmatrix}}
#     {\begin{vmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{vmatrix}}
#     = \frac{-12
#     \begin{vmatrix} -3 & -1 \\ 4 & 3 \end{vmatrix}}
#     {-3\begin{vmatrix} -3 & -1 \\ 4 & 3 \end{vmatrix}} \\
#     &= \frac{-12(-5)}{-3(-5)} = \frac{60}{15} = 4,\\ \\
#     x_2 &= \frac{
#     \begin{vmatrix} -2 & -5 & -1 \\ -4 & -20 & 3 \\ -3 & -12 & 0 \end{vmatrix}}{15} 
#     = \frac{-\begin{vmatrix} -4 & -20 \\ -3 & -12 \end{vmatrix} 
#     - 3\begin{vmatrix}-2 & -5 \\ -3 & -12 \end{vmatrix}}{15}  \\
#     &= \frac{12 - 3(9)}{15} = \frac{-15}{15} = -1, \\ \\
#     x_3 &= \frac{
#     \begin{vmatrix} -2 & -3 & - 5 \\ -4 & 4 & -20 \\ -3 & 0 & -12 \end{vmatrix}}{15}
#     =\frac{-3\begin{vmatrix} -3 & -5 \\ 4 & -20 \end{vmatrix} - 
#     12\begin{vmatrix} -2 & -3 \\ -4 & 4 \end{vmatrix}}{15} \\
#     & = \frac{-3(80) - 12(-20)}{15} = \frac{0}{15} = 0.
# \end{align*}
# 
# Check solution:
# 
# \begin{align*}
#     A\mathbf{x} = 
#     \begin{pmatrix} -2 & -3 & -1 \\ -4 & 4 & 3 \\ -3 & 0 & 0 \end{pmatrix}
#     \begin{pmatrix} 4 \\ -1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} -5 \\ -20 \\ -12 \end{pmatrix} = \mathbf{b} \qquad \checkmark
# \end{align*}
# 
# ```
# 
# ````
