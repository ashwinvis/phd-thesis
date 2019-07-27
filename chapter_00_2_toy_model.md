# Toy-model equations
$$
\frac{\partial {\bf u}} {\partial t} + \red{{\bf u}\cdot \nabla} {\bf u} +
f {\bf e}_z \times {\bf u} = -c^2 \nabla \eta
$${#eq:swe_u}
$$
\frac{\partial \eta}{\partial t}+ \red{{\bf u} \cdot \nabla} \eta   = \red{- (1+\eta) \nabla \cdot {\bf u}}
$${#eq:swe_eta}


1. Assumption #1: Surface displacement much smaller compared to the mean fluid layer height, $\eta << 1$.
   Replace the right hand side of the scalar equation to make it linear.
   Reason: $\eta << 1$ when $Fr -> 0$
   Replace $\red{-(1+\eta) \nabla \cdot  {\bf u}}$ with $\green{-\nabla \cdot {\bf u}}$.

1. Assumption #2: Velocities in the large scale are dominated by rotational
   part, $|\bf u^r| >> |\bf u^d|$.
   <!-- Use Helmoltz decomposition to make this distinction. -->
   Use Helmholtz decomposition to calculate $\bf{u}^r$, ${\bf u} = \bf{u}^r + \bf{u}^d$
   i.e. in the advection term we use rotational velocity. Reason: large scale motions dominated by rotation.
   Replace  $\red{{\bf u} \cdot \nabla}$  with $\green{{\bf u^r} \cdot \nabla}$

While allowing, $|\zeta| \sim |d|$ in contrast with QG where $|\zeta| >> |d|$.
Applying these two modifications on the classical shallow water equations gives
us,
\begin{align}
\label{eq:toy}
\frac{\partial {\bf u}} {\partial t} + \green{{\bf u}^r\cdot \nabla} {\bf u} + f {\bf e}_z\times {\bf u} = -c \nabla \theta \\
\label{eq:toy_theta}
\frac{\partial \theta}{\partial t}+ \green{{\bf u}^r \cdot \nabla} \theta   = -  c\green{\nabla \cdot {\bf u}}
\end{align}
where,

 * $\theta = c\eta$, replaces $\eta$ with a proportional $\theta$ variable. Takes the form of potential temperature.
 * ${\bf u}^r$  is the rotational component of velocity obtained by applying
   the Helmholtz decomposition.

Compared with SWE, there are certain

* pros: no shocks, KE and APE are quadratic and conserved, linearised potential
* vorticity conserved in the limit $Ro \rightarrow 0$: $q = \zeta - f\eta$; and
* cons: full potential vorticity $Q$ is not exactly conserved.
<!-- #endregion -->


## Normal modes

The toy model introduces modification to the nonlinear terms and therefore, in
its linearised form it would be identical to the linearised SWE. Hence the
eigenvalues of the system would be exactly the same and thus the inversion
matrix $Q$ can be reused. However, an extra consideration should be made while
decomposing rotational velocities, $u^r$ and $v^r$. The corresponding normal
mode vector should be calculated, starting from the $\mathbf{U}^r = \{ \hat{u}^r,
\hat{v}^r, \theta \}^T$. In the next section, we shall see an application of
the normal mode decomposition to interpret the spectral energy budget.
