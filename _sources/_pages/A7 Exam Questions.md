# Exam Questions

## 2025 Exam

---

### Question 1

Let $A$, $B$ and $C$ be matrices defined as follows:

$$ \begin{align*}
    A &= 
    \begin{pmatrix}
        1 & 2 & 3 \\
        0 & 4 & 5 \\
        1 & 0 & 6 
    \end{pmatrix}, &
    B &= 
    \begin{pmatrix}
        7 & 8 & 9 \\
        2 & 1 & 4 \\
        3 & 6 & 5 
    \end{pmatrix}, &
    C &= 
    \begin{pmatrix}
        2 & 1 & 0 \\
        0 & 3 & 1 \\
        4 & 2 & 2
    \end{pmatrix}.
\end{align*}$$

(a) &emsp; Calculate $AB$.

(b) &emsp; Determine whether the matrix multiplication of $A$ and $B$ is commutative.

(c) &emsp; Calculate the determinant of $C$.

(d) &emsp; For matrix $A$, verify that $\det(A) = \det(A^\mathsf{T})$.

(e) &emsp; Calculate the inverse of $C$.

```{dropdown} Solution
(a) &emsp; 

$$ \begin{align*}
    AB &= 
    \begin{pmatrix}
        1 & 2 & 3 \\
        0 & 4 & 5 \\
        1 & 0 & 6 
    \end{pmatrix}
    \begin{pmatrix}
        7 & 8 & 9 \\
        2 & 1 & 4 \\
        3 & 6 & 5 
    \end{pmatrix}
    =
    \begin{pmatrix}
        7 + 4 +  9 & 8 + 2 + 18 & 9 +  8 + 15 \\
        0 + 8 + 15 & 0 + 4 + 30 & 0 + 16 + 25 \\
        7 + 0 + 18 & 8 + 0 + 36 & 9 +  0 + 30
    \end{pmatrix} \\
    &= 
    \begin{pmatrix}
        20 & 28 & 32 \\
        23 & 34 & 41 \\
        25 & 44 & 39
    \end{pmatrix}
\end{align*} $$

(b) &emsp; Calculate $BA$

$$ \begin{align*}
    BA &= 
    \begin{pmatrix}
        7 & 8 & 9 \\
        2 & 1 & 4 \\
        3 & 6 & 5 
    \end{pmatrix}
    \begin{pmatrix}
        1 & 2 & 3 \\
        0 & 4 & 5 \\
        1 & 0 & 6 
    \end{pmatrix}
    =
    \begin{pmatrix}
        16 & \cdot & \cdot \\
        \cdot & \cdot & \cdot \\
        \cdot & \cdot & \cdot
    \end{pmatrix}
\end{align*} $$

So $AB \neq BA$ and $A$ and $B$ do not commute.

(c) &emsp; 

$$\begin{align*}
    \det(C) &=
    \begin{pmatrix}
        2 & 1 & 0 \\
        0 & 3 & 1 \\
        4 & 2 & 2
    \end{pmatrix}
    = 
    2 \begin{vmatrix} 3 & 1 \\ 2 & 2 \end{vmatrix} -
    \begin{vmatrix} 0 & 1 \\ 4 & 2 \end{vmatrix}
    = 2(4) + 4 = 12.
\end{align*} $$

(d) &emsp;

$$\begin{align*}
    \det(A) &=
    \begin{vmatrix}
        1 & 2 & 3 \\ 
        0 & 4 & 5 \\
        1 & 0 & 6
    \end{vmatrix}
    =
    \begin{vmatrix} 4 & 5 \\ 0 & 6 \end{vmatrix} +
    \begin{vmatrix} 2 & 3 \\ 4 & 5 \end{vmatrix}
    = 24 - 2 = 22, \\
    \det(A^\mathsf{T}) &=
    \begin{vmatrix}
        1 & 0 & 1 \\
        2 & 4 & 0 \\
        3 & 5 & 6
    \end{vmatrix}
    =
    \begin{vmatrix} 4 & 0 \\ 5 & 6 \end{vmatrix} +
    \begin{vmatrix} 2 & 4 \\ 3 & 5 \end{vmatrix}
    = 24 -2 = 22 = \det(A)
\end{align*} $$

(e) &emsp;

$$\begin{align*}
    \det(C) &= 12,\\
    \adj(C) &= 
    \begin{pmatrix}
            4 &  4 & -12 \\
        -2 &  4 &   0 \\
            1 & -2 &   6
    \end{pmatrix}^\mathsf{T}
    =
    \begin{pmatrix}
        4 & -2 & 1 \\
        4 & 4 & -2 \\
        -12 & 0 & 6
    \end{pmatrix}, \\
    C^{-1} &= \frac{\adj(C)}{\det(C)} = 
    \frac{1}{12}
    \begin{pmatrix}
        4 & -2 & 1 \\
        4 & 4 & -2 \\
        -12 & 0 & 6
    \end{pmatrix}
    = 
    \begin{pmatrix}
        1/3 & -1/6 & 1/12 \\
        1/3 & 1/3 & -1/6 \\
        -1 & 0 & 1/2
    \end{pmatrix}.
\end{align*} $$
```

---

### Question 2

Consider the following system of linear equations:

$$ \begin{align*}
    2 x_1 - 3 x_2 +   x_3 &= 7, \\
    4 x_1 +   x_2 - 2 x_3 &= -1, \\
        -x_1 + 2 x_2 + 3 x_3 &= 3.
\end{align*} $$

(a) &emsp; Solve the system using Cramer's rule.

(b) &emsp; Solve the system using Gaussian elimination.

(c) &emsp; Calculate the inverse of the coefficient matrix using Gauss-Jordan elimination.

---

### Question 3

Let $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ and $\mathbf{x}$ be vectors in $\mathbb{R}^3$ such that

$$ \begin{align*}
    \vec{u} &= \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}, &
    \vec{v} &= \begin{pmatrix} 1 \\ 4 \\ -2 \end{pmatrix}, &
    \vec{w} &= \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, &
    \vec{x} &= \begin{pmatrix} a \\ b \\ c \end{pmatrix}.
\end{align*} $$

where $a, b, c \in \mathbb{R}$

(a) &emsp; Compute $\mathbf{u} \cdot \mathbf{v}$.

(b) &emsp; Compute $\mathbf{u} \times \mathbf{v}$.

(c) &emsp; What is the angle between $\mathbf{v}$ and $\mathbf{w}$?

(d) &emsp; For what values of $a$, $b$ and $c$ is $\mathbf{x}$ orthogonal to both $\mathbf{u}$ and $\mathbf{w}$?

(e) &emsp; Express the vector $\mathbf{y} = (1, -7, 15)$ as a linear combination of $\mathbf{u}$, $\mathbf{v}$ and $\mathbf{w}$.

---

### Question 4

Consider the points $A = (1,2,3)$, $B = (4,-1,2)$ and $C = (2, 3, -4)$ in $\mathbb{R}^3$.

(a) &emsp; Determine the vector equation of the line passing through the points $A$ and $B$ in the standard basis.

(b) &emsp; Find an equation of the plane that passes through the points $A$, $B$ and $C$.

(c) &emsp; What is the shortest distance between the point with co-ordinates $(10, -5, 3)$ and the plane from part (b)?

(d) &emsp; Find the equation of the line where the plane described by the equation $x + 2y - 3z = 4$ intersects with the plane from part (b).

---

### Question 5

Consider the vector space $V$ over the field $\mathbb{R}$ with basis vectors 

$$ \begin{align*}
    \mathbf{v}_1 &= \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, &
    \mathbf{v}_2 &= \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}.
\end{align*} $$

(a) &emsp; Determine whether the set $T = \{ \mathbf{u} \in \mathbb{R}^3 : \mathbf{u} \cdot \mathbf{v}_1 = 0 \}$ is a subspace of $\mathbb{R}^3$.

(b) &emsp; Show that the vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are linearly independent. 

(c) &emsp; Extend the set $\{ \mathbf{v}_1, \mathbf{v}_2 \}$ to a basis of $\mathbb{R}^3$. Justify your choice of the additional vector.

(d) &emsp; Find the change of basis matrix that changes from the standard basis to your basis from part (c).

(e) &emsp; Using your change of basis matrix from part (c) or otherwise, express the vector $\mathbf{u} = (1, 1, 4)$ with respect to your basis from part (c).

---

### Question 6

Let $T : \mathbb{R}^3 \to \mathbb{R}^3$ be a linear transformation defined by

$$T (x, y, z) = (2x + y - z , 3x - 4y + 2z , -x + 5y + 3z ).$$

(a) &emsp; Find the matrix $A$ that represents the linear transformation such that $T(\mathbf{u}) = A \mathbf{u}$.

(b) &emsp; Use your matrix from part (a) to determine $T (1, 2, 3)$.

(c) &emsp; Does there exist an inverse transformation $T^{-1}$ such that $T^{-1}(T(\mathbf{u})) = \mathbf{u}$? Justify your answer. If an inverse does exist, find the transformation matrix for the inverse transformation.

(d) &emsp; A point in $\mathbb{R}^2$ with co-ordinates $(1,2)$ is rotated anti-clockwise about the origin by angle $\frac{\pi}{3}$ and then translated by the vector $\mathbf{t} = (5, 2)$. Determine the single matrix that achieves the composite of the two transformations. Use your matrix to calculate the co-ordinates of the transformed point. 