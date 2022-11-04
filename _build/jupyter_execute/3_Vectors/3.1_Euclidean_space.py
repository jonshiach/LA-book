#!/usr/bin/env python
# coding: utf-8

# (euclidean-space-section)=
# # Euclidean space
# 
# ```{figure} https://cdn.britannica.com/46/8446-050-BC92B998/Euclid-woodcut-1584.jpg
# ---
# width: 200px
# alt: Euclid
# figclass : margin
# ---
# [Euclid](https://en.wikipedia.org/wiki/Euclid) (fl 300 BCE, coloured woodcut 1584)
# ```
# 
# Before we discuss vectors it is useful to first define [**Euclidean space**](https://en.wikipedia.org/wiki/Euclidean_space) which is the mathematical system which vectors are most commonly applied. Attributed to the Greek mathematician [Euclid](https://en.wikipedia.org/wiki/Euclid), Euclidean space is a representation of physical space where the position of a point in the space can be described by the signed distance along perpendicular real numbers lines called **axes** (singular: axis). 
# 
# An $n$-dimensional Euclidean space is defined by $n$ perpendicular real axes and is referred to as $\mathbb{R}^n$. For example, consider the diagram of $\mathbb{R}^3$ in {numref}`R3-figure`. Here we have a representation of a 3-dimensional Euclidean space defined by the 3 axes labelled $x$, $y$ and $z$. This representation uses the [**right-hand rule**](https://en.wikipedia.org/wiki/Right-hand_rule) so-called because if we use the thumb on our right hand to represent the $x$ axis, the index finger for the $y$ axis and the middle finger for the $z$ axis then holding out the right hand palm up with the thumb and index finger at right-angles and the middle finger pointing up then we have the axis configuration shown in {numref}`R3-figure`. Doing similar with the left hand gives the **left-hand rule** where the $x$ axis is pointing in the opposite direction than in the right-hand rule. 
# 
# ```{figure} ../Images/R3.png
# :name: R3-figure
# 
# The position of a point in $\mathbb{R}^3$ can be defined by its co-ordinates $(x, y, z)$.
# ```
# 
# The position of a point in Euclidean space can be defined by its **co-ordinates** which is an ordered set known as a **tuple** where each element contains the signed distances along each axis, e.g., $(x, y, z)$ where $x, y, z \in \mathbb{R}$. 
