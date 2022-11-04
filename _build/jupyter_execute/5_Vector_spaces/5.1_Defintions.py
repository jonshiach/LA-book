#!/usr/bin/env python
# coding: utf-8

# (vector-spaces-definitions-section)=
# 
# # Definitions
# 
# ```{admonition} Binary operation
# :class: note
# :name: binary-operation-definition
# 
# A **binary operation** is a mapping of two elements of the same set $S$ whose output is also an element of $S$. 
# 
# $$ f: S \times S \to S$$
# 
# The symbol $\times$ is used to denote the [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) and $\to$ denotes a mapping from one set to another.
# ```
# 
# We have already met examples of binary operations in addition, multiplication, subtraction and division of real numbers. For $a,b \in \mathbb{R}$ then
# 
# - $f(a,b) = a + b$ is a real number.
# - $f(a,b) = a \cdot b$ ($a$ multiplied by $b$) is a real number [^1].
# - $f(a,b) = a - b$ is a real number.
# - $f(a,b) = a \div b$ is a real number.
# 
# [^1]: The symbol $\times$ is often used to denote multiplication which strictly speaking should be denoted using $\cdot$ (which is often omitted).
# 
# Another example is for the set of all $2 \times 2$ matrices $M_2(\mathbb{R})$, $f(A, B) = AB$ is a binary operation since $AB$ is also a $2 \times 2$ matrix.
# 
# ```{admonition} Definition: Field
# :class: note
# :name: field-definition
# 
# A **field** is a set $F$ together with two binary operations on elements of $F$ called *addition* and *multiplication*. For $a,b \in F$ addition is written as $a + b$ and multiplication is written as $a \cdot b$. 
# ```
# 
# The classic example of a field is a set of numbers which will suffice for what we will be doing here. However, a field can be any set of objects for which the above definition is satisfied and you may meet other examples of fields in your studies in the future.
# 
# ```{admonition} Definition: Vector space
# :class: note
# :name: vector-space-definition
# 
# A **vector space** over a field $F$ is a non-empty set $V$ of objects called vectors on which the binary operations below are defined
# 
# - **addition** $(+)$: $V \times V \to V$. For example, given two elements $u, v \in V$ we can 'add' them together to obtain another element $u + v \in V$. 
# - **scalar multiplication** $(\cdot )$: $F \times V \to V$. For example given $\alpha \in F$ and $u \in V$ we can 'multiply' $u$ by $\alpha$ to obtain another element $\alpha \cdot u \in V$
# ```
# 
# For example, a field could be the set of all real numbers $\mathbb{R}$ and a vector space be the set of all vectors in $\mathbb{R}^3$ since we can add two vectors and multiply a vector by a scalar. Not all subsets of a field can be classified as a vector space, to do so the set $V$ must satisfy the following axioms. 
# 
# ```{admonition} Theorem: Axioms of a vector space
# :class: important
# :name: vector-space-axioms-theorem
# 
# Let $u, v, w \in V$ and $\alpha, \beta \in F$, $V$ is a vector space if all of the following axioms are satisfied
# 
# - **A1**: Associativity of vector addition: $u + (v + w) = (u + v) + w$;
# - **A2**: Commutativity of vector addition: $u + v = v + u$;
# - **A3**: Identity element of vector addition: there exists an element $0 \in V$ such that $u + 0 = u$ for all $v \in V$;
# - **A4**: Additive inverse: For every $u \in V$ there exists an element $- v \in V$, called the **additive inverse**, such that $u + (- u) = 0$;
# - **M1**: Associativity of scalar multiplication: $\alpha(\beta u) = (\alpha \beta) u$;
# - **M2**: Identity element of scalar multiplication: there exists an element $1$ called the **multiplicative identity** such that $1 u = u$;
# - **M3**: Distributivity of scalar multiplication with respect to vector addition: $\alpha(u + v) = \alpha u + \alpha v$;
# - **M4**: Distributivity of scalar multiplication with respect to addition: $(\alpha + \beta)u = \alpha u + \beta u$.
# ```
# 
# The first group of four axioms are concerned with addition and the second group of four axioms are concerned with scalar multiplication. When the scalars are real numbers, e.g., $F = \mathbb{R}$, we call $V$ a *'real vector space'* which is short for a *'vector space over the field of real numbers'*. When the scalars are complex numbers, e.g., $F=\mathbb{C}$, we talk of a *'complex vector space'*.
# 
# We now list some basic properties for multiplication by scalars in a vector space.
# 
# ```{admonition} Theorem: Properties of vector spaces
# :class: important
# :name: properties-of-vector-spaces-theorem
# 
# Let $V$ be a vector space over $F$ and $u \in V,\alpha\in F$. Then the following hold:
# 
# - $\alpha \cdot 0 = 0$;
# - $0 \cdot u = 0$;
# - if $\alpha \cdot u = 0$ then either $\alpha = 0$ or $u = 0$;
# - $-(\alpha \cdot u) = (-\alpha)\cdot u = \alpha\cdot(-u)$.
# ```
# 
# The name *'vector space'* indicates a connection with the study of vectors. Indeed our Euclidean spaces $\mathbb{R}^n$, as introduced in [Vectors](vectors-chapter), are vector spaces over $F=\mathbb{R}$. Addition and scalar multiplication, in the sense of a vector space, for $\mathbb{R}^n$ are as given in [vector addition](vector-addition-definition) and [scalar multiplication](scalar-multiplication-of-a-vector-definition) respectively. Euclidean vector spaces are often the first examples of vector spaces that a student meets. However, maybe they do not quite demonstrate the power behind this construction. The real motivation of the study of the vector spaces comes from the fact that a lot of more abstract sets, such as differentiable functions or matrices, can be viewed as vector spaces. Everything that we learn about vector spaces can be then applied to any set which satisfies the definition of a vector space. This means that the set of $m\times n$ matrices with matrix addition and scalar multiplication or the set of all polynomials of degree at most $n$, in some sense, behave in a very similar fashion to Euclidean space.
# 
# ````{admonition} Example 5.1
# :class: seealso
# :name: real-numbers-vector-space-example
# 
# Show that the following are vector spaces:
# 
# &emsp; (i) &emsp; The set of real numbers over itself;
# 
# ```{dropdown} Solution
# 
# We need to check that all of the axioms of vector spaces are satisfied. Here $V = \mathbb{R}$, $F = \mathbb{R}$ and let $u, v, w \in V$ and $\alpha, \beta \in \mathbb{R}$
# 
# - A1: $u + (v + w) = (u + v) + w \quad \checkmark$
# - A2: $u + v = v + u \quad \checkmark$
# - A3: $u + 0 = u \quad \checkmark$ (i.e., 0 is the identity element of addition)
# - A4: $u + (-u) = 0 \quad \checkmark$ (i.e., the negative of any number is the additive inverse)
# - M1: $\alpha(\beta u) = (\alpha \beta) u \quad \checkmark$
# - M2: $1 u = u \quad \checkmark$ (i.e., 1 is the multiplicative identity of all numbers)
# - M3: $\alpha(u + v) = \alpha u + \alpha v \quad \checkmark$
# - M4: $(\alpha + \beta) u = \alpha u + \beta u \quad \checkmark$
# ```
# 
# &emsp; (ii) &emsp; The set of all polynomials of degree at most $n$ with real coefficients $P_n(\mathbb{R})$
# 
# \begin{align*}
#     p = p(x) := a_0x^0 + a_1x^1 + a_2x^2 + \cdots + a_nx^n = \sum_{i=0}^n a_ix^i,
# \end{align*}
# 
# where $a_i \in \mathbb{R}$ and $x$ is some variable. Show that $P(\mathbb{R}_n)$ is a vector space.
# 
# ```{dropdown} Solution
# 
# Let $p, r, q \in P_n(\mathbb{R})$ where $a_i, b_i, c_i \in \mathbb{R}$ are the coefficients for $p$, $q$ and $r$ respectively and $k\in \mathbb{R}$ is some scalar then we define
# 
# - Vector addition:
# 
# \begin{align*}
#     p + r &= (a_0 + b_0)x^0 + (a_1 + b_1)x^1 + \cdots + (a_n + b_n)x^n \\
#     &= \sum_{i=0}^n (a_i + b_i)x^i.
# \end{align*}
# 
# - Scalar multiplication:
# 
# \begin{align*}
#     k \cdot p &= ka_0x^0 + ka_1x^1 + \cdots + ka_nx^n \\
#     &= \sum_{i=0}^n ka_ix^i.
# \end{align*}
# 
#  - Additive identity element is the zero polynomial
#  
# \begin{align*}
#     0 = 0x^0 + 0x^1 + \cdots + 0x^n.
# \end{align*}
# 
# - The additive inverse to the polynomial $p$ is
# 
# \begin{align*}
#     -p &= (-a_0)x^0 + (-a_1)x^2 + \cdots + (-a_n)x^n \\
#     &= \sum_{i=0}^n (-a_i)x^i \\
#     &= -\sum_{i=0}^n a_ix^i.
# \end{align*}
# 
# Checking the that axioms of vector spaces are satisfied
# 
# - A1: 
# \begin{align*}
#     p + (q + r) &= \displaystyle \sum_{i=0}^n (a_i + (b_i + c_i))x^i \\
#     &= \displaystyle \sum_{i=0}^n ((a_i + b_i) + c_i)x^i \\
#     &= (p + q) + r \quad \checkmark
# \end{align*}
# 
# - A2: 
# \begin{align*}
#     p + q &= \displaystyle \sum_{i=0}^n (a_i + b_i)x^i \\
#     &= \displaystyle \sum_{i=0}^n (b_i + a_i)x^i \\
#     &= q + p \quad \checkmark
# \end{align*}
# 
# - A3: 
# \begin{align*}
#     p + 0 &= \displaystyle \sum_{i=0}^n (a_i + 0)x^i \\
#     &= \displaystyle \sum_{i=0}^n a_ix^i \\
#     &= p \quad \checkmark
# \end{align*}
# 
# - A4: 
# \begin{align*}
#     p + (-p) &= \displaystyle \sum_{i=0}^n(a_i + (-a_i)) x^i \\
#     &= 0 \quad \checkmark
# \end{align*}
# 
# - M1: 
# \begin{align*}
#     \alpha(\beta p) &= \alpha \displaystyle \sum_{i=0}^n \beta a_i x^i \\
#     &= \alpha \beta \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= (\alpha \beta) p \quad \checkmark
# \end{align*}
# 
# - M2: 
# \begin{align*}
#     1p &= \displaystyle \sum_{i=0}^n 1 a_i x^i \\
#     &= \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= p \quad \checkmark
# \end{align*}
# 
# - M3: 
# \begin{align*}
#     \alpha (p + q) &= \alpha \sum (a_i + b_i) x^i \\
#     &= \alpha \sum a_i x^i + \alpha b_i x^i \\
#     &= \alpha p + \alpha q \quad \checkmark
# \end{align*}
# 
# - M4: 
# \begin{align*}
#     (\alpha + \beta) p &= (\alpha + \beta) \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= \alpha \displaystyle \sum_{i=0}^n a_i x^i + \beta \displaystyle \sum_{i=0}^n a_i x^i \\
#     &= \alpha p + \beta p \quad \checkmark
# \end{align*}
# ```
# ````
# 
# ## Examples of non-vector spaces
# 
# Of course not all sets are vector spaces. For example, consider the set of integers $\mathbb{Z}$ over the field $F=\mathbb{R}$. It is easy to show that the [axioms A1 to A4](vector-space-axioms-theorem) are satisfied for the set of integers. The problem comes when one tries to define scalar multiplication. From the [definition of scalar multiplication](vector-space-definition), $\mathbb{R} \times \mathbb{Z} \to \mathbb{Z}$ so for $u \in \mathbb{Z}$ and $\alpha \in \mathbb{R}$, $\alpha \cdot x\in \mathbb{Z}$. However, this is not always the case, for example, when $u=1$ and $\alpha = \frac{1}{2}$ we have $\frac{1}{2} \cdot 1 = \frac{1}{2} \notin \mathbb{Z}$. This was an example of a proof by counterexample where we just need to show 1 instance where the axioms are not satisfied to prove that we do not have a vector space.
# 
# ````{admonition} Example 5.2
# :class: seealso
# :name: non-vector-space-example
# 
# Show that the following a not vector spaces:
# 
# &emsp; (i) &emsp; The set of all positive real numbers, $\mathbb{R}_+$ over itself
# 
# &emsp; (ii) &emsp; $V$ is defined to be a parabola $y=x^2$ in $\mathbb{R}^2$, i.e., all the points in $\mathbb{R}^2$ defined by $V = {(x, x^2)}$.
# 
# ```{dropdown} Solution
# &emsp; (i) &emsp; We do not have an identity element for addition since $0 \notin \mathbb{R}_+$ so axiom A3 is not satisfied. Also, by axiom A4, if $u, v \in \mathbb{R}_+$ are two positive real numbers then $x + y > 0$ so no additive inverse exists.
# 
# &emsp; (ii) If we take the example $u \in V$ such that $u = (1, 1)$ then the additive inverse $-u = (-1, -1) \notin V$ so $V$ is not a vector space.
# ```
# ````
