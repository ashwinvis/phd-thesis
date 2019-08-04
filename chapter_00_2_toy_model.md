# Toy-model equations

The toy model was formulated as a modification of the SWE
[@LindborgMohanan2017]. Below we write the SWE equations, with the terms that
are modified highlighted in red:
$$
\frac{\partial {\bf u}} {\partial t} + \red{{\bf u}\cdot \nabla} {\bf u} +
f {\bf e}_z \times {\bf u} = -c^2 \nabla \eta,
$${#eq:swe_u}
$$
\frac{\partial \eta}{\partial t}+ \red{{\bf u} \cdot \nabla} \eta   = \red{- (1+\eta) \nabla \cdot {\bf u}}.
$${#eq:swe_eta}


- Assumption #1: Surface displacement is small compared to the mean fluid
   layer height, $\eta << 1$.  Replace $\red{-(1+\eta) \nabla \cdot  {\bf u}}$
   by $\green{-\nabla \cdot {\bf u}}$.

- Assumption #2: Velocities in the large scale are dominated by rotational
   part, $|\bf u^r| >> |\bf u^d|$. Replace $\red{{\bf u} \cdot \nabla}$ by
   $\green{{\bf u^r} \cdot \nabla}$, while allowing, $|\zeta| \sim |d|$ in
   contrast with QG where $|\zeta| >> |d|$.

Applying these two modifications on the classical shallow water equations gives
us the toy model equation, with the modifications highlighted in blue:
\begin{align}
\label{eq:toy}
\frac{\partial {\bf u}} {\partial t} + \green{{\bf u}^r\cdot \nabla} {\bf u} + f {\bf e}_z\times {\bf u} = -c \nabla \theta, \\
\label{eq:toy_theta}
\frac{\partial \theta}{\partial t}+ \green{{\bf u}^r \cdot \nabla} \theta   = -  c\green{\nabla \cdot {\bf u}}.
\end{align}
where

 * $\theta = c\eta$, replaces $\eta$
   and takes the form of potential temperature,
 * ${\bf u}^r$  is the rotational component of velocity obtained by applying
   the Helmholtz decomposition.

\noindent Compared with SWE, there are certain benefits and drawbacks. These are:

* Benefits: No shocks, KE and APE are quadratic and conserved, linearised
  potential vorticity conserved in the limit $Ro \rightarrow 0$: $q = \zeta -
  f\eta$.
* Drawbacks: Full potential vorticity $Q$ is not exactly conserved.

## Normal modes

The toy model introduces modification to the nonlinear terms and therefore, in
its linearised form, it is  identical to the linearised SWE. Hence the
eigenvalues of the system are exactly the same and thus the inversion
matrix $Q$ can be reused. However, an extra consideration should be made while
computing normal modes of rotational velocities, $u^r$ and $v^r$. When
doing this, a modified primitive variable vector should be used as input which
is, $\mathbf{U}^r = \{ \hat{u}^r, \hat{v}^r, \theta \}^T$.

The normal mode decomposition has served multiple purposes in
@LindborgMohanan2017: to reformulate the governing equations in terms of normal
modes while numerically solving the toy model, to distinguish the wave and
vortical energy spectra, and to interpret the spectral energy budget.
In the next section we describe the latter in detail.
