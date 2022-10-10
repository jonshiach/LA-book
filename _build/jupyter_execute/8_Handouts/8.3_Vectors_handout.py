#!/usr/bin/env python
# coding: utf-8

# # Vectors
# 
# ``````{div} full-width
# 
# <span style="font-size:20pt;">Examples</span>
# 
# - **Vectors:** $\overrightarrow{AB} = B - A$
# 
# `````{admonition} Example 3.1
# :class: seealso
# 
# Let $U=(3,-1)$ and $V=(5,0)$ be points in $\mathbb{R}^2$. Determine the vector $\overrightarrow{UV}$.
# `````
# 
# - **Vector magnitude:** $|\mathbf{a}| = \sqrt{\displaystyle\sum_{i=1}^n a_i^2} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}$
# 
# `````{admonition} Example 3.2
# :class: seealso
# 
# Calculate the magnitudes of the following vectors
# 
# (i) &emsp; $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$
# &emsp; &emsp; (ii) &emsp; $\mathbf{v} = \begin{pmatrix} 5 \\ -12 \\ 0 \end{pmatrix}$
# &emsp; &emsp; (iii) &emsp; $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$
# `````
# 
# - **Normalising a vector:** $\hat{\mathbf{a}} = \dfrac{\mathbf{a}}{|\mathbf{a}|}$ 
# 
# `````{admonition} Example 3.3
# :class: seealso
# 
# Find the unit vector parallel to the following:
# 
# (i) &emsp; $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ &emsp; &emsp; 
# (ii) &emsp; $\mathbf{v} = \begin{pmatrix} 5 \\ -12 \\ 0 \end{pmatrix}$ &emsp; &emsp;
# (iii) &emsp; $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$
# `````
# 
# - **Dot product:** $\mathbf{a} \cdot \mathbf{b} = \displaystyle\sum_{i=1}^n a_ib_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n$
# 
# `````{admonition} Example 3.4
# :class: seealso
# 
# Given the vectors $\mathbf{u} = (1, 2, 3)$ and $\mathbf{v} = (3, -1, 0)$. Calculate:
# 
# (i) &emsp; $\mathbf{u} \cdot \mathbf{v}$;
# &emsp; (ii) &emsp; the angle between $\mathbf{u}$ and $\mathbf{v}$
# `````
# 
# - **Cross product:** $\mathbf{a} \times \mathbf{b} = \det \begin{pmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{pmatrix}$
# 
# `````{admonition} Example 3.5
# :class: seealso
# 
# Calculate the cross product between the vectors $\mathbf{u} = (1, 2, 3)$ and $\mathbf{v} = (4, 5, 6)$.
# `````
# 
# - **Linear combination of vectors:** $\mathbf{v}=\alpha_1\mathbf{u}_1+\alpha_2\mathbf{u}_2+\dots+\alpha_m\mathbf{u}_m$
# 
# ````{admonition} Example 3.6
# :class: seealso
# 
# Express the vector $\mathbf{v} = (7, -2, -11)$ as a linear combination of the vectors 
# 
# \begin{align*}
#     \mathbf{u}_1 &= \begin{pmatrix} 1 \\ 0 \\ 7 \end{pmatrix}, &
#     \mathbf{u}_2 &= \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}, &
#     \mathbf{u}_3 &= \begin{pmatrix} 5 \\ -2 \\ -6 \end{pmatrix}.
# \end{align*}
# ````
# 
# - **Basis vectors:** a set of linearly independent vectors for which all other vectors in the space can be represented as a linear combination of
# 
# ````{admonition} Example 3.7
# :class: seealso
# 
# Represent the following vectors as linear combination of the basis vectors $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$
# 
# (i) &emsp; $\begin{pmatrix} 2 \\ 5 \\ 3 \end{pmatrix}$ &emsp; &emsp;
# (ii) &emsp; $3\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}$
# 
# ````
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# `````{admonition} Exercise 3.1
# :class: note
# 
# The points $U$, $V$ and $W$ have the following position vectors:
# \begin{align*}
#     \mathbf{u} &= \begin{pmatrix} 2 \\ 3 \end{pmatrix}, &
#     \mathbf{v} &= \begin{pmatrix} 3 \\ -2 \end{pmatrix}, &
#     \mathbf{w} &= \begin{pmatrix} 1 \\ 6 \end{pmatrix}.
# \end{align*}
# 
# Find:
# 
# ````{grid}
# :gutter: 2
# 
# ```{grid-item} 
# (a) &emsp; $2 \mathbf{u} + \mathbf{w}$
# ```
# ```{grid-item} 
# (b) &emsp; $\mathbf{w} - \mathbf{u}$
# ```
# ```{grid-item}  
# :columns: 12
# (c) &emsp; a unit vector pointing in the same direction of $\mathbf{u}$
# ```
# ```{grid-item}  
# :columns: 12
# (d) &emsp; a unit vector pointing in the opposite direction of $\mathbf{v}$ 
# ```
# ```{grid-item}  
# :columns: 12
# (e) &emsp; a vector pointing in the same direction as $\mathbf{v}$ with half its magnitude
# ```
# ```{grid-item}  
# :columns: 2
# (f) &emsp; $\overrightarrow{UV}$
# ```
# ```{grid-item}  
# :columns: 2
# (g) &emsp; $\overrightarrow{UW}$
# ```
# ```{grid-item}  
# :columns: 2
# (h) &emsp; $\mathbf{u} \cdot \mathbf{w}$
# ```
# ```{grid-item}  
# :columns: 4
# (i) &emsp; the angle $\angle VUW$
# ```
# ```{grid-item}  
# :columns: 4
# (j) &emsp; show that $\mathbf{u}$ is at right angles to $\mathbf{v}$
# ```
# ```{grid-item}  
# :columns: 4
# (k) &emsp; $\mathbf{v} \times \mathbf{w}$
# ```
# ````
# `````
# 
# `````{admonition} Exercise 3.2
# :class: note
# 
# Write $\mathbf{u} = (2,7,1)$ as:
# 
# (a) &emsp; a linear combination of $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, $\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$ and $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.
# 
# (b) &emsp; a linear combination of vectors $\mathbf{f}_1 = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \mathbf{f}_2 = \begin{pmatrix} 0 \\ 2 \\ 0 \end{pmatrix}$ and $\mathbf{f}_3 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.
# 
# `````
# 
# `````{admonition} Exercise 3.3
# :class: note
#         
# Let $\mathbf{u} \in \mathbb{R}^3$ be given as $\mathbf{u} = (x, x + y, z - x) = (1, 3, 5)$.
# 
# (a) &emsp; Find $x$, $y$ and $z$.
# 
# (b) &emsp; What property of vectors are you using to determine $x,y$ and $z$?
# 
# `````
# 
# `````{admonition} Exercise 3.4
# :class: note
# 
# Find $k$ such that the vectors $\mathbf{u}$ and $\mathbf{v}$ are perpendicular:
# 
# (a) &emsp; $\mathbf{u} = (1, k, -2)$ and $\mathbf{v} = (2, -5, 4)$ in $\mathbb{R}^3$.
# 
# (b) &emsp; $\mathbf{u} =(1, 0, k+2, -1, 2)$ and $\mathbf{v} = (1, k, -2, 1, 2)$ in $\mathbb{R}^5$.
# `````
# 
# `````{admonition} Exercise 3.5
# Which pair of the following vectors is perpendicular? For the remaining pairs, what is the angle between them?
# 
# \begin{align*}
#     \mathbf{u} &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, &
#     \mathbf{v} &= \begin{pmatrix} -1 \\ 2 \\ -1 \end{pmatrix}, &
#     \mathbf{w} &= \begin{pmatrix} 2 \\ -3 \\ 1 \end{pmatrix}.
# \end{align*}
# `````
# 
# ``````
