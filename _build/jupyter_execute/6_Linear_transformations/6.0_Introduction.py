#!/usr/bin/env python
# coding: utf-8

# (linear-transformations-chapter)=
# # Linear Transformations
# 
# You will already be familiar with the use of <a href="https://en.wikipedia.org/wiki/Function_(mathematics)" target="_blank">functions</a> in mathematics to study sets and the **mapping** from a set of inputs set to another set of outputs. The notation used to denote functions is of the form $f: X \to Y$ where $f$ is the name of the function, $X$ is the set of inputs known as the **domain** and $Y$ is a member of the set of outputs known as the **codomain**. The mapping which defines the relationship between the domain and codmain is defined using $y = f(x)$ where $x$ is a member of the domain and $y$ is a member of the codomain. 
# 
# In linear algebra we study the linear mapping of a set of vectors to another set of vectors so we define $T: V \to W$ where $V$ and $W$ are vector spaces and the mapping from an input vector $\mathbf{u} \in V$ to an output vector $\mathbf{w} \in W$ is given by $\mathbf{w} = T(\mathbf{u})$.
# 
# Linear transformations have lots of uses in mathematics and computing. A good example is in the field of computer graphics and computer games where they are fundamental to the manipulation and visualisation of three-dimensional objects. 
# 
# **Learning outcomes**
# 
# On successful completion of this chapters students will be able to:
# 
# - identify when a transformation is a [linear transformation](linear-transformation-definition);
# - determine the [transformation matrix](transformation-matrix-definition) that represents a linear transformation;
# - perform [composite linear transformation](composite-transformation-definition);
# - apply [rotation](rotation-in-R2-theorem), [reflection](reflection-theorem), [scaling](scaling-theorem) and [translation](translation-definition) transformations in $\mathbb{R}^2$ as well as their inverses;
# - use [homogeneous co-ordinates](homogeneous-coordinates-definition) to describe points in $\mathbb{R}^n$.
