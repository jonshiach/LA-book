#!/usr/bin/env python
# coding: utf-8

# (vectors-definition-section)=
# # Definition
# 
# In Euclidean space, a **vector** represents a **displacement** from a point $A$ to a point $B$ ({numref}`vector-figure`). The vector $\overrightarrow{AB}$ is an object that has a **magnitude** (length) and a **direction**. The magnitude of the vector is the distance between the two points and the direction refers to the direction of displacement from $A$ to $B$, with respect to the given Euclidean space. Note that the actual points $A$ and $B$ are not important for the definition of the vector, only the way of getting from $A$ to $B$ is. Pictorially, vectors are represented by arrows. The start of the vector is called the **tail** and the end of the vector is called the **head**.
# 
# ```{figure} ../Images/vector.png
# :name: vector-figure
# 
# The vector $\overrightarrow{AB}$ points from its tail at $A$ to its head at $B$.
# ```
# 
# Vectors in mathematical notation are usually denoted by a single lowercase character. To distinguish vectors from other mathematical objects such as scalars and variables, the character representing a vector is written in boldface when typeset or underlined when written by hand.  Some authors also represent a vector using a small right arrow over the vector name. For example, the following are all valid representations of vectors:
# 
# \begin{align*}
#     \mathbf{a}, \qquad \underline{a}, \qquad \vec{a}.
# \end{align*}
# 
# A vector in $\mathbb{R}^n$ can be represented by an $n$-tuple or a single column matrix
# 
# \begin{align*}
#     \mathbf{a} = (a_1, a_2, \ldots, a_n) = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n\end{pmatrix},
# \end{align*}
# 
# where each coordinate represents the signed difference between the tail and head of the vector in the Cartesian coordinate system. Note we use the same $n$-tuple notation to denote both points and vectors in $\mathbb{R}^n$, however, it should always be clear from the context which we are referring to.
# 
# `````{admonition} Example 3.1
# :class: seealso
# :name: vector-example
# 
# Let $U=(3,-1)$ and $V=(5,0)$ be points in $\mathbb{R}^2$. Determine the vector $\overrightarrow{UV}$.
# 
# ````{dropdown} Solution
# The vector $\overrightarrow{UV}$ is
# \begin{align*}
#     \overrightarrow{UV} = V - U = 
#     \begin{pmatrix}
#         5 \\ 0
#     \end{pmatrix} -
#     \begin{pmatrix}
#         3 \\ -1
#     \end{pmatrix} =
#     \begin{pmatrix}
#         2 \\ 1
#     \end{pmatrix}.
# \end{align*}
# ````
# `````
# 
# Consider the vector $\mathbf{a}$ in $\mathbb{R}^2$ as given in the {numref}`R3-vector-figure`. Here the displacement along the $x$, $y$ and $z$ axes are $a_1$, $a_2$ and $a_3$ respectively, therefore $\mathbf{a} = (a_1, a_2, a_3)$.
# 
# ```{figure} ../Images/R3_vector.png
# :name: R3-vector-figure
# :width: 400
# 
# The vector $\mathbf{a} = (a_1, a_2, a_3)$ in $\mathbb{R}^3$.
# ```
# 
# We use $\mathbf{0}$ to denote the **zero vector** $(0, 0, \ldots, 0)$. This can be thought of as the vector $\overrightarrow{AA}$, for any point $A$. In this chapter we introduce vectors in Euclidean space, therefore the coefficients $a_i$ are necessarily real numbers. In [vector spaces](vector-spaces-chapter) we generalise the notion of a vector and allow its coefficients to be any elements coming from a field.
# 
# (position-vector-section)=
# ## Position vectors
# 
# A **position vector** $\mathbf{p}$ is a vector with tail located at the origin $O$ and head located at a point $P$. So $\mathbf{p} = \overrightarrow{OP}.$
# 
# ```{figure} ../Images/position_vector.png
# :name: position-vector-figure
# 
# The position vector $\mathbf{p}$ points from the origin $O$ to the point $P$.
# ```
# 
# Since $O = (0, 0, \ldots, 0)$, the tuple representing the position vector $\mathbf{p}$ is the same as that representing the co-ordinates of $P$.
# 
# ## Python code
# 
# The SymPy command `Matrix()` can be used to define a vector. If we enter the vector as a row matrix SymPy will treat the vector as a column vector. The following code defines the vector $\mathbf{a} = (1, 2, 3)$.

# In[1]:


import sympy as sym

a = sym.Matrix([1, 2, 3])
display(a)

