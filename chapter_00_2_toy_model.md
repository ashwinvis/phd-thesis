# Toy-model equations

$$\frac{\partial {\bf u}} {\partial t} + {{\bf u}\cdot \nabla} {\bf u} +  f {\bf e}_z \times {\bf u} = -c^2 \nabla \eta $${#eq:swe_u}
$$\frac{\partial \eta}{\partial t}+ {{\bf u} \cdot \nabla} \eta   = \red{- (1+\eta) \nabla \cdot {\bf u}}$${#eq:swe_eta}


1. Assumption #1: Surface displacement much smaller compared to the mean fluid layer height, $\eta << 1$.
   Replace the right hand side of the scalar equation to make it linear. Reason: \eta << 1 when Fr -> 0
   Replace $\red{-(1+\eta) \nabla \cdot  {\bf u}}$ with $\green{-\nabla \cdot {\bf u}}$.

1. Assumption #2: Velocities in the large scale are dominated by rotational
   part, $|\bf u_r| >> |\bf u_d|$.
   <!-- Use Helmoltz decomposition to make this distinction. -->
   Use Helmholtz decomposition to calculate $\bf{u}_r$, ${\bf u} = \bf{u}_r + \bf{u}_d$
   i.e. in the advection term we use rotational velocity. Reason: large scale motions dominated by rotation.
   Replace  $\red{{\bf u} \cdot \nabla}$  with $\green{{\bf u_r} \cdot \nabla}$ 

While allowing, $|\zeta| \sim |d|$ in contrast with QG where $|\zeta| >> |d|$.
Apply two modifications on the classical shallow water equations


####  The toy model equations

$$\frac{\partial {\bf u}} {\partial t} + \green{{\bf u}_r\cdot \nabla} {\bf u} + f {\bf e}_z\times {\bf u} = -c \nabla \theta $$

$$\frac{\partial \theta}{\partial t}+ \green{{\bf u}_r \cdot \nabla} \theta   = -  c\green{\nabla \cdot {\bf u}} $$

where, $\theta = c\eta$

* Pros: No shocks, KE and APE are quadratic and conserved, linearised potential vorticity conserved in the limit $Ro \rightarrow 0$: $q = \zeta - f\eta$

* Cons: Full potential vorticity $Q$ is not exactly conserved
<!-- #endregion -->

* Replaced $\eta$ with a proportional $\theta$ variable. Takes the form of potential temperature.
* Advantages and disadvantages

 * ${\bf u}_r  = -\nabla \times ( {\bf e_z} \Psi)$ is the rotational component
 * $\bf {u}_d = \nabla \chi$ is the divergent component
 
with $\Psi$ and $\chi$ being the stream function and the velocity potential respectively.
