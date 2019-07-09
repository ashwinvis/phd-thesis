Shallow water equations
=======================

## Governing Equations

The shallow water equations (SWE) have found utility as a academic tool to study
and explain numerous fundamental geophysical wave phenomena [see chapter 3,
@vallis_atmospheric_2017] and also as the "dynamical core" of some numerical
weather prediction models [for eg., flux vector splitting scheme based on
@lin_explicit_1997 was used in NOAA's GFS model until very recently][^FV3].
The governing equations for a single layer shallow layer of fluid are:
\begin{align}
    \label{eq:dtu0} \partial_t \mathbf{u} & = - (\mathbf{u}.\nabla) \mathbf{u}
    - c^2 \nabla h - f\mathbf{e_z} \times \mathbf{u} \\
    \label{eq:dth} \partial_t h         & = - \nabla. (h \mathbf{u})
\end{align}
where $\bf u$ is two-dimensional horizontal velocity vector, $h$ is the
non-dimensional scalar height field, $c$ is the phase speed of gravity waves,
$f$ is the system rotation responsible for the Coriolis force. [@Eq:dtu0]
conserves momentum and kinetic energy and [@eq:dth] conserves mass and
potential energy. In comparison with the QG equation which conserves
quasi-geostrophic potential vorticity, SWE permits both quasi-geostrophic
(vortices) and ageostrophic (gravity waves) modes. On one hand, QG equation is
analogous to incompressible 2D Navier-Stokes equations, and on the other hand,
the SWE system is comparable to compressible 2D Navier-Stokes equations -- due to
fact that [@eq:dth] has the same mathematical structure as the
mass-conservation equation for advection of $\rho$, and also because a Mach
number can derived from SWE
[@Baines1998;@augier_shallow_2019;@vallis_atmospheric_2017].

[^FV3]: See [https://www.gfdl.noaa.gov/fv3/](https://www.gfdl.noaa.gov/fv3/)

[@Eq:dtu0] may also be written in the *rotational form* as:
$$\label{eq:dtu}
    \partial_t \mathbf{u}
    = - \nabla |\mathbf{u}|^2/2 - c^2 \nabla h - \zeta \mathbf{\hat{e}}_z
    \times \mathbf{u}
$$
where, [$\zeta$]{acronym-label="zeta" acronym-form="singular+short"} represents
absolute vorticity, i.e. the sum of vorticity and system rotation.
Furthermore, some auxiliary equations can be derived from the SWE.  [@Eq:dtu0]
and [@eq:dth] can be combined to form an equation for the *total mass flux*,
[J]{acronym-label="J" acronym-form="singular+short"} $= h\mathbf{u}$:
$$\label{eq:dtJ}
    \partial_t \mathbf{J} = -(\mathbf{u}.\nabla)\mathbf{J} - \nabla(c^2h^2)/2 -
    \zeta \mathbf{\hat{e}}_z \times \mathbf{J} - (\nabla.
    \mathbf{J})\mathbf{u}$$
Similarly, an equation for the *displaced mass flux*, [M]{acronym-label="M"
acronym-form="singular+short"} $=
    \eta\mathbf{u}$ is: $$\label{eq:dtM}
    \partial_t \mathbf M = -(\mathbf{u}.\nabla)\mathbf{M} - \nabla(c^2\eta^2)/2 -
    \zeta \mathbf{\hat{e}}_z \times \mathbf M - (\nabla.\mathbf{u} + \nabla.\mathbf{M})\mathbf u$$
For a divergence free flow, a Poisson equation for *h* can be
formulated. Taking the divergence of [@eq:dtu0], yields the Poisson equation:
$$
    \nabla^2 h = \frac{1}{c^2} \left[ \nabla.(\zeta \mathbf{\hat{e}}_z \times \mathbf u )
        - \nabla^2 \frac{|u|^2}{2} \right]
$${#eq:poisson}
The spectral counterpart for [@eq:poisson] in tensor notation is:
$$\label{eq:poisson_fft}
    -\kappa^2 \hat{h} = \frac{1}{c^2} \left[ ik_i (\widehat{\epsilon_{ijk} \zeta_j
            u_k})
        + \kappa^2 \frac{\widehat{u_i u_i}}{2} \right]$$
where the $\widehat{\text{ }}$ denotes the Fourier transform. To study
interactions within SW turbulence it is useful to decompose the equations.
There are two possibilities: Helmholtz and normal-mode decomposition.

## Helmholtz Decomposition

The Helmholtz decomposition theorem, or the fundamental theorem of
vector calculus [@baird_helmholtz_2012], states that any well-behaved vector
field can be decomposed into the sum of a longitudinal (diverging, non-curling,
irrotational) vector field and a transverse (solenoidal, curling, rotational,
non-diverging) vector field. This allows us to express the velocity field as:
\begin{align}
    \label{eq:helm_u}
    \mathbf{u} & = -\nabla \times (\mathbf{\hat{e}}_z \Psi) + \nabla \mathbf{\Phi}
\end{align}
<!-- & =  -\nabla \times \Psi_z + \nabla \Phi -->
For the sake of clarity, we shall denote the rotational and divergent parts of
the velocity with the suffix *r* and *d* respectively,
\begin{align*}
    \mathbf{u}_r & = -\nabla \times \mathbf{\hat{e}}_z\Psi; & \mathbf{u}_d =
    \nabla {\bf \Phi}
\end{align*}
and, $\mathbf u  = \mathbf u_r + \mathbf u_d$.
To find the projection operators for the divergent parts, take the
divergence of [@eq:helm_u] giving $\nabla .\mathbf{u} = \nabla^2 {\bf \Phi}$.
This transforms into spectral space as, $i{\bf k}.\hat{\bf u} = -\kappa^2 \hat{\Phi}$, implying:
\begin{align*}
    {\hat{\bf u}}_d = & i {\bf k}\hat{\Phi} = \frac{{\bf k}.\hat{\bf u}}{\kappa^2} {\bf k}       \\
    {\hat{\bf u}}_r = & \hat{\bf u} - {\hat{\bf u}}_d
\end{align*}
where, $\kappa = |\mathbf{k}|$, magnitude of the wavenumber vector.
To obtain a similar decomposition, $h = h_r + h_d$, for the fluid depth one can
use the Poisson equation [@eq:poisson_fft]. Since Poisson equation requires a
divergence free flow, the LHS of [@eq:poisson_fft] would correspond to the
rotational part of the flow in the transformed plane, i.e.  $\hat{h}_r$.
Henceforth, the divergent part, $\hat{h}_d$ can be obtained by subtracting
$\hat{h}_r$ from $\hat{h}$. While Helmholtz decomposition is simple to compute
and provide insightful results, it would be more accurate to extract
normal-modes -- especially in the case of flows under the presence of system
rotation, where vorticity and potential vorticity deviates in meaning.

Normal mode decomposition
-------------------------

@bartello_geostrophic_1995 demonstrated an approach for decomposing the
Boussinesq equation into its normal modes. Here, we follow the same procedure
for the SWE. In order to isolate oscillating fast modes, we linearize the SWE
followed by a normal mode or eigenvector decomposition. As a result of
linearization of [@eq:dtu0] and [@eq:dth] transforms to,
\begin{align}
    \label{eq:dtu_l}
    \partial_t \mathbf u = & - c^2 \nabla \eta - f\mathbf{e_z} \times \mathbf u \\
    \label{eq:dth_l}
    \partial_t \eta =      & - \nabla.  \mathbf u\end{align}
 Taking the curl and divergence of the linearized equation for momentum
[@eq:dtu_l] gives the following evolution equations:
\begin{align}
    \partial_t \zeta =  & - f \delta
    \label{eq:dtcurl_l}                                                  \\
    \partial_t \delta = & f \zeta - c^2 \nabla^2 \eta \label{eq:dtdiv_l} \\
    \partial_t \eta =   & - \delta \label{eq:dteta_l}\end{align}
where $\zeta$ and $\delta$ are relative vorticity and divergence
respectively. Representing the dependent flow quantities in terms of Fourier
modes:
\begin{align*}
    \begin{pmatrix}
        u \\ v \\ \eta \\ \zeta \\ \delta
    \end{pmatrix} (\mathbf{r},t)
    = \int
    \begin{pmatrix}
        \hat{u} \\ \hat{v} \\ \hat{\eta} \\ \hat{\zeta} \\ \hat{\delta}
    \end{pmatrix} e^{i(\mathbf k . \mathbf{r} - \omega t)} \mathbf{dk} d\omega\end{align*}
allows us to rewrite the system of equations [@eq:dtcurl_l] to
[@eq:dteta_l] as an eigenvalue problem:
\begin{align*}
    i\omega
    \begin{Bmatrix}
        \hat{\zeta} \\ \hat{\delta} \\c\kappa\hat{\eta}
    \end{Bmatrix}
    = i
    \begin{bmatrix}
        0   & if       & 0         \\
        -if & 0        & -ic\kappa \\
        0   & ic\kappa & 0
    \end{bmatrix}
    \begin{Bmatrix}
        \hat{\zeta} \\ \hat{\delta} \\c\kappa\hat{\eta}
    \end{Bmatrix}\end{align*}
Let us define $A$ as the Hermitian matrix operating on the vector
$\mathbf{W} = \{\hat{\zeta}, \hat{\delta} ,c\kappa \hat{\eta} \}^T$ which
yields the familiar dispersion relation for the slow geostrophic mode
and fast Poincaré wave modes:
$$\omega^{(0)} = 0;\quad \omega^{(\pm)}=\pm \sigma$$ where,
$\sigma = \sqrt{f^2 + c^2\kappa^2 }$. These are the eigenvalues of the
matrix operator *A*. Since *A* is Hermitian, the corresponding
eigenvectors are orthogonal and these are normalized as follows
\begin{align*}
    \mathbf X^{(0)}_n =
    \frac{1}{\sigma}
    \begin{Bmatrix}
        -c\kappa \\ 0 \\ f
    \end{Bmatrix}; \quad
    \mathbf X^{(\pm)}_n =
    \frac{1}{\sqrt{2} \sigma}
    \begin{Bmatrix}
        f \\ \mp i\sigma \\ c\kappa
    \end{Bmatrix}\end{align*}
 Let $X_n$ be the eigenvector matrix, which follows the property
$X_n \bar{X}_n^{T}=I$. It can, then, be applied to diagonalize the
system of equations as follows:
\begin{align*}
    \partial_t \mathbf{W} =               & [A] \mathbf{W}                    \\
    \partial_t (\bar{X}_n^T \mathbf{W}) = & \bar{X}_n^T[A]X_n
    \bar{X}_n^T\mathbf{W}                                                     \\
    =                                     & [\Lambda] (\bar{X}_n^T\mathbf{W})\end{align*}
 Thus, the alternate diagonalized system of equations for the normal
modes are given by:
\begin{align*}
    \partial_t
    \mathbf{N}
    = &
    \begin{bmatrix}
        0 & 0        & 0       \\
        0 & -i\sigma & 0       \\
        0 & 0        & i\sigma
    \end{bmatrix}
    \mathbf{N}                   \\
    \text{where},
    \mathbf{N} = \bar{X}_n^T \mathbf{W}
    = & \frac{1}{\sqrt{2}\sigma}
    \begin{Bmatrix}
        -\sqrt{2}c\kappa(\hat{\zeta} -f \hat{\eta})                \\
        f\hat{\zeta} + c^2\kappa^2\hat{\eta} - i\sigma\hat{\delta} \\
        f\hat{\zeta} + c^2\kappa^2\hat{\eta} + i\sigma\hat{\delta}
    \end{Bmatrix}\end{align*}
The first mode represents *linearised potential vorticity* . The remaining two
are the *linearised ageostrophic or wave modes*. In the absence of system
rotation, i.e.  $f=0$, the normal modes are simply,
$$\label{eq:nmode}
    \mathbf{N} =
    \begin{Bmatrix}
        \hat \zeta                                              \\
        \frac{1}{\sqrt{2}} (c\kappa \hat{\eta} - i\hat{\delta}) \\
        \frac{1}{\sqrt{2}} (c\kappa \hat{\eta} + i\hat{\delta})
    \end{Bmatrix}$$

<!-- ### Following Farge & Sadourny 1989 -->
<!--  -->
<!-- Instead of finding the normal modes for the vorticity, divergence and -->
<!-- displacement field of the flow, we shall make use of the Helmholtz -->
<!-- decomposition described in [@eq:helm_u]. The shallow water equations -->
<!-- then transform to: -->
<!-- \begin{align} -->
<!--     \partial_t \psi = & f \phi -->
<!--     \label{eq:dtpsi_l}                                        \\ -->
<!--     \partial_t \phi = & -f \psi - c^2 \eta \label{eq:dtphi_l} \\ -->
<!--     \partial_t \eta = & - \nabla^2 \phi \label{eq:dteta_l2}\end{align} -->
<!--  where $\psi$ and $\psi$ are stream function and velocity potential as -->
<!-- functions of $\mathbf{r}$ and $t$ respectively. By substituting the -->
<!-- dependent variables with the respective Fourier transform, this reduces -->
<!-- to the eigenvalue problem: -->
<!-- \begin{align*} -->
<!--     i\omega -->
<!--     \begin{Bmatrix} -->
<!--         \hat{\psi} \\ \hat{\phi} \\ \hat{\eta} -->
<!--     \end{Bmatrix} -->
<!--     = i -->
<!--     \begin{bmatrix} -->
<!--         0   & if         & 0    \\ -->
<!--         -if & 0          & ic^2 \\ -->
<!--         0   & -i\kappa^2 & 0 -->
<!--     \end{bmatrix} -->
<!--     \begin{Bmatrix} -->
<!--         \hat{\psi} \\ \hat{\phi} \\ \hat{\eta} -->
<!--     \end{Bmatrix}\end{align*} -->
<!--  the square matrix is not Hermitian and this would result in complex -->
<!-- eigenvalues. By adopting the following change of variables: -->
<!-- $$\hat{\psi} \to \kappa^2\hat \psi = \hat{\zeta} ; \quad -->
<!--     \hat{\phi} \to -\kappa^2\hat \phi = \hat{\delta}; \quad -->
<!--     \hat{\eta} \to c\kappa\hat \eta$$ it falls back to the previous -->
<!-- eigenvalue problem as demonstrated in the previous section. In other -->
<!-- words, we can use the same eigenvector matrix, $X_n$ to find the normal -->
<!-- modes of: -->
<!--  -->
<!-- $$\mathbf{H} = \{\hat \psi,\; \hat \phi,\;  \eta  \}^T$$ which is -->
<!-- closely related to: $$\mathbf{W} -->
<!--     = \{\kappa^2\hat \psi,\; -\kappa^2\hat -->
<!--     \phi,\; c\kappa\hat \eta  \}^T -->
<!--     = \{\hat \zeta;\; \hat \delta;\;  c\kappa \hat \eta \}^T$$ -->

### Normal mode inversion to primitive variables

To study spectral energy budget, normal modes have to be transformed
back to the primitive variable using another matrix operation, say $Q$.  It has
been shown before that the normal modes can be represented by $\mathbf{N} =
\bar{X}_n^T \mathbf{W}$. Now, we shall form a new vector $\mathbf{B} =
\mathbf{N}/\kappa$ which will have the same dimensions as velocity.  Thus,
\begin{align*}
    \mathbf{B}
    = & \frac{1}{\sqrt{2}\sigma}
    \begin{Bmatrix} \sqrt{2} c\left(-
        \kappa^{2} \hat \psi +  f\hat\eta \right)               \\
        \kappa \left(c^{2} \eta + f \psi + i \phi \sigma\right) \\
        \kappa \left(c^{2} \eta + f \psi - i \phi \sigma\right)
    \end{Bmatrix}\end{align*}
The vector can also be related to the primitive variable
vector, $\mathbf{U} = \{\hat{u},\hat{v},c\hat{\eta}\}^T$ using
transformation matrices as follows:
\begin{align*}
    \mathbf{B} = & \frac{1}{\kappa}[\bar{X}_n]^T W              \\
    =            & \frac{1}{\kappa}[\bar{X}_n]^T [P] \mathbf{U}\end{align*}
 where, $$P=
    \begin{bmatrix}- i k_{y} & i k_{x} & 0 \\ i k_{x} &  i
        k_{y}     &
        0                       \\0 & 0 & \kappa\end{bmatrix}$$ It is
also straightforward to show that the magnitude of the normal modes
equals the total energy as:
\begin{align*}
    \mathbf{\bar B}^T\mathbf{B}
    = & \frac{1}{\kappa^2} \mathbf{\bar U}^T
    [\bar P]^T[{X}_n]  [\bar{X}_n]^T [P] \mathbf{U} \\
    = & \mathbf{\bar U}^T\mathbf{U}\end{align*}
 implying,
 $$(E_K+E_P)=\frac{1}{2}\sum_i B^{(i)}{B}^{*(i)}=
 \frac{1}{2}\kappa^{2}(\psi {\psi}^* +\kappa^{2} \phi {\phi}^* + c^{2} \eta {\eta}^*)
    = \frac{1}{2}(uu* + vv* + c^2\eta\eta*)$$ This allows us to
represent the primitive variables in terms of normal modes as
$$\mathbf{U} = [Q]\mathbf{B}$$ where, the inversion matrix is
\begin{align*}
    Q
    = & \kappa [P]^{-1}[\bar{X}_n]^{T^{-1}} \\
    = & \frac{1}{\sqrt{2}\sigma\kappa}
    \begin{bmatrix}
        -i\sqrt{2}c\kappa  k_{y}                    &
        \left(i f k_{y} +
        k_{x}   \sigma\right)                       &
        \left(i f k_{y} - k_{x} \sigma\right)         \\
        i \sqrt{2}c\kappa k_{x}                     &
        \left(-  i f k_{x} +  k_{y}   \sigma\right) &
        - \left(i f  k_{x} + k_{y} \sigma\right)      \\
        \sqrt{2}\kappa f                            &
        c\kappa^{2}                                 &
        c\kappa^{2}
    \end{bmatrix}\end{align*}
 In tensor notation,
\begin{align*}
    \hat{u}_l =   & \epsilon_{lm3} ik_m\left[ -\frac{c}{\sigma} B^{(0)} +
        \frac{f}{\sqrt{2}\sigma\kappa} (B^{(+)} + B^{(-)})
        \right]
    + k_l \frac{1}{\sqrt{2}\kappa}  (B^{(+)} - B^{(-)})                       \\
    c\hat{\eta} = & \frac{f}{\sigma} B^{(0)} + \frac{c\kappa}{\sqrt{2}\sigma}
    (B^{(+)} + B^{(-)})\end{align*}

Spectral energy budget
----------------------

### Kinetic energy

Kinetic energy being cubic for shallow water equations, it can be split
into quadratic and non-quadratic parts as follows:
\begin{align*}
    E_K(\mathbf{r},t)
    = & h\mathbf{u}.\mathbf{u}                            \\
    = & (1+\eta)\mathbf{u}.\mathbf{u}                     \\
    = & \mathbf{u}.\mathbf{u} + \eta\mathbf{u}.\mathbf{u} \\
    = & E_K^Q + E_K^{NQ}\end{align*}

Let the rate of change of kinetic energy, without any approximations, be
written as: $$\label{eq:dtKE}
    \pder{t}E_K(\mathbf{k},t) = T_K + C_K$$ where, $T_K$ and $C_K$
represents the transfer and conversion spectral functions respectively.
Equation [@eq:dtKE] splits into:
\begin{align*}
    \pder{t}E_K^Q + \pder{t}E_K^{NQ}
    = & (T_K^{Q} + C_K^{Q}) + (T_K^{NQ} + C_K^{NQ})\end{align*}

#### Quadratic K.E. budget:

Consider the rate of change of quadratic kinetic energy,
$$\label{eq:dtKE2}
    \pder{t}E_K^{Q}(\mathbf{k},t) = T_K^{Q} + C_K^{Q}$$ Following
[@eq:dtu0], equation [@eq:dtKE2] expands into:
\begin{align*}
    \partial_t E_K^{Q}(\mathbf{k},t)
    = & \frac{1}{2}\partial_t(\mathbf{\hat u}.\mathbf{\hat u^*})       \\
    = & \frac{1}{2}\left[ \mathbf{\hat u} .\pder[\mathbf{\hat u^*}]{t}
        + \mathbf{\hat u^*}. \pder[\mathbf{\hat u}]{t}\right]          \\
    = & \frac{1}{2}\left[ -\hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        - c^2 \hat{u}_i (ik_i \hat{\eta})^*
        - \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*
        - ... \text{conjugate terms}
        \right]                                                        \\
    = & -\text{Re}\left[ \hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        + c^2 \hat{u}_i (ik_i \hat{\eta})^*
        + \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^* \right]\end{align*}
 we have,
\begin{align*}
    T_K^{Q}= & -\text{Re}\left[\hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        \right]                                                              \\
    C_K^{Q}= & -\text{Re}\left[   c^2 \hat{u}_i (ik_i \hat{\eta})^*  \right] \\
    =        & -\text{Re}\left[   c^2 \hat{u}_i^* ik_i \hat{\eta} \right]\end{align*}

#### Non-quadratic K.E. budget:


\begin{align*}
    \pder{t}E_K^{NQ}(\mathbf{k},t) = & T_K^{NQ} + C_K^{NQ}\end{align*}
 Following equations [@eq:dtu0] and [@eq:dtM] for rate of change of
velocity $\mathbf{u}$ and the displaced mass flux,
$\mathbf M = \eta \mathbf{u}$ respectively,
\begin{align*}
    \partial_t E_K^{NQ}(\mathbf{k},t)
    = & \frac{1}{2}\partial_t(\mathbf{\hat M}.\mathbf{\hat u^*})        \\
    = & \frac{1}{2}\left[ \mathbf{\hat M} .\pder[\mathbf{\hat u^*}]{t}
        + \mathbf{\hat u^*}. \pder[\mathbf{\hat M}]{t}\right]           \\
    = & \frac{1}{2}\left[-\hat{M}_i(\widehat{ u_j\partial_j u_i })^*
        - c^2 \hat{M}_i (ik_i \hat{\eta})^*
        - \hat{M}_i (\epsilon_{i3k} f \hat{u}_k)^* \right]              \\
      & +\frac{1}{2}\left[ - \hat{u}_i^* \widehat{(u_j\partial_j M_i) }
        - c^2\hat{u}_i^*ik_i\widehat{\eta\eta}/2
        - \hat{u}_i^* (\epsilon_{i3k} f \hat{M}_k)
        - \hat{u_i}^* \widehat{(u_i \partial_j({u}_j+
            M_j))}
        \right]\end{align*}
The transfer terms may be classified as follows:
\begin{align*}
    T_K^{NQ}=       & -\frac{1}{2}\left[\hat{M}_i(\widehat{ u_j\partial_j u_i })^*
        + \hat{u}_i^* \widehat{(u_j\partial_j M_i) }
        + \hat{u_i}^* \widehat{(u_i \partial_j{M}_j)}
        \right]                                                                    \\
    C_{K}^{NQ}= & -\frac{1}{2}\left[ \hat{u_i}^* \widehat{(u_i
            \partial_j{u}_j)}
        \right]                                                                    \\
    C_{P}^{NQ}= & -\frac{1}{2}\left[c^2 \hat{M}_i (ik_i \hat{\eta})^*
        + c^2\hat{u}_i^*ik_i\widehat{\eta\eta} /2
        \right]
\end{align*}
where the $T_K^{NQ}$ represents fourth order self interactions terms,
$C_K^{NQ}$ and $C_P^{NQ}$ represents exchange with quadratic K.E. and P.E.,
respectively. Numerically these terms have been observed to have a tiny, yet
non-negligible contribution in the spectral energy budget.


### Available potential energy

\begin{align*}
    \braket{ E_P}
     & = \frac{c^2}{2} \braket{ \eta^2}\end{align*}
 The spectral equivalent of which is:
\begin{align*}
    \braket{ E_P}
     & = \frac{c^2}{2} \braket{ \hat{\eta}\hat{\eta}^*}\end{align*}

Similar to equation [@eq:dtKE] we can form, $$\label{eq:dtPE}
    \pder{t}E_P(\mathbf{k},t) = T_P+ C_P$$ where, $T_P$ and $C_P$
represents the transfer and conversion spectral functions respectively.

Following [@eq:dth], equation [@eq:dtPE] expands as:
\begin{align*}
    \pder{t}E_P(\mathbf{k},t)
    = & \frac{c^2}{2}\partial_t({\hat \eta}{\hat \eta^*})                 \\
    = & \frac{c^2}{2}\left[ \hat{\eta} .\pder[\hat{\eta}^*]{t}+ \hat
        \eta^*.\pder[\hat \eta]{t}\right]                                 \\
    = & \frac{c^2}{2}\left[ - \hat{\eta} (ik_i\hat{ u_i } + ik_i\widehat{
            \eta u_i })^*
        - \hat{\eta}^* (ik_i\hat{ u_i } + ik_i\widehat{
            \eta u_i })  \right]                                          \\
    = & -\text{Re}\left[c^2\hat{\eta} (ik_i\hat{ u_i } + ik_i\widehat{
            \eta u_i })^* \right]\end{align*}
 Thus,
\begin{align*}
    T_P= & -\text{Re}\left[c^2\hat{\eta} (ik_i\widehat{
            \eta u_i })^*  \right]                                 \\
    C_P= & -\text{Re}\left[c^2\hat{\eta} (ik_i\hat{u_i })^*\right] \\
    =    & +\text{Re}\left[c^2\hat{\eta} ik_i\hat{u_i }^*\right]\end{align*}
 thus, $C^Q_K = -C_P$ which, in turn, makes the assertion that
equivalent conversion occurs between quadratic K.E. and A.P.E.

