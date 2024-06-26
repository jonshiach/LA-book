
(vector-spaces-exercises-solutions-section)=
# E. Vector Spaces Exercises Solutions

```{solution} vector-spaces-ex-R3-axioms

Let $\vec{u}, \vec{v}, \vec{w} \in \mathbb{R}^3$ and $\alpha, \beta \in \mathbb{R}$ then 

- A1: $\vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w} \checkmark$
- A2: $\vec{u} + \vec{v} = \vec{v} + \vec{u} \checkmark$
- A3: $\vec{u} + \vec{0} = \vec{u} \checkmark$
- A4: $\vec{u} + (-\vec{u}) = \vec{0} \checkmark$
- M1: $\alpha(\beta \vec{u}) = (\alpha \beta) \vec{u} \checkmark$
- M2: $1 \vec{u} = \vec{u} \checkmark$
- M3: $\alpha(\vec{u} + \vec{v}) = \alpha\vec{u} + \alpha \vec{v} \checkmark$
- M4: $(\alpha + \beta) \vec{u} = \alpha \vec{u} + \beta \vec{u} \checkmark$

All of the axioms of vector spaces hold for $\mathbb{R}^3$.
```

```{solution} vector-spaces-ex-R3-subspaces

(a) &emsp; $U$ is non-empty since $\vec{0} \in U$. Let $\vec{u} = (u_1, u_2, 0)^\mathsf{T}, \vec{v} = (v_1, v_2, 0)^\mathsf{T} \in U$ and $\alpha \in \mathbb{R}$ then

$$ \vec{u} + \alpha \vec{v} = 
    \begin{pmatrix} u_1 \\ u_2 \\ 0 \end{pmatrix} + \alpha 
    \begin{pmatrix} v_1 \\ v_2 \\ 0 \end{pmatrix} = 
    \begin{pmatrix} 
        u_1 + \alpha v_1 \\ 
        u_2 + \alpha v_2 \\ 
        0 
    \end{pmatrix} \in U, $$
therefore $U$ is a subspace.

(b) &emsp; $V$ is non-empty since $(1,2,0)^\mathsf{T} \in V$. However $\alpha (1, 2, 0)^\mathsf{T} = (\alpha , 2\alpha , 0)^\mathsf{T} \notin V$ for $\alpha \in \mathbb{R}$ so $V$ is not a subspace.

(c) &emsp; $W$ is non-empty since $\vec{0} \in W$. Let $\vec{u} = (0, u_2, 0)^\mathsf{T}, \vec{v} = (0, v_2, 0)^\mathsf{T} \in U$ and $\alpha \in \mathbb{R}$ then

$$ \vec{u} + \alpha \vec{v} = 
    \begin{pmatrix} 0 \\ u_2 \\ 0 \end{pmatrix} + \alpha 
    \begin{pmatrix} 0 \\ v_2 \\ 0 \end{pmatrix} = 
    \begin{pmatrix} 0 \\ u_2 + \alpha v_2 \\ 0 \end{pmatrix} \in W, $$

therefore $W$ is a subspace. Note that $W \subseteq U$ so since we showed $U$ is a subspace then $W$ must also be a subspace.

(d) &emsp; $X$ is not a subspace since if $\vec{u} = (1, 1, 0)^\mathsf{T}, \vec{v} = (-1, 1, 0)^\mathsf{T} \in X$ then $\vec{u} + \vec{v} = (0, 2, 0)^\mathsf{T} \notin X$.
```

```{solution} vector-spaces-ex-M2-subspaces

(a) &emsp; $A$ is non-empty since $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in A$. Let $U = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in A$ then 

$$ 2U = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \notin A, $$

so $A$ is not a subspace.

(b) &emsp; $B$ is non-empty since $0_{2\times 2} \in B$. Let $U = \begin{pmatrix} u_{11} & 0 \\ u_{11} & u_{11} \end{pmatrix}, V = \begin{pmatrix} v_{11} & 0 \\ v_{11} & v_{11} \end{pmatrix} \in B$ and $\alpha \in \mathbb{R}$ then

$$ \begin{align*}
    U + \alpha V = 
    \begin{pmatrix} u_{11} & 0 \\ u_{11} & u_{11} \end{pmatrix} + \alpha
    \begin{pmatrix} v_{11} & 0 \\ v_{11} & v_{11}\end{pmatrix}
    = \begin{pmatrix} u_{11} + \alpha v_{11} & 0 \\ u_{11} + \alpha v_{11} & u_{11} + \alpha v_{11} \end{pmatrix} \in B,
\end{align*} $$

so $B$ is a subspace.

(c) &emsp; $C$ is not a subspace since $U = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in C$ but $2U = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \notin C$.
```

```{solution} vector-spaces-R3-basis

We need to show that the vectors in the set are {prf:ref}`linearly independent<linear-dependence-definition>`.

$$ \begin{align*}
    & \left( \begin{array}{ccc|c}
        1 & 0 & -1 & 0 \\
        2 & 5 & 1 & 0 \\
        0 & 7 & 3 & 0
    \end{array} \right)
    \begin{matrix} \\ R_2 - 2R_1 \\ \phantom{x} \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccc|c}
        1 & 0 & -1 & 0 \\
        0 & 5 & 3 & 0 \\
        0 & 7 & 3 & 0
    \end{array} \right)
    \begin{matrix} \\ \frac{1}{5}R_2 \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{ccc|c}
        1 & 0 & -1 & 0 \\
        0 & 1 & 3/5 & 0 \\
        0 & 7 & 3 & 0
    \end{array} \right)
    \begin{matrix} \\ \\ R_3 - 7R_2 \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccc|c}
        1 & 0 & -1 & 0 \\
        0 & 1 & 3/5 & 0 \\
        0 & 0 & -6/5 & 0
    \end{array} \right)
    \begin{matrix} \\ \\ -\frac{5}{6}R_3 \end{matrix}  \\ \\
    \longrightarrow &
    \left( \begin{array}{ccc|c}
        1 & 0 & -1 & 0 \\
        0 & 1 & 3/5 & 0 \\
        0 & 0 & 1 & 0
    \end{array} \right)
    \begin{matrix} R_1 + R_3 \\ R_2 - \frac{3}{5}R_3 \\ \phantom{x} \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccc|c}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0
    \end{array} \right) 
\end{align*} $$

So this set of vectors is a basis for $\mathbb{R}^3$, calculating the inverse of the coefficient matrix

$$ \begin{align*}
    \det 
    \begin{pmatrix} 1 & 0 & -1 \\ 2 & 5 & 1 \\ 0 & 7 & 3 \end{pmatrix} &=
    8 - 14 = -6, \\
    \operatorname{adj}
    \begin{pmatrix} 1 & 0 & -1 \\ 2 & 5 & 1 \\ 0 & 7 & 3 \end{pmatrix} &=
    \begin{pmatrix} 8 & -6 & 14 \\ -7 & 3 & -7 \\ 5 & -3 & 5 \end{pmatrix}^\mathsf{T} =
    \begin{pmatrix} 8 & -7 & 5 \\ -6 & 3 & -3 \\ 14 & -7 & 5 \end{pmatrix}, \\
    \therefore
    \begin{pmatrix} 1 & 0 & -1 \\ 2 & 5 & 1 \\ 0 & 7 & 3 \end{pmatrix}^{-1} &=
    \frac{1}{6} \begin{pmatrix} -8 & 7 & -5 \\ 6 & -3 & 3 \\ -14 & 7 & -5 \end{pmatrix}.
\end{align*} $$

Let $U = \left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 5 \\ 7 \end{pmatrix}, \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix} \right\}$ then

$$ \begin{align*}
    \left[ \begin{pmatrix} 0 \\ 13 \\ 17 \end{pmatrix} \right]_U &= 
    \frac{1}{6} \begin{pmatrix} -8 & 7 & -5 \\ 6 & -3 & 3 \\ -14 & 7 & -5 \end{pmatrix}
    \begin{pmatrix} 0 \\ 13 \\ 17 \end{pmatrix} =
    \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, \\
    \left[ \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} \right]_U &= 
    \frac{1}{6} \begin{pmatrix} -8 & 7 & -5 \\ 6 & -3 & 3 \\ -14 & 7 & -5 \end{pmatrix}
    \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} =
    \begin{pmatrix} 0 \\ 1 \\ -2  \end{pmatrix}.
\end{align*} $$
```

```{solution} vector-spaces-ex-R4-basis

We need to find two vectors in $\mathbb{R}^4$ that are linearly independent to $(1, 1, 2, 4)^\mathsf{T}$ and $(2, -1, -5, 2)^\mathsf{T}$ and one another. Let's choose $(1, 0, 0, 0)^\mathsf{T}$ and $(0, 1, 0, 0)^\mathsf{T}$  and check for linear dependence

$$ \begin{align*}
    & \left( \begin{array}{cccc|c}
        1 & 0 & 1 & 2 & 0 \\
        0 & 1 & 1 & -1 & 0 \\
        0 & 0 & 2 & -5 & 0 \\
        0 & 0 & 4 & 2 & 0
    \end{array} \right)
    \begin{matrix} \\ \\ \frac{1}{2}R_3 \\ \phantom{x} \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{cccc|c}
        1 & 0 & 1 & 2 & 0 \\
        0 & 1 & 1 & -1 & 0 \\
        0 & 0 & 1 & -5/2 & 0 \\
        0 & 0 & 4 & 2 & 0
    \end{array} \right)
    \begin{matrix} R_1 - R_3 \\ R_2 - R_3 \\ \\ R_4 - 4R_1 \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{cccc|c}
        1 & 0 & 0 & 9/2 & 0 \\
        0 & 1 & 0 & 3/2 & 0 \\
        0 & 0 & 1 & -5/2 & 0 \\
        0 & 0 & 0 & 12 & 0
    \end{array} \right)
    \begin{matrix} \\ \\ \\ \frac{1}{12}R_4 \end{matrix}  &
    \longrightarrow &
    \left( \begin{array}{cccc|c}
        1 & 0 & 0 & 9/2 & 0 \\
        0 & 1 & 0 & 3/2 & 0 \\
        0 & 0 & 1 & -5/2 & 0 \\
        0 & 0 & 0 & 1 & 0
    \end{array} \right)
    \begin{matrix} R_1 - \frac{9}{2}R_4 \\ R_2 - \frac{3}{2}R_4 \\ R_3 + \frac{5}{2}R_4 \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{cccc|c}
        1 & 0 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 & 0
    \end{array} \right)
\end{align*} $$

Therefore $\left\{ \begin{pmatrix} 1 \\ 1 \\ 2 \\ 4 \end{pmatrix}, \begin{pmatrix} 2 \\ -1 \\ -5 \\ 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \right\}$ is a basis for $\mathbb{R}^4$. Note that we could have used any two vectors in $\mathbb{R}^4$ that form a linearly independent set of vectors.
```

```{solution} vector-spaces-ex-R4-basis-2

We need to find which of the vectors $\vec{u}$, $\vec{v}$, $\vec{w}$, $\vec{x}$ and $\vec{y}$ are linearly dependent (and therefore remove them to from the basis).

$$ \begin{align*}
    & \left( \begin{array}{ccccc|c}
        1 & 1 & 2 & 1 & 1 & 0 \\
        2 & -1 & 1 & -1 & -1 & 0 \\
        3 & 2 & 5 & 0 & 0 & 0 \\
        4 & 0 & 3 & 3 & 4 & 0
    \end{array} \right)
    \begin{matrix} \\ R_2 - 2R_1 \\ R_3 - 3R_1 \\ R_4 - 4R_1 \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 1 & 2 & 1 & 1 & 0 \\
        0 & -3 & -3 & -3 & -3 & 0 \\
        0 & -1 & -1 & -3 & -3 & 0 \\
        0 & -4 & -5 & -1 & 0 & 0
    \end{array} \right)
    \begin{matrix} \\ -\frac{1}{3}R_2 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 1 & 2 & 1 & 1 & 0 \\
        0 & 1 & 1 & 1 & 1 & 0 \\
        0 & -1 & -1 & -3 & -3 & 0 \\
        0 & -4 & -5 & -1 & 0 & 0
    \end{array} \right)
    \begin{matrix} R_1 - R_2 \\ \\ R_3 + R_2 \\ R_4 + 4R_2 \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 1 & 0 & 0 & 0 \\
        0 & 1 & 1 & 1 & 1 & 0 \\
        0 & 0 & 0 & -2 & -2 & 0 \\
        0 & 0 & -1 & 3 & 4 & 0
    \end{array} \right)
    \begin{matrix} \\ \\ R_3 \leftrightarrow R_4 \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 1 & 0 & 0 & 0 \\
        0 & 1 & 1 & 1 & 1 & 0 \\
        0 & 0 & -1 & 3 & 4 & 0 \\
        0 & 0 & 0 & -2 & -2 & 0 
    \end{array} \right)
    \begin{matrix} \\ \\ -R_3 \\ \phantom{x} \end{matrix} &
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 1 & 0 & 0 & 0 \\
        0 & 1 & 1 & 1 & 1 & 0 \\
        0 & 0 & 1 & -3 & -4 & 0 \\
        0 & 0 & 0 & -2 & -2 & 0 
    \end{array} \right)
    \begin{matrix} R_1 - R_3 \\ R_2 - R_3 \\ \phantom{x} \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 0 & 3 & 4 & 0 \\
        0 & 1 & 0 & 4 & 5 & 0 \\
        0 & 0 & 1 & -3 & -4 & 0 \\
        0 & 0 & 0 & -2 & -2 & 0 
    \end{array} \right) 
    \begin{matrix} \\  \\  \\ -\frac{1}{2}R_4 \end{matrix}  &
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 0 & 3 & 4 & 0 \\
        0 & 1 & 0 & 4 & 5 & 0 \\
        0 & 0 & 1 & -3 & -4 & 0 \\
        0 & 0 & 0 & 1 & 1 & 0 
    \end{array} \right)
    \begin{matrix} R_1 - 3 R_4 \\ R_2 - 4R_4 \\ R_3 + 3R_4 \\ \phantom{x} \end{matrix} \\ \\
    \longrightarrow &
    \left( \begin{array}{ccccc|c}
        1 & 0 & 0 & 0 & 1 & 0 \\
        0 & 1 & 0 & 0 & 1 & 0 \\
        0 & 0 & 1 & 0 & -1 & 0 \\
        0 & 0 & 0 & 1 & 1 & 0 
    \end{array} \right)
\end{align*} $$

The fifth column does not have a pivot element so $\vec{y}$ is linearly dependent on the other vectors, therefore a basis for $W$ is $\{ \vec{u}, \vec{v}, \vec{w}, \vec{x}\}$ and $\dim(W) = 4$.
```
