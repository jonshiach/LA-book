(vector-spaces-exercises-solutions-section)=

# Vector Spaces Exercise Solutions

```{solution} vector-spaces-ex-R3-axioms


Let $\mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^3$ and $\alpha, \beta \in \mathbb{R}$ then 

- A1: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w} \checkmark$
- A2: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \checkmark$
- A3: $\mathbf{u} + \mathbf{0} = \mathbf{u} \checkmark$
- A4: $\mathbf{u} + (-\mathbf{u}) = \mathbf{0} \checkmark$
- M1: $\alpha(\beta \mathbf{u}) = (\alpha \beta) \mathbf{u} \checkmark$
- M2: $1 \mathbf{u} = \mathbf{u} \checkmark$
- M3: $\alpha(\mathbf{u} + \mathbf{v}) = \alpha\mathbf{u} + \alpha \mathbf{v} \checkmark$
- M4: $(\alpha + \beta) \mathbf{u} = \alpha \mathbf{u} + \beta \mathbf{u} \checkmark$

All of the axioms of vector spaces hold for $\mathbb{R}^3$.
```
```{solution} vector-spaces-ex-R3-subspaces


(a) &emsp; $U$ is non-empty since $\mathbf{0} \in U$. Let $\mathbf{u} = (u_1, u_2, 0), \mathbf{v} = (v_1, v_2, 0) \in U$ and $\alpha \in \mathbb{R}$ then

$$ \mathbf{u} + \alpha \mathbf{v} = 
    \begin{pmatrix} u_1 \\ u_2 \\ 0 \end{pmatrix} + \alpha 
    \begin{pmatrix} v_1 \\ v_2 \\ 0 \end{pmatrix} = 
    \begin{pmatrix} 
        u_1 + \alpha v_1 \\ 
        u_2 + \alpha v_2 \\ 
        0 
    \end{pmatrix} \in U, $$
therefore $U$ is a subspace.

(b) &emsp; $V$ is non-empty since $(1,2,0) \in V$. However $\alpha (1, 2, 0) = (\alpha , 2\alpha , 0) \notin V$ for $\alpha \in \mathbb{R}$ so $V$ is not a subspace.

(c) &emsp; $W$ is non-empty since $\mathbf{0} \in W$. Let $\mathbf{u} = (0, u_2, 0), \mathbf{v} = (0, v_2, 0) \in U$ and $\alpha \in \mathbb{R}$ then

$$ \mathbf{u} + \alpha \mathbf{v} = 
    \begin{pmatrix} 0 \\ u_2 \\ 0 \end{pmatrix} + \alpha 
    \begin{pmatrix} 0 \\ v_2 \\ 0 \end{pmatrix} = 
    \begin{pmatrix} 0 \\ u_2 + \alpha v_2 \\ 0 \end{pmatrix} \in W, $$

therefore $W$ is a subspace. Note that $W \subseteq U$ so since we showed $U$ is a subspace then $W$ must also be a subspace.

(d) &emsp; $X$ is not a subspace since if $\mathbf{u} = (1, 1, 0), \mathbf{v} = (-1, 1, 0) \in X$ then $\mathbf{u} + \mathbf{v} = (0, 2, 0) \notin X$.
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
    \begin{pmatrix} 8 & -6 & 14 \\ -7 & 3 & -7 \\ 5 & -3 & 5 \end{pmatrix} =
    \begin{pmatrix} 8 & -7 & 5 \\ -6 & 3 & -3 \\ 14 & -7 & 5 \end{pmatrix}, \\
    \therefore
    \begin{pmatrix} 1 & 0 & -1 \\ 2 & 5 & 1 \\ 0 & 7 & 3 \end{pmatrix}^{-1} &=
    \frac{1}{6} \begin{pmatrix} -8 & 7 & -5 \\ 6 & -3 & 3 \\ -14 & 7 & -5 \end{pmatrix}.
\end{align*} $$

Let $U = \{(1, 2, 0), (0, 5, 7), (-1, 1, 3)\}$ then

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


We need to find two vectors in $\mathbb{R}^4$ that are linearly independent to $(1, 1, 2, 4)$ and $(2, -1, -5, 2)$ and one another. Let's choose $(1, 0, 0, 0)$ and $(0, 1, 0, 0)$  and check for linear dependence

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

Therefore $\{(1, 1, 2, 4), (2, -1, -5, 2), \mathbf{e}_1, \mathbf{e}_2 \}$ is a basis for $\mathbb{R}^4$. Note that we could have used any two vectors in $\mathbb{R}^4$ that form a linearly independent set of vectors.
```
```{solution} vector-spaces-ex-R4-basis-2


We need to find which of the vectors $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$, $\mathbf{x}$ and $\mathbf{y}$ are linearly dependent (and therefore remove them to from the basis).

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

The fifth column does not have a pivot element so $\mathbf{y}$ is linearly dependent on the other vectors, therefore a basis for $W$ is $\{ \mathbf{u}, \mathbf{v}, \mathbf{w}, \mathbf{x}\}$ and $\dim(W) = 4$.
```