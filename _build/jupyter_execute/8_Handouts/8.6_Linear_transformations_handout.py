#!/usr/bin/env python
# coding: utf-8

# # Linear Transformations
# 
# <span style="font-size:20pt;">Examples</span>
# 
# ``````{div} full-width
# 
# - **Linear transformation:** $T:V \to W$ is a linear transformation defined by $T: \mathbf{u} \mapsto \mathbf{w}$ where $\mathbf{u} \in V$ and $\mathbf{v} \in W$ such that $T(x + \alpha y) = T(x) + \alpha T(y)$ for $\alpha \in F$
# 
# ````{admonition} Example 6.1
# :class: seealso
# :name: linear-transformation-example
# 
# Determine which of the following transformations are linear transformations
# 
# &emsp; (i) &emsp; $T: \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T: (x, y, z) \mapsto (x, y)$
# 
# &emsp; (ii) &emsp; $T: \mathbb{R}^3 \to \mathbb{R}^2$ defined by $T: (x, y, z) \mapsto (x + 3, y)$
# ````
# 
# - **Transformation matrix:** the transformation matrix for a linear transformation $T$ is a matrix $A$ such that $T(\mathbf{u}) = A \mathbf{u}$ where $A = (T(\mathbf{v}_1), T(\mathbf{v}_2), \ldots, T(\mathbf{v}_n))$ where $\mathbf{v}_1, \ldots, \mathbf{v}_n$ are basis vectors.
# 
# ````{admonition} Example 6.2
# :class: seealso
# :name: transformation-matrix-example
# 
# A linear transformation $T:\mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (3x + y, x + 2y)$. Calculate the transformation matrix and use it to calculate $T(1, 1)$.
# ````
# 
# - **Determining the transformation matrix from a set of images:** if $T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)$ are the images for a linear transformation $T$ then the transformation matrix for $T$ is $A = (T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)) \cdot (\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n)^{-1}$
# 
# ````{admonition} Example 6.3
# :class: seealso
# :name: transformation-matrix-example-2
# 
# Determine the transformation matrix $A$ for the linear transformation $T$ such that
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 4 \\ 3 \end{pmatrix}, &
#     T\begin{pmatrix} 1 \\ 2 \end{pmatrix} &= \begin{pmatrix} 5 \\ 5 \end{pmatrix}.
# \end{align*}
# ````
# 
# - **Inverse linear transformation:** the inverse of a linear transformation $T: V \to W$ is $T^{-1}: W \to V$. If $A$ is the transformation matrix for $T$ then the transformation matrix for $T^{-1}$ is $A^{-1}$
# 
# ````{admonition} Example 6.4
# :class: seealso
# :name: inverse-transformation-example
#     
# Determine the inverse of the transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ defined by $T(x, y) \mapsto (3 x + y, x + 2 y)$ and calculate $T^{-1}(4, 3)$.
# ````
# 
# - **Composite linear transformations:** if $T$ and $S$ are linear transformations then $S \circ T(\mathbf{u}) = S(T(\mathbf{u}))$ is a composite transformation.
# 
# ````{admonition} Example 6.5
# :class: seealso
# :name: composite-transformation-example
# 
# Two linear transformations is defined as $T:(x, y, z) \mapsto (2 x + 4 y, -x + 3 y, x + 2 y)$ and $S:(x, y) \mapsto (2x + y - z, 3x + z, y - 2z)$, determine the composite linear transformation $S \circ T(\mathbf{u})$ for $\mathbf{u} = (x, y, z)$.
# ````
# 
# - **Composite transformations matrix:** if $T$ and $S$ are linear transformations with transformation matrices $A$ and $B$ respectively then $S \circ T(\mathbf{u}) = B \cdot A \cdot \mathbf{u}$
# 
# 
# ````{admonition} Example 6.6
# :class: seealso
# :name: composite-transformation-matrix-example
# 
# Calculate the transformation matrices, $A$ and $B$, for the transformations $T$ and $S$ from [example 6.5](composite-transformation-example) and use them to calculate the transformation matrix $C$ for $S\circ T$. 
# ````
# 
# - **Rotation transformation:** the transformation matrix for rotation in $\mathbb{R}^2$ anti-clockwise by the angle $\theta$ about the origin is $Rot(\theta) = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}$
# 
# `````{admonition} Example 6.7
# :class: seealso
# :name: rotation-example
# 
# Rotate the vector $\mathbf{u} = (2, 1)$ by angle $\theta = \frac{\pi}{2}$ anti-clockwise about the origin.
# `````
# 
# - **Reflection transformation:** the transformation matrix for rotation in $\mathbb{R}^2$ about the line that passes through the origin at an angle $\theta$ from the $x$-axis is $Ref(\theta) = \begin{pmatrix} \cos(2\theta) & \sin(2 \theta) \\ \sin(2\theta) & -\cos(2\theta) \end{pmatrix}$
# 
# `````{admonition} Example 6.8
# :class: seealso
# :name: reflection-example
# 
# Reflect the vector $\mathbf{u} = (3, -1)$ about the line that passes through the origin and has gradient of 1. 
# `````
# 
# - **Scaling transformation:** the transformation matrix for scaling in $\mathbb{R}^n$ by scaling vector $\mathbf{s} = (s_1, s_2, \ldots, s_n)$ about the origin is $S(\mathbf{s}) = \begin{pmatrix} s_1 & 0 & \cdots & 0 \\ 0 & s_2 & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & s_n \end{pmatrix}$
# 
# `````{admonition} Example 6.9
# :class: seealso
# :name: scaling-example
# 
# Scale the point with position vector $\mathbf{u} = (2,1)$ by scaling scaling vector $\mathbf{s} = (2, 3)$.
# `````
# 
# - **Translation transformation:** the transformation matrix for translating the vector $\mathbf{u} = (u_1, u_2, \ldots, u_n, 1)$ in $\mathbb{R}^n$ by the translation vector $\mathbf{t} = (t_1, t_2, \ldots, t_n)$ is $T(\mathbf{t}) = \begin{pmatrix} 
#         & & & t_1 \\
#         & I_n & & \vdots \\
#         & & & t_n \\
#         0 & \cdots & 0 & 1
#     \end{pmatrix}$
# 
# `````{admonition} Example 6.10
# :class: seealso
# :name: translation-example
# 
# Translate the point with position vector $\mathbf{u} = (1, 2)$ by the vector $\mathbf{t} = (3, 1)$.
# `````
# 
# `````{admonition} Example 6.11
# :class: seealso
# :name: rotation-scaling-and-translating-example
# 
# An isosceles triangle has the vertices with co-ordinates $(-1, -1)$, $(1, -1)$ and $(0, 2)$. The triangle is transformed using the following transformations:
# 
# - Scaled by a factor of 2 in both directions
# - Rotated by $\frac{\pi}{4}$ anti-clockwise about the origin
# - Translated by the vector $\mathbf{t} = (6, 4)$
# 
# Calculate the co-ordinates of the triangle after each of these transformations has been applied and determine a transformation matrix that performs all three transformations at the same time.  
# `````
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# `````{admonition} Exercise 6.1
# :class: note
# :name: ex6.1
# 
# Which of the following transformations are linear transformations?
# 
# ````{grid}
# 
# ```{grid-item}
# :columns: 4
# (a) &emsp; $T: (x, y) \mapsto (0, y)$
# ```
# 
# ```{grid-item}
# :columns: 4
# (b) &emsp; $T: (x, y) \mapsto (x, 5)$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (c) &emsp; $T: (x, y) \mapsto (x, x - y)$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (d) &emsp; $T: (x, y, z) \mapsto (x + y, z)$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (e) &emsp; $T: (x, y) \mapsto (3x + 1, y)$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (f) &emsp; $T: f(x) \mapsto \dfrac{\mathrm{d}}{\mathrm{d}x} f(x)$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (g) &emsp; $T: f(x) \mapsto xf(x)$
# ```
# 
# ```{grid-item}
# :columns: 6
# 
# (h) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto x + y$
# ```
# 
# ```{grid-item}
# :columns: 4
# 
# (i) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto x y$
# ```
# 
# ```{grid-item}
# :columns: 6
# 
# (j) &emsp; $T: \mathbb{C}^2 \to \mathbb{C}$ where $T: (x, y) \mapsto \bar{y}$
# ```
# ````
# 
# $\bar{x}$ is the complex conjugate of $x = a + bi$ defined by $\bar{x} = a - bi$
# 
# `````
# 
# `````{admonition} Exercise 6.2
# :class: note
# :name: ex6.2
# 
# A linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (-x + 3y, x - 4y)$. Determine the transformation matrix for $T$ and hence calculate $T \begin{pmatrix} 2 \\ 5 \end{pmatrix}$.
# `````
# 
# `````{admonition} Exercise 6.3
# :class: note
# :name: ex6.3
# 
# A linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$ is defined by $T: (x, y) \mapsto (x - 2y, 2x + 3y)$. Given $T(\mathbf{u}) = \begin{pmatrix} -1 \\ 5 \end{pmatrix}$ determine $\mathbf{u}$.
# `````
# 
# `````{admonition} Exercise 6.4
# :class: note
# :name: ex6.4
# 
# $T: \mathbb{R}^3 \to \mathbb{R}^3$ is a linear transformation such that
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} &= \begin{pmatrix} 4 \\ 3 \\ 11 \end{pmatrix}, &
#     T\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} &= \begin{pmatrix} 1 \\ 0 \\ 4 \end{pmatrix}, &
#     T\begin{pmatrix} -2 \\ -1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 1 \\ 3 \\-1 \end{pmatrix}.
# \end{align*}
# 
# Find the transformation matrix for $T$.
# `````
# 
# `````{admonition} Exercise 6.5
# :class: note
# :name: ex6.5
# 
# A rotate the point with co-ordinates $(2, 1)$ by $\frac{\pi}{6}$ anti-clockwise about the origin. 
# `````
# 
# ``````
