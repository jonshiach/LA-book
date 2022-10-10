#!/usr/bin/env python
# coding: utf-8

# (coordinate-geometry-chapter)=
# # Co-ordinate Geometry
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - define a line using the [vector equation of a line](vector-equation-of-a-line-definition);
# - determine whether two lines [intersect](line-line-intersection-definition), are [parallel](parallel-lines-definition), [skew](skew-lines-definition) and/or [perpendicular](perpendicular-lines-definition);
# - define a plane using the [point-normal definition of a plane](point-normal-definition);
# - determine the [intersection of two planes](intersection-of-planes-section); 
# - calculate the shortest distance between [two points](shortest-distance-between-two-points), [a point and a line](point-line-distance-theorem), [between two skew lines](line-line-distance-theorem) and [a point and a plane](ex4.7).
# 
# ---
# ## Definition
# 
# The area of mathematics dealing with describing geometry in terms of **coordinate systems**, hence as points and vectors, is called **Cartesian geometry** (named after French mathematician and philosopher [René Descartes](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes)) or **coordinate geometry**. In this chapter we systematise the basic knowledge and understanding of the terms **point**, **line** and **plane**.
# 
# (points-section)=
# ## Points in $\mathbb{R}^n$
# 
# In his works the *Elements*, Euclid described a *point* as *"that which has no part"*
# A point has position only, it has no length, width or thickness, and thus no area or volume. As we've already seen, a typical point in $\mathbb{R}^n$ is described by its co-ordinates $(a_1,a_2,\dots,a_n)$, where the $a_i \in \mathbb{R}$. We also think of $\mathbb{R}^0$ as a single point. This might seem a bit strange because what does a $0$-tuple even mean? However, it makes sense for us to adopt this absolutely standard convention.
# 
# 
# (lines-section)=
# ## Lines in $\mathbb{R}^n$
# 
# Euclid defined a line as having *"breadthless length"* which is another way of saying a line is a one dimensional object that has a length but no breadth or volume. Given that we have already taken the time to introduce vectors in $\mathbb{R}^n$ in [Vectors](vectors-chapter) it makes sense to use them to define what it means to be a line in $\mathbb{R}^n$.
# 
# ````{admonition} Definition: Vector equation of a line
# :class: note
# :name: vector-equation-of-a-line-definition
# 
# Let $P = (p_1, \ldots ,p_n)$ be a point in $\mathbb{R}^n$ and $\mathbf{d} = (d_1, \ldots, d_n)$ a non-zero vector in $\mathbb{R}^n$. The line $\ell$ [^1] which passes through $P$ in the direction of $\mathbf{d}$ has equation
# 
# ```{math}
# :label: line-vector-equation
# 
# Q = P + t\mathbf{d},
# ```
# where $Q$ is a general point on $\ell$ and $t\in \mathbb{R}$ is known as a **parameter**.
# ````
# 
# [^1]: $\ell$ is used here instead of $l$ to avoid confusing with a 1 or uppercase i.
# 
# In other words, every point on $\ell$ is obtained by adding some scalar multiple of $\mathbf{d}$ to $P$ ({numref}`line-vector-equation-figure`). So $\ell$ is the line which passes through $P$ in the direction of $\mathbf{d}$. We call the vector $\mathbf{d}$ a **direction vector** of the line.
# 
# ```{figure} ../Images/line_vector_equation.png
# :name: line-vector-equation-figure
# 
# The position of any point on the line $\ell$ can be obtained by adding a scalar multiple of $\mathbf{d}$ to $P$.
# ```
# 
# In practice one can determine the direction vector $\mathbf{d}$ of a line by taking any two distinct points $P_1$ and  $P_2$ on $\ell$ and setting $\mathbf{d}=P_2 - P_1$ and $P$ in the line equation to be any point on the line. In particular, $\mathbf{d}$ and $P$ are not unique. If fact, one could choose any non-zero scalar multiple of $\mathbf{d}$ to express the same line. Take for instance the $x$-axis in $\mathbb{R}^3$. $\ell$ can be described as
# 
# \begin{align*}
#    Q = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} t \\ 0 \\ 0 \end{pmatrix},
# \end{align*}
# 
# which means we are taking $P=(0,0,0)$ and $\mathbf{d}=(1,0,0)$ and for example the point $Q=(5,0,0)$ is found when $t=5$. Alternatively we can describe the $x$-axis as 
# 
# \begin{align*}
#     Q = \begin{pmatrix} 71 \\ 0 \\ 0 \end{pmatrix} + t \begin{pmatrix} 5 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 71 + 5t \\ 0 \\ 0 \end{pmatrix},
# \end{align*} 
# 
# which means we are taking $P=(71,0,0)$ and $\mathbf{d}=(5,0,0)$ and the point $Q = (5,0,0)$ is found when $71 +5t = 5 \implies t = -\dfrac{66}{5}$.
# 
# 
# `````{admonition} Example 4.1
# :class: seealso
# :name: line-vector-equation-example
# 
# Given a point $P=(1,0,2,1,4)$ and a direction vector $\mathbf{d} = (1,-1,0,-1,1)$ in $\mathbb{R}^5,$ find the equation of the line $\ell$ which goes through $P$ in the direction of $\mathbf{d}$.
# 
# ````{dropdown} Solution
# Substituting $P$ and $\mathbf{d}$ into {eq}`line-vector-equation`
# 
# \begin{align*}
#     Q &= P + t\mathbf{d}
#     = \begin{pmatrix} 1 \\ 0 \\ 2 \\ 1 \\ 4 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ -1 \\ 0 \\ -1 \\ 1 \end{pmatrix}
#     = \begin{pmatrix} 1 + t \\ -t \\ 2 \\ 1 - t \\ 4 + t \end{pmatrix}.
# \end{align*}
# ````
# `````
# 
# (intersecting-lines-section)=
# ## Intersecting lines
# 
# ````{admonition} Definition: Intersection between two lines
# :class: note
# :name: line-line-intersection-definition
# 
# Two lines $\ell_1: P_1 + t_1\mathbf{d}_1$ and $\ell_2: P_2 + t_2\mathbf{d}_2$ in $\mathbb{R}^n$ **intersect** if there exists values of $t_1$ and $t_2$ such that
# 
# \begin{align*}
#     P_1 + t_1 \mathbf{d}_1 = P_2 + t_2 \mathbf{d}_2.
# \end{align*}
# 
# ```{figure} ../Images/line_line_intersection.png
# :name: line-line-intersection-figure
# 
# The intersection between the two lines $\ell_1$ and $\ell_2$.
# ```
# ````
# 
# To determine whether two lines intersect we simply equate the vector equations of the two lines and attempt to solve for $t_1$ and $t_2$.
# 
# ````{admonition} Example 4.2
# :class: seealso
# :name: line-line-intersection-example
# 
# Three lines in $\mathbb{R}^3$ are defined as $\ell_1: (1 + t, -3 + 2t, t)$, $\ell_2: (6 - t, -5 - 2t, t - 1)$ and $\ell_3: (6 + 2t, -11 + 2t, -2 - t)$. Determine the points of intersection between the three lines (if possible).
# 
# ```{dropdown} Solution
# Equating $\ell_1$ and $\ell_2$ gives
# 
# \begin{align*}
#     1 + t_1 &= 6 - t_2, \\
#     -3 + 2t_1 &= -5 + 2t_2, \\
#     t_1 &= -1 + t_2.
# \end{align*}
# 
# The third equation is $t_1 = t_2 - 1$ and substituting into the first equation gives $t_2 = 3$ so $t_1 = 2$. Substituting these into the second equation gives $-3 + 2(2) = -5 + 2(3)$ which is $1 = 1$ so $\ell_1$ and $\ell_2$ intersect. To find the point of intersection we substitute $t_1$ or $t_2$ into the equations for $\ell_1$ or $\ell_2$ respectively.
# 
# \begin{align*}
#     \begin{pmatrix} 1 + 2 \\ -3 + 2(2) \\ 2 \end{pmatrix}  &= \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}, \\
#     \begin{pmatrix} 6 - 3 \\ -5 -2(3) \\ 3 - 1 \end{pmatrix} &= \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}. \\
# \end{align*}
# 
# So $\ell_1$ and $\ell_2$ intersect at $(3, 1, 2)$. 
# 
# Equating $\ell_1$ and $\ell_3$ gives
# 
# \begin{align*}
#     1 + t_1 &= 6 + t_3, \\
#     -3 + 2t_1 &= -11 + 2t_3, \\
#     t_1 &= -2 - t_3.
# \end{align*}
# 
# Substituting the third equation into the first equation gives $1 - 2 - t_3 = 6 + t_3$ so $t_3 = -\frac{7}{2}$ and $t_1 = -\frac{21}{2}$. Substituting these into the second equation gives $-3 + 2(-\frac{21}{2}) = -11 + 2(-\frac{7}{2})$ which is $-24 = -18$ which is a contradiction so no values of $t_1$ or $t_3$ satisfy $\ell_1 = \ell_3$ and $\ell_1$ and $\ell_3$ do not intersect.
# 
# Equating $\ell_2$ and $\ell_3$ gives the system
# 
# \begin{align*}
#     6 - t_2 &= 6 + 2t_3, \\
#     -5 + 2t_2 &= -11 + 2t_3, \\
#     -1 + t_2 &= -2 - t_3.
# \end{align*}
# 
# The third equation gives $t_2 = -1 - t_3$ and substituting into the first equation gives $6 + 1 + t_3 = 6 + 2t_3$ so $t_3 = 1$ and $t_2 = -2$. Substituting these into the second equation gives $-5 + 2(-2) = -11 + 2(1)$ which is $-9 = -9$ so $\ell_2$ and $\ell_3$ intersect. Substituting $t_2$ and $t_3$ into the equations for $\ell_2$ and $\ell_3$
# 
# \begin{align*}
#     \begin{pmatrix} 6 - (-2) \\ -5 + 2(-2) \\ -1 + (-2) \end{pmatrix} &= \begin{pmatrix} 8 \\ -9 \\ -3 \end{pmatrix}, \\
#     \begin{pmatrix} 6 + 2(1) \\ -11 + 2(1) \\ -2 - 1 \end{pmatrix} &= \begin{pmatrix} 8 \\ -9 \\ -3 \end{pmatrix}.
# \end{align*}
# 
# So $\ell_2$ and $\ell_3$ intersect at $(8, -9, -3)$.
# 
# ```
# ````
#  
# ## Parallel lines
# 
# ````{admonition} Definition: Parallel lines
# :class: note
# :name: parallel-lines-definition
#  
# Two lines $\ell_1$ and $\ell_2$ in $\mathbb{R}^n$ are said to be **parallel** if their direction vectors are parallel, i.e., $\mathbf{d_1} = k\mathbf{d_2},$ for some non-zero scalar $k$ ({numref}`parallel-lines-figure`).
# 
# ```{figure} ../Images/parallel_lines.png
# :name: parallel-lines-figure
# 
# The lines $\ell_1$ and $\ell_2$ are parallel in $\mathbb{R}^3$.
# ```
# ````
# 
# In practice the condition from the [definition of parallel lines](parallel-lines-definition) can be verified as follows: two lines $\ell_1$ and $\ell_2$ in $\mathbb{R}^n$ are parallel if for any two distinct points $P_1, P_2 \in \ell_1$ and any two distinct points $Q_1, Q_2 \in \ell_2$ 
# 
# \begin{align*}
#     \overrightarrow{P_1P_2} = k\overrightarrow{Q_1Q_2},
# \end{align*}
# 
# for some non-zero $k \in \mathbb{R}$.
# 
# `````{admonition} Example 4.3
# :class: seealso
# :name: parallel-lines-example
# 
# Let $\ell_1$ and $\ell_2$ be two lines in $\mathbb{R}^3$ be defined by $\ell_1 = \{(x,y,z) : z = x+1, y=0\}$ and $\ell_2 = \{(x,y,z) : z = -x-1, y=3\}$.
# 
# 
# &emsp; (i) &emsp; Write equations for $\ell_1$ and $\ell_2$ in vector form;
# 
# &emsp; (ii) &emsp; show that these lines are not parallel in $\mathbb{R}^3$.
# 
# ````{dropdown} Solutions
# 
# (i) &emsp; To calculate the direction vector $\mathbf{d}$ we need two points on the line. Choosing $x=0$ and $x=1$ then we have the two points $P_1 = (0, 0, 1)$ and $P_2 = (1, 0, 2)$ on $\ell_1$. Therefore
# \begin{align*}
#     \mathbf{d} = P_2 - P_1 = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix},
# \end{align*}
# so the equation of $\ell_1$ is
# \begin{align*}
#     Q = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} t \\ 0 \\ 1 + t \end{pmatrix}.
# \end{align*}
# Doing similar for $\ell_2$ we have $P_1 = (0, 3, -1)$, $P_2 = (1, 3, -2)$ so
# \begin{align*}
#     \mathbf{d} = \overrightarrow{P_1P_2} = P_2 - P_1 = 
#     \begin{pmatrix} 1 \\ 3 \\ -2 \end{pmatrix} - 
#     \begin{pmatrix} 0 \\ 3 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix},
# \end{align*}
# so the equation of $\ell_2$ is
# \begin{align*}
#     Q = \begin{pmatrix} 0 \\ 3 \\ -1 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} t \\ 3 \\ -1 -t \end{pmatrix}.
# \end{align*}
# 
# (ii) &emsp; Notice that to verify if the two lines are parallel we do not need to know their equations, just their direction vectors. From [the definition of parallel lines](parallel-lines-definition), $\ell_1$ and $\ell_2$ are parallel if $\mathbf{d}_1 = k\mathbf{d}_2$, therefore
# 
# \begin{align*}
#     \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} &= k
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}
#     \qquad \implies \qquad 
#     \begin{matrix}
#         k = 1, \\
#         k = -1
#     \end{matrix}
# \end{align*}
# 
# Here we have a contradiction so no value of $k$ exists to satisfy $\mathbf{d}_1 = k\mathbf{d}_2$ so $\ell_1$ and $\ell_2$ are not parallel.
# 
# ````
# `````
# 
# ## Skew lines
# 
# ````{admonition} Definition: Skew lines
# :class: note
# :name: skew-lines-definition
# 
# Two distinct lines in $\mathbb{R}^3$, which neither intersect nor are parallel, are called **skew lines** ({numref}`skew-lines-figure`)
# 
# ```{figure} ../Images/skew_lines.png
# :name: skew-lines-figure
# 
# The lines $\ell_1$ and $\ell_2$ are skew lines in $\mathbb{R}^3$.
# ```
# ````
# 
# ````{admonition} Example 4.4
# :class: seealso
# :name: skew-lines-example
# 
# Show that the lines $\ell_1$ and $\ell_2$ from [example 4.3](parallel-lines-example) are skew lines.
# 
# ```{dropdown} Solution
# 
# We have shown in [example 4.3](parallel-lines-example) that $\ell_1$ and $\ell_2$ are not parallel. Therefore to we need to show that they do not intersect. Equating $\ell_1$ and $\ell_2$ gives
# 
# \begin{align*}
#     t_1 &= t_2, \\
#     0 &= 3, \\
#     -1 &= -1 - t_2.
# \end{align*}
# 
# Here the second equation is a contradiction so this system is inconsistent and the lines $\ell_1$ and $\ell_2$ do not intersect. Since $\ell_1$ and $\ell_2$ are not parallel and do not intersect then they must be skew.
# ```
# 
# ````
# 
# ## Perpendicular lines
# 
# ````{admonition} Definition: Perpendicular lines
# :class: note
# :name: perpendicular-lines-definition
# 
# Two lines, $\ell_1$ and $\ell_2$, are **perpendicular** if their direction vectors $\mathbf{d}_1$ and $\mathbf{d}_2$ respectively are at right angles. We denote this using $\ell_1 \perp \ell_2$. In $\mathbb{R}^n$ two lines are perpendicular if and only if their direction vectors are perpendicular, which happens precisely when their dot product is zero.
# ````
# 
# `````{admonition} Example 4.5
# :class: seealso
# :name: perpendicular-lines-example
# 
# &emsp; (i) &emsp; Determine whether the two lines from [example 4.3](parallel-lines-example) are perpendicular.
# 
# &emsp; (ii) &emsp; Find the equation of a line $\ell_2$ which is perpendicular to $\ell_1 = \{(t,-t,1+t) : t \in \mathbb{R} \}$ at the point $P = (-1,1,0).$
# 
# ````{dropdown} Solution
# (i) &emsp; The direction vectors were $\mathbf{d}_1 = (1, 0, 1)$ and $\mathbf{d}_2 = (1, 0, -1)$ 
# 
# \begin{align*}
#     \mathbf{d}_1 \cdot \mathbf{d}_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = 1 + 0 + (-1) = 0.
# \end{align*}
# 
# So $\ell_1 \perp \ell_2$.
# 
# (ii) &emsp; Writing $\ell_1$ in vector form gives
# 
# \begin{align*}
#     Q = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so the direction vector is $\mathbf{d}_1 = (1, -1, 1)$. To find a direction vector perpendicular to $\mathbf{d}_1$, $\mathbf{d}_2$ say, we need to satisfy $\mathbf{d}_1 \cdot \mathbf{d}_2 = 0$
# 
# \begin{align*}
#     \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}  \cdot \mathbf{d}_2 = 
#     \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \cdot 
#     \begin{pmatrix} d_1 \\ d_2 \\ d_3 \end{pmatrix} = d_1 - d_2 + d_3 = 0.
# \end{align*}
# 
# This equation has infinitely many solutions, to find a solution we need to choose values for any two from $d_1$ ,$d_2$ and $d_3$ (where at least one is non-zero). Let $d_1 = 1$ and $d_2 = 0$ then $d_3 = -1$ so $\mathbf{d}_2 = (1, 0, -1)$. Since $\ell_2$ passes through $P = (-1, 1, 0)$ and the equation of $\ell_2$ is
# 
# \begin{align*}
#     Q = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = 
#     \begin{pmatrix} -1 + t \\ 1 \\ -t \end{pmatrix} = (-1 + t, 1, -t).
# \end{align*}
# ````
# `````
# 
# The notion of perpendicularity does not necessarily require that the lines intersect. The only condition is that the direction vectors of lines are perpendicular.
