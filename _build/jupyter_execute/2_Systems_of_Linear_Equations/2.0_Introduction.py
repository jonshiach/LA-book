#!/usr/bin/env python
# coding: utf-8

# (systems-of-linear-equations-chapter)=
# # Systems of Linear Equations
# 
# Systems of linear equations, and the methods used to solve them, is a fundamental part of linear algebra. They are used to describe relationships between sets of variables and have applications in co-ordinate geometry, numerical methods, the solution to differential equations and mathematical modelling to name a few. There are many techniques we can use to compute the solutions to systems of linear equations and we will be covering the most common of these.
# 
# ## Learning outcomes
# 
# On successful completion of this chapter students will be able to:
# 
# - [define a system of linear equations](system-of-linear-equation-definition) and write them as a matrix equation;
# - calculate the solution to a system of linear equations using the [inverse matrix](solution-using-inverse-matrix-theorem) and [Cramer's rule](cramers-rule-theorem);
# - use [Gaussian elimination](ge-definition) to row reduce a matrix to [row echelon form](ref-definition) and calculate the solution to a system of linear equations using back substitution;
# - use [partial pivoting](ge-pp-definition) to reduce the risk of rounding errors whilst performing Gaussian elimination;
# - use [Gauss-Jordan elimination](gje-definition) to row reduce a matrix to [reduced row echelon form](rref-definition) and use it to solver a system of linear equations
# - use Gauss-Jordan elimination to calculate the [inverse of a matrix](gj-matrix-inverse-section);
# - identity when a system of linear equations is [consistent](consistent-system-theorem), [inconsistent](inconsistent-system-theorem) or [indeterminate](indeterminate-system-theorem);
# - solve a [homogeneous system of linear equations](homogeneous-system-definition).
