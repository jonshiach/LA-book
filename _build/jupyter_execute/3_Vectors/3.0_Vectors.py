#!/usr/bin/env python
# coding: utf-8

# (vectors-chapter)=
# # Vectors
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - define a [vector](vectors-section) in $\mathbb{R}^n$ Euclidean space, calculate its [magnitude](magnitude-definition) and parallel [unit vector](normalising-a-vector-proposition);
# - perform the arithmetic operations of [vector addition](vector-addition-definition), [multiplication by a scalar](scalar-multiplication-of-a-vector-definition), [dot product](dot-product-definition) and [cross product](cross-product-definition);
# - express a vector as a [linear combination of vectors](linear-combination-of-vectors-definition).
# ---
# 
# 
# (euclidean-space-section)=
# ## Euclidean space
# 
# Before we discuss vectors it is useful to first define [**Euclidean space**](https://en.wikipedia.org/wiki/Euclidean_space) which is the mathematical system which vectors are most commonly applied. Attributed to the Greek mathematician [Euclid](https://en.wikipedia.org/wiki/Euclid_of_Megara), Euclidean space is a representation of physical space where the position of a point in the space can be described by the signed distance along perpendicular real numbers lines called **axes** (singular: axis). 
# 
# An $n$-dimensional Euclidean space is defined by $n$ perpendicular real axes and is referred to as $\mathbb{R}^n$. For example, consider the diagram of $\mathbb{R}^3$ in {numref}`R3-figure`. Here we have a representation of a 3-dimensional Euclidean space defined by the 3 axes labelled $x$, $y$ and $z$. This representation uses the [**right-hand rule**](https://en.wikipedia.org/wiki/Right-hand_rule) so-called because if we use the thumb on our right hand to represent the $x$ axis, the index finger for the $y$ axis and the middle finger for the $z$ axis then holding out the right hand palm up with the thumb and index finger at right-angles and the middle finger pointing up then we have the axis configuration shown in {numref}`R3-figure`. Doing similar with the left hand gives the **left-hand rule** where the $x$ axis is pointing in the opposite direction than in the right-hand rule. 
# 
# :::{figure} ../Images/R3.png
# :name: R3-figure
# 
# The position of a point in $\mathbb{R}^3$ can be defined by its co-ordinates $(x, y, z)$.
# :::
# 
# The position of a point in Euclidean space can be defined by its **co-ordinates** which is an ordered set known as a **tuple** where each element contains the signed distances along each axis, e.g., $(x, y, z)$ where $x, y, z \in \mathbb{R}$. 
# 
# (vectors-section)=
# ## Vectors
# 
# In Euclidean space, a **vector** represents a **displacement** from a point $A$ to a point $B$ ({numref}`vector-figure`). The vector $\overrightarrow{AB}$ is an object that has a **magnitude** (length) and a **direction**. The magnitude of the vector is the distance between the two points and the direction refers to the direction of displacement from $A$ to $B$, with respect to the given Euclidean space. Note that the actual points $A$ and $B$ are not important for the definition of the vector, only the way of getting from $A$ to $B$ is. Pictorially, vectors are represented by arrows. The start of the vector is called the **tail** and the end of the vector is called the **head**.
# 
# :::{figure} ../Images/vector.png
# :name: vector-figure
# 
# The vector $\overrightarrow{AB}$ points from its tail at $A$ to its head at $B$.
# :::
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
# :::::{admonition} Example 3.1
# :class: seealso
# :name: vector-example
# 
# Let $U=(3,-1)$ and $V=(5,0)$ be points in $\mathbb{R}^2$. Determine the vector $\overrightarrow{UV}$.
# 
# ::::{dropdown} Solution
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
# ::::
# :::::
# 
# Consider the vector $\mathbf{a}$ in $\mathbb{R}^2$ as given in the {numref}`R3-vector-figure`. Here the displacement along the $x$, $y$ and $z$ axes are $a_1$, $a_2$ and $a_3$ respectively, therefore $\mathbf{a} = (a_1, a_2, a_3)$.
# 
# :::{figure} ../Images/R3_vector.png
# :name: R3-vector-figure
# :width: 400
# 
# The vector $\mathbf{a} = (a_1, a_2, a_3)$ in $\mathbb{R}^3$.
# :::
# 
# We use $\mathbf{0}$ to denote the **zero vector** $(0, 0, \ldots, 0)$. This can be thought of as the vector $\overrightarrow{AA}$, for any point $A$. In this chapter we introduce vectors in Euclidean space, therefore the coefficients $a_i$ are necessarily real numbers. In [vector spaces](vector-spaces-chapter) we generalise the notion of a vector and allow its coefficients to be any elements coming from a field.
# 
# (position-vector-section)=
# ## Position vectors
# 
# A **position vector** $\mathbf{p}$ is a vector with tail located at the origin $O$ and head located at a point $P$. So $\mathbf{p} = \overrightarrow{OP}.$
# 
# :::{figure} ../Images/position_vector.png
# :name: position-vector-figure
# 
# The position vector $\mathbf{p}$ points from the origin $O$ to the point $P$.
# :::
# 
# Since $O = (0, 0, \ldots, 0)$, the tuple representing the position vector $\mathbf{p}$ is the same as that representing the co-ordinates of $P$.
# 
# ## Python code
# 
# The SymPy command `Matrix()` can be used to define a vector. If we enter the vector as a row matrix SymPy will treat the vector as a column vector. The following code defines the vector $\mathbf{a} = (1, 2, 3)$.

# In[1]:


from sympy import *

a = Matrix([1, 2, 3])
display(a)

