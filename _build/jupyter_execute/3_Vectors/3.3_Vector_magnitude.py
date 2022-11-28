#!/usr/bin/env python
# coding: utf-8

# (vector-magnitude-section)=
# # Vector magnitude
# 
# The **magnitude** of a vector $\overrightarrow{AB}$ is the distance between the two points $A$ and $B$ which we can calculate using an extension of Pythagoras' theorem.
# 
# ````{admonition} Definition: Vector magnitude
# :class: note
# :name: magnitude-definition
# 
# The **magnitude** of a vector $\mathbf{a} = (a_1, a_2, \ldots, a_n)$ denoted by $|\mathbf{a}|$ is calculated using
# 
# ```{math}
# :label: magnitude-equation
# |\mathbf{a}| = \sqrt{\sum_{i=1}^n a_i^2} = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}.
# 
# ```
# ````
# 
# Vector magnitude is also known as the [**Euclidean norm**](https://en.wikipedia.org/wiki/Norm_(mathematics)). Note that $|\mathbf{a}|=0$ if and only if $\mathbf{a}=(0, 0, \ldots, 0)$.
# 
# `````{admonition} Example 3.2
# :class: seealso
# :name: magnitude-example
# 
# Calculate the magnitudes of the following vectors
# 
# &emsp; (i) &emsp; $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$
# &emsp; &emsp; (ii) &emsp; $\mathbf{v} = \begin{pmatrix} 5 \\ -12 \\ 0 \end{pmatrix}$
# &emsp; &emsp; (iii) &emsp; $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$
# 
# ````{dropdown} Solution
# (i) &emsp; $|\mathbf{u}| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1+4+9} = \sqrt{14}$
# 
# (ii) &emsp; $|\mathbf{v}| = \sqrt{5^2 + (-12)^2 + 0^2} = \sqrt{25+144+0} = \sqrt{169} = 13$
# 
# (iii) &emsp; $|\mathbf{w}| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1+0+1} = \sqrt{2}$
# ````
# 
# `````
# 
# ## Python code
# 
# The SymPy command for calculating the magnitude of a vector `v` is `v.norm()`. The code below calculates the solutions to [example 3.2](magnitude-example).

# In[1]:


import sympy as sym

# (i)
u = sym.Matrix([1, 2, 3])
print("(i)  ")
display(u.norm())

# (ii)
v = sym.Matrix([5, -12, 0])
print("(ii)")
display(v.norm())

# (iii)
w = sym.Matrix([1, 0, 1])
print("(iii)")
display(w.norm())


# ## Unit vectors
# 
# For every non-zero vector $\mathbf{a}$ there exist a unique **unit vector** which is a vector in the same direction as $\mathbf{a}$ and whose magnitude is 1.
# 
# ````{admonition} Definition: Unit vectors
# :class: note
# :name: unit-vector-definition
# 
# A unit vector is a vector with a magnitude of 1.
# ````
# 
# `````{admonition} Proposition: Normalising a vector
# :class: important
# :name: normalising-a-vector-proposition
# 
# Any non-zero vector can be scaled to transform it into a unit vector by dividing all its coordinates by its magnitude
# 
# ```{math}
# :label: normalising-a-vector-equation
# 
# \hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}.
# ```
# 
# This process is called **normalising a vector**. Unit vectors are denoted with a caret above the vector name, i.e., $\hat{\mathbf{a}}$ which is read as *'$\mathbf{a}$ hat'*.
# 
# `````
# 
# **Proof**
# 
# *Let $\mathbf{a}$ be a non-zero vector*
# 
# \begin{align*}
#     \left|\frac{1}{|\mathbf{a}|}\mathbf{a}\right| &= \left|\frac{1}{|\mathbf{a}|}\right| |\mathbf{a}| \\
#     &= \frac{1}{|\mathbf{a}|} |\mathbf{a}| \qquad \text{(since $|\mathbf{a}|>0$)}\\
#     &= 1.
# \end{align*}
# 
# <div style="text-align: right"> &#9633; </div>
# 
# `````{admonition} Example 3.3
# :class: seealso
# :name: normalising-a-vector-example
# 
# Find the unit vector parallel to the following:
# 
# &emsp; (i) &emsp; $\mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ &emsp; &emsp; 
# (ii) &emsp; $\mathbf{v} = \begin{pmatrix} 5 \\ -12 \\ 0 \end{pmatrix}$ &emsp; &emsp;
# (iii) &emsp; $\mathbf{w} = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$
# 
# ````{dropdown} Solution
# (i) &emsp; $\hat{\mathbf{u}} = \dfrac{\mathbf{u}}{|\mathbf{u}|} = \dfrac{1}{\sqrt{14}} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{14}}{14} \\ \frac{\sqrt{14}}{7} \\ \frac{3\sqrt{14}}{14} \end{pmatrix}$
# 
# Check magnitude of $\hat{\mathbf{u}}$
# 
# \begin{align*}
#     |\hat{\mathbf{u}}| &= \sqrt{ \left( \frac{\sqrt{14}}{14} \right)^2 + \left( \frac{\sqrt{14}}{7} \right)^2 + \left(\frac{3\sqrt{14}}{14} \right)^2} \\
#     &= \sqrt{ \frac{14}{196} +\frac{14}{49} + \frac{126}{196}} = \sqrt{1} = 1 \qquad \checkmark
# \end{align*}
# 
# (ii) &emsp; $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{|\mathbf{v}|} = \dfrac{1}{13} \begin{pmatrix} 5 \\ -12 \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{5}{13} \\ -\frac{12}{13} \\ 0 \end{pmatrix}$
# 
# Check magnitude of $\hat{\mathbf{v}}$
# 
# \begin{align*}
#     |\hat{\mathbf{v}}| &= \sqrt{ \left(\frac{5}{13} \right)^2 + \left( -\frac{12}{13} \right)^2 + 0^2} \\
#     &= \sqrt{ \frac{25}{169} + \frac{144}{169} + 0} = \sqrt{1} = 1 \qquad \checkmark
# \end{align*}
# 
# (iii) &emsp; $\hat{\mathbf{w}} = \dfrac{\mathbf{w}}{|\mathbf{w}|} = \dfrac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{2}}{2} \\ 0 \\ \frac{\sqrt{2}}{2} \end{pmatrix}$
# 
# Check magnitude of $\hat{\mathbf{w}}$
# 
# \begin{align*}
#     |\hat{\mathbf{w}}| &= \sqrt{ \left( \frac{\sqrt{2}}{2} \right)^2 + 0^2 + \left( \frac{\sqrt{2}}{2} \right)^2 } \\
#     &= \sqrt{ \frac{2}{4} + 0 + \frac{2}{4} } = \sqrt{1} = 1 \qquad \checkmark
# \end{align*}
# 
# ````
# `````
# 
# ### Python code
# 
# The code below calculates the solutions to [example 3.3](normalising-a-vector-example).

# In[14]:


# (i)
uhat = u / u.norm()

print("(i) uhat")
display(uhat)

# (ii)
vhat = v / v.norm()

print("(ii) vhat")
display(vhat)

# (iii)
what = w / w.norm()

print("(iii) what")
display(what)

