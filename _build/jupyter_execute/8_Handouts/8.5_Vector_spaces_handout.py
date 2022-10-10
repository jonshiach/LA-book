#!/usr/bin/env python
# coding: utf-8

# # Vector Spaces
# 
# ``````{div} full-width
# 
# <span style="font-size:20pt;">Examples</span>
# 
# - **Vector space axioms:**
#     - A1: Associativity of vector addition: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$;
#     - A2: Commutativity of vector addition: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$;
#     - A3: Identity element of vector addition: there exists an element $\mathbf{0} \in V$ such that $\mathbf{u} + \mathbf{0} = \mathbf{u}$ for all $\mathbf{v} \in V$;
#     - A4: Additive inverse: For every $\mathbf{u} \in V$ there exists an element $- \mathbf{v} \in V$, called the **additive inverse**, such that $\mathbf{u} + (- \mathbf{u}) = \mathbf{0}$;
#     - M1: Associativity of scalar multiplication: $\alpha(\beta \mathbf{u}) = (\alpha \beta) \mathbf{u}$;
#     - M2: Identity element of scalar multiplication: there exists an element $1$ called the **multiplicative identity** such that $1 \mathbf{u} = \mathbf{u}$;
#     - M3: Distributivity of scalar multiplication with respect to vector addition: $\alpha(\mathbf{u} + \mathbf{v}) = \alpha \mathbf{u} + \alpha \mathbf{v}$;
#     - M4: Distributivity of scalar multiplication with respect to addition: $(\alpha + \beta)\mathbf{u} = \alpha \mathbf{u} + \beta \mathbf{u}$.
# 
# ````{admonition} Example 5.1
# :class: seealso
# :name: real-numbers-vector-space-example
# 
# Show that the following are vector spaces:
# 
# &emsp; (i) &emsp; The set of real numbers over itself;
# 
# &emsp; (ii) &emsp; The set of all polynomials of degree at most $n$ with real coefficients $P(\mathbb{R}_n)$
# 
# \begin{align*}
#     p = p(x) := a_0x^0 + a_1x^1 + a_2x^2 + \cdots + a_nx^n = \sum_{i=0}^n a_ix^i,
# \end{align*}
# 
# &emsp; where $a_i \in \mathbb{R}$ and $x$ is some variable. Show that $P(\mathbb{R}_n)$ is a vector space.
# 
# ````
# 
# ````{admonition} Example 5.2
# :class: seealso
# :name: non-vector-space-example
# 
# Show that the following a not vector spaces:
# 
# &emsp; (i) &emsp; The set of all positive real numbers, $\mathbb{R}_+$ over itself
# 
# &emsp; (ii) &emsp; $V$ is defined to be a parabola $y=x^2$ in $\mathbb{R}^2$, i.e., all the points in $\mathbb{R}^2$ defined by $V = {(x, x^2)}$
# ````
# 
# - **Subspace condition:** $W$ is a subspace of $V$ over the field $F$ if $W \neq \emptyset$ and for any $\mathbf{u}, \mathbf{w} \in V$ and $\alpha \in F$ the condition $\mathbf{u} + \alpha\mathbf{w} \in W$ holds
# 
# ````{admonition} Example 5.3
# :class: seealso
# :name: subspace-example
# 
# &emsp; (i) &emsp; Let $W$ be the subset $M_{2\times 2}$ given by
# 
# \begin{align*}
#     W = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} : a + b + c + d = 0 \right\}.
# \end{align*}
# 
# &emsp; Show that $W$ is a subspace of $M_{2\times 2}$.
# 
# &emsp; (ii) &emsp; Let $W = \{ p(x) \in P(\mathbb{R}_n) : p(x) = p(-x)\} \subseteq P(\mathbb{R}_n)$ be the set of all even functions. Show that $W$ is a subspace of $P(\mathbb{R}_n)$.
# ````
# 
# ````{admonition} Example 5.4
# :class: seealso
# :name: non-subspace-example
# 
# Show that the following are not subspaces:
# 
# &emsp; (i) &emsp; $W = \{z = (a+bi) : a + b = 5\} \subseteq \mathbb{C}$;
# 
# &emsp; (ii) &emsp; $W = \{z = (a + bi) : a^2 + b^2 < 0\} \subseteq \mathbb{C}$;
# 
# &emsp; (iii) &emsp; $W = \{(x,y,z) : x + y + z = 5\} \subseteq{\mathbb{R}^3}$.
# 
# ````
# 
# - **Linear independence:** a set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ are linearly independent if the only solution to the equation $\alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n = \mathbf{0}$ is $\alpha_i = 0$ for $i = 1, \ldots, n$.
# 
# ````{admonition} Example 5.5
# :class: seealso
# :name: linear-dependence-equation
# 
# Determine whether the following are linearly dependent
# 
# &emsp; (i) &emsp; $(1, 0, 2), (2, 1, 3), (-3, -4, -2) \in \mathbb{R}^3$ over $\mathbb{R}$
# 
# &emsp; (ii) &emsp; $p(x) = x^2 + x + 1$, $r(x) = x - 1$ and $s(x) = x^2 - 1 \in P(\mathbb{R}_2)$ over $\mathbb{R}$
# ````
# 
# - **Spanning set:** a set of linearly independent vectors $S$ for which all over vectors in the vector space can be expressed by a linear combination of the vectors in $S$
# 
# ````{admonition} Example 5.6
# :class: seealso
# :name: spanning-set-example
# 
# &emsp; (i) &emsp; Show that  $\{ \mathbf{v}_1, \mathbf{v}_2 \}$ where $\mathbf{v}_1 = (2, 1)$ and $\mathbf{v}_2 = (4, 3)$ is a spanning set for $\mathbb{R}^2$.
# 
# &emsp; (ii) &emsp; Determine a spanning set for $\mathbb{R}^3$.
# ````
# 
# - **Basis:** for a vector space $V$ a basis is a set of vectors $W \subset V$ where $W$ spans $V$.
# - **Orthoganal basis:** each of the basis vectors are orthogonal (perpendicular) to one another
# - **Orthonormal basis:** and orthogonal basis where each basis vector has a magnitude of 1
# - **Dimension of a vector space:** the cardinality of the basis
# 
# ````{admonition} Example 5.7
# :class: seealso
# :name: basis-example
# 
# Show that the vectors $\mathbf{v}_1 = (1, 1, 0)$, $\mathbf{v}_2 = (1, -1, 1)$ and $\mathbf{v}_3 = (1, -1, -2)$ is a basis for $\mathbb{R}^3$.
# ````
# 
# ````{admonition} Example 5.8
# :class: seealso
# :name: change-of-basis-example
# 
# Represent the vector $\mathbf{u} = (4, 0, 5)$ with respect to the basis $W = \{(1, 1, 0), (1, -1, 1), (1, -1, -2)\}$.
# ````
# 
# <span style="font-size:20pt;">Exercises</span>
# 
# ````{admonition} Exercise 5.1
# :class: note
# :name: ex5.1
# 
# Prove that the [axioms](vector-space-axioms-theorem) of the vector space $\mathbb{R}^3$ hold.
# ````
# 
# ````{admonition} Exercise 5.2
# :class: note
# :name: ex5.2
# 
# Using [the subspace condition](subspace-condition-theorem), determine whether the following subsets of $\mathbb{R}^3$ are subspaces:
# 
# &emsp; (a) &emsp; $U = \{ (x, y, 0) : x, y \in \mathbb{R} \}$
# 
# &emsp; (b) &emsp; $V = \{ (1, 2, 0) \}$
# 
# &emsp; (c) &emsp; $W = \{ (0, y, 0) : y \in \mathbb{R} \}$
# 
# &emsp; (d) &emsp; $X = \{ (x, y, z) : y = |x|, x, y, z \in \mathbb{R}\}$
# 
# ````
# 
# ````{admonition} Exercise 5.3
# :class: note
# :name: ex5.3
# 
# Which of the following sets are subspaces of $M_{2\times 2}$?
# 
# &emsp; (a) &emsp; $A = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} : a, b, c, d \in \mathbb{R}, a + b = 1,  \right\}$
# 
# &emsp; (b) &emsp; $B = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix}: a, b, c, d \in \mathbb{R}, a = c = d \right\}$
# 
# &emsp; (c) &emsp; $C = \{ A \in M_{2\times 2} : A^2 = A \}$
# 
# ````
# 
# ````{admonition} Exercise 5.4
# :class: note
# :name: ex5.4
# 
# Prove that $\{ (1, 2, 0), (0, 5, 7), (-1, 1, 3) \}$ is a basis for $\mathbb{R}^3$ and find the co-ordinates of $(0, 13, 17)$ and $(2, 3, 1)$ relative to this basis.
# ````
# 
# ````{admonition} Exercise 5.5
# :class: note
# :name: ex5.5
# 
# Extend $\{(1, 1, 2, 4), (2, -1, -5, 2)\}$ to a basis of $\mathbb{R}^4$.
# ````
# 
# ````{admonition} Exercise 5.6
# :class: note
# :name: ex5.6
# 
# Suppose that $W$ is a subspace of $\mathbb{R}^4$ generated by the vectors
# 
# \begin{align*}
#     \left\{ \mathbf{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}, 
#     \mathbf{v} = \begin{pmatrix} 1 \\ -1 \\ 2 \\ 0 \end{pmatrix}, 
#     \mathbf{w} = \begin{pmatrix} 2 \\ 1 \\ 5 \\ 3 \end{pmatrix}, 
#     \mathbf{x} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 3 \end{pmatrix}, 
#     \mathbf{y} = \begin{pmatrix} 1 \\ -1 \\ 0 \\ 4 \end{pmatrix} \right\}.
# \end{align*}
# 
# Find a basis for $W$ and determine $\dim(W)$.
# ````
# ``````
