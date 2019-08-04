Shallow water equations
=======================

## Governing Equations

The shallow water equations (SWE) have found utility as an academic tool to study
and explain fundamental geophysical phenomena [see chapter 3,
@vallis_atmospheric_2017] and also as the "dynamical core" of some numerical
weather prediction models [for eg., a flux vector splitting scheme based
formulation of the SWE [@lin_explicit_1997] was used in NOAA's GFS model until
recently][^FV3]. The governing equations for a single layer shallow layer
of fluid are:
\begin{align}
    \label{eq:dtu0} \partial_t \mathbf{u} & = - (\mathbf{u}.\nabla) \mathbf{u}
    - c^2 \nabla h - f\mathbf{e_z} \times \mathbf{u}, \\
    \label{eq:dth} \partial_t h         & = - \nabla \cdot (h \mathbf{u}),
\end{align}
where $\bf u$ is two-dimensional horizontal velocity vector, $c$ is the phase
speed of gravity waves, $f$ is the system rotation, $h = (1 + \eta)$ is the
non-dimensional scalar height field, and $\eta$ is surface displacement.  In
this inviscid formulation, the system of equations [@Eq:dtu0] and [@eq:dth]
conserves the sum of kinetic and potential energy, defined as $E_K = h|\bf
u|^2$ and $E_P = c^2h^2 / 2$. Expanding the expression for $E_P$ in $\eta$ we
get,
$$
E_P = c^2(1/2 + \eta + \eta^2/2).
$$
The first term is the constant background potential energy, while
the two remaining terms are the potential energy associates with
surface displacements. The second term, which is linear in $\eta$,
is conserved by @eq:dtu0. The third term, $E_A = c^2n^2/2$,
may be called available potential energy (APE), a concept introduce
by @Lorenz:1955. The SWE also conserves the sum $E_K + E_A$. As a matter of
fact, wave motions in SWE is characterized by equipartition between
kinetic and available potential energy.

The inviscid SWE has another materially conserved invariant which is potential
vorticity, $Q = (\zeta + f)/h$.
Conservation of potential vorticity is crucial to explain several
geophysical fluid motions [@vallis_atmospheric_2017].
Since $Q$ is a materially conserved quantity, so are higher powers of $Q$,
including the quadratic potential enstrophy.
From a turbulence perspective [@Warn1986;@LindborgMohanan2017], the
non-quadratic nature of potential enstrophy restricts our interpretation of a
potential enstrophy cascade. However, in the limit of strong rotation or QG
limit, we can study its linearized form, $q = \zeta - f\eta$, which is
approximately conserved.

In comparison with the QG equation which conserves quasi-geostrophic
potential vorticity, the SWE permits both quasi-geostrophic (vortices) and
ageostrophic (gravity waves) modes. On the one hand, the QG equation is similar to
the incompressible 2D Navier-Stokes equations, and on the other hand, the SWE
system has some similarities with the compressible 2D Navier-Stokes equations
-- due to fact that [@eq:dth] has the same mathematical structure as the
mass-conservation equation for advection of density $\rho$, and because shock
waves are produced in the SWE
[@Baines1998;@augier_shallow_2019;@vallis_atmospheric_2017].

[^FV3]: See [https://www.gfdl.noaa.gov/fv3/](https://www.gfdl.noaa.gov/fv3/)

[@Eq:dtu0] may also be written in the *rotational form* as:
$$\label{eq:dtu}
    \partial_t \mathbf{u}
    = - \nabla |\mathbf{u}|^2/2 - c^2 \nabla h - \zeta \mathbf{\hat{e}}_z
    \times \mathbf{u},
$$
where, [$\zeta$]{acronym-label="zeta" acronym-form="singular+short"} represents
absolute vorticity, i.e. the sum of vorticity and system rotation.
Furthermore, some auxiliary equations are derived from the SWE.  [@Eq:dtu0]
and [@eq:dth] can be combined to form an equation for the *total mass flux*,
[J]{acronym-label="J" acronym-form="singular+short"} $= h\mathbf{u}$:
$$\label{eq:dtJ}
    \partial_t \mathbf{J} = -(\mathbf{u}.\nabla)\mathbf{J} - \nabla(c^2h^2)/2 -
    \zeta \mathbf{\hat{e}}_z \times \mathbf{J} - (\nabla.
    \mathbf{J})\mathbf{u}.
$$
For a divergence free flow, a Poisson equation for *h* can be
formulated. Taking the divergence of [@eq:dtu0], yields the Poisson equation:
$$
    \nabla^2 h = \frac{1}{c^2} \left[ \nabla.(\zeta \mathbf{\hat{e}}_z \times \mathbf u )
        - \nabla^2 \frac{|u|^2}{2} \right].
$${#eq:poisson}
The spectral counterpart for [@eq:poisson] in tensor notation is:
$$
    -\kappa^2 \hat{h} = \frac{1}{c^2} \left[ ik_i (\widehat{\epsilon_{ijk} \zeta_j
            u_k})
        + \kappa^2 \frac{\widehat{u_i u_i}}{2} \right],
$${#eq:poisson_fft}
where the $\widehat{\text{ }}$ denotes the Fourier transform. To study
interactions within SW turbulence it is useful to decompose the flow field. We
consider two decompositions: the Helmholtz and the normal-mode decomposition.

## Helmholtz Decomposition

The fundamental theorem of vector calculus [@baird_helmholtz_2012] states that
any well-behaved vector field can be decomposed into the sum of an irrotational
vector field and a rotational or non-divergent vector field. This allows us to
express the velocity field as:
\begin{align}
    \label{eq:helm_u}
    \mathbf{u} & = -\nabla \times (\mathbf{\hat{e}}_z \Psi) + \nabla \mathbf{\Phi}.
\end{align}
<!-- & =  -\nabla \times \Psi_z + \nabla \Phi -->
For the sake of clarity, we shall denote the rotational and divergent parts of
the velocity with the suffix *r* and *d* respectively,
$$
    \mathbf{u}^r & = -\nabla \times \mathbf{\hat{e}}_z\Psi, \quad \mathbf{u}^d =
    \nabla {\bf \Phi}.
$$
<!-- and, $\mathbf u  = \mathbf u^r + \mathbf u^d$. -->
To find the projection operator for the divergent part, take the
divergence of [@eq:helm_u], giving $\nabla \cdot \mathbf{u} = \nabla^2 {\bf \Phi}$.
This equation transforms into spectral space as $i{\bf k} \cdot \hat{\bf u} =
-\kappa^2 \hat{\Phi}$, implying:
\begin{align*}
    {\hat{\bf u}}^d = & i {\bf k}\hat{\Phi} = \frac{{\bf k}\cdot\hat{\bf u}}{\kappa^2} {\bf k},       \\
    {\hat{\bf u}}^r = & \hat{\bf u} - {\hat{\bf u}}^d,
\end{align*}
where, $\kappa = |\mathbf{k}|$, is the magnitude of the wavenumber vector.
To obtain a similar decomposition, $h = h^r + h^d$, for the fluid depth one can
use the Poisson equation [@eq:poisson_fft]. Since the Poisson equation requires a
divergence free flow, the LHS of [@eq:poisson_fft] would correspond to the
rotational part of the flow in the transformed plane, i.e.  $\hat{h}^r$.
Henceforth, the divergent part, $\hat{h}^d$ can be obtained by subtracting
$\hat{h}^r$ from $\hat{h}$. While the Helmholtz decomposition is simple to compute
and provide insightful results, it may be more revealing to apply a
normal-mode decomposition -- especially in the case with
system rotation, wherein potential vorticity is conserved and not vorticity.

Normal mode decomposition
-------------------------

@bartello_geostrophic_1995 demonstrated how the
Boussinesq equations can be analysed using a normal-mode decomposition.  Here,
we follow the same procedure for the SWE. In order to isolate the geostrophic
modes from the oscillating fast modes, we linearize the SWE followed by a
normal mode or eigenmode decomposition. The linearized [@eq:dtu0] and [@eq:dth]
can be written as
\begin{align}
    \label{eq:dtu_l}
    \partial_t \mathbf u = & - c^2 \nabla \eta - f\mathbf{e_z} \times \mathbf u, \\
    \label{eq:dth_l}
    \partial_t \eta =      & - \nabla \cdot  \mathbf u.
\end{align}
Taking the curl and divergence of @eq:dtu_l gives the following evolution
equations:
\begin{align}
    \partial_t \zeta =  & - f \delta \label{eq:dtcurl_l}, \\
    \partial_t \delta = & f \zeta - c^2 \nabla^2 \eta \label{eq:dtdiv_l}, \\
    \partial_t \eta =   & - \delta \label{eq:dteta_l},
\end{align}
where $\zeta$ is the relative vorticity and $\delta$ is the divergence.
Representing the dependent flow quantities in terms of Fourier modes:
\begin{align*}
    \begin{pmatrix}
        u \\ v \\ \eta \\ \zeta \\ \delta
    \end{pmatrix} (\mathbf{r},t)
    = \int
    \begin{pmatrix}
        \hat{u} \\ \hat{v} \\ \hat{\eta} \\ \hat{\zeta} \\ \hat{\delta}
    \end{pmatrix} e^{i(\mathbf k \cdot \mathbf{r} - \omega t)} \mathbf{dk} d\omega,
\end{align*}
allows us to rewrite the system of equations
[@eq:dtcurl_l;@eq:dtdiv_l;@eq:dteta_l] as an eigenvalue problem:
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
    \end{Bmatrix}.
\end{align*}
Let us define $A$ as the Hermitian matrix operating on the vector
$\mathbf{W} = \{\hat{\zeta}, \hat{\delta} ,c\kappa \hat{\eta} \}^T$ which
yields the familiar dispersion relation for the slow geostrophic mode
and fast Poincaré wave modes:
$$
\omega^{(0)} = 0,\quad \omega^{(\pm)}=\pm \sigma,
$$
where,
$\sigma = \sqrt{f^2 + c^2\kappa^2 }$. These are the eigenvalues of the
matrix operator *A*. Since *A* is Hermitian, the corresponding
eigenvectors are orthogonal and these are normalized as follows
\begin{align*}
    \mathbf X^{(0)}_n =
    \frac{1}{\sigma}
    \begin{Bmatrix}
        -c\kappa \\ 0 \\ f
    \end{Bmatrix}, \quad
    \mathbf X^{(\pm)}_n =
    \frac{1}{\sqrt{2} \sigma}
    \begin{Bmatrix}
        f \\ \mp i\sigma \\ c\kappa
    \end{Bmatrix}.
\end{align*}
Let $X_n$ be the eigenvector matrix, which follows the property $X_n X_n^*=I$,
where $^*$ represents the Hermitian transpose. It can be applied to
diagonalize the system of equations as follows:
\begin{align*}
    \partial_t \mathbf{W} =               & [A] \mathbf{W}, \\
    \partial_t (X_n^* \mathbf{W}) = & X_n^*[A]X_n
    X_n^*\mathbf{W} = [\Lambda] (X_n^*\mathbf{W}),
\end{align*}
where $\Lambda$ is the diagonal eigenvalue matrix. Thus, the alternate
diagonalized system of equations for the normal modes are given by:
\begin{align*}
    \partial_t
    \mathbf{N}
    = &
    \begin{bmatrix}
        0 & 0        & 0       \\
        0 & -i\sigma & 0       \\
        0 & 0        & i\sigma
    \end{bmatrix}
    \mathbf{N},
\end{align*}
where
\begin{align}
  \label{eq:nmode}
    \mathbf{N} = X_n^* \mathbf{W}
    = & \frac{1}{\sqrt{2}\sigma}
    \begin{Bmatrix}
        -\sqrt{2}c\kappa(\hat{\zeta} -f \hat{\eta})                \\
        f\hat{\zeta} + c^2\kappa^2\hat{\eta} - i\sigma\hat{\delta} \\
        f\hat{\zeta} + c^2\kappa^2\hat{\eta} + i\sigma\hat{\delta}
    \end{Bmatrix}.
\end{align}
The first mode represents *linearized potential vorticity*. The remaining two
are the *linearized ageostrophic or wave modes*. In the absence of system
rotation, i.e. $f=0$, the normal modes reduce to,
$$
    \mathbf{N} =
    \begin{Bmatrix}
        \hat \zeta                                              \\
        \frac{1}{\sqrt{2}} (c\kappa \hat{\eta} - i\hat{\delta}) \\
        \frac{1}{\sqrt{2}} (c\kappa \hat{\eta} + i\hat{\delta})
    \end{Bmatrix}.
$${#eq:nmode_f0}

### Normal mode inversion to primitive variables

To study the spectral energy budget, normal modes have to be transformed
back to the primitive variable using another matrix operation, say $Q$.
The normal modes can be represented by $\mathbf{N} = X_n^* \mathbf{W}$.
Now, we form a new vector $\mathbf{B} = \mathbf{N}/\kappa$ which has the same
dimension as velocity.  Thus,
\begin{align}
\label{eq:bvec}
    \mathbf{B}
    = & \frac{1}{\sqrt{2}\sigma}
    \begin{Bmatrix} \sqrt{2} c\left(-
        \kappa^{2} \hat \psi +  f\hat\eta \right)               \\
        \kappa \left(c^{2} \eta + f \psi + i \phi \sigma\right) \\
        \kappa \left(c^{2} \eta + f \psi - i \phi \sigma\right)
    \end{Bmatrix}.
\end{align}
The vector can also be related to the primitive variable
vector, $\mathbf{U} = \{\hat{u},\hat{v},c\hat{\eta}\}^T$ using
transformation matrices as follows:
\begin{align*}
    \mathbf{B} = & \frac{1}{\kappa}X_n^* \mathbf{W}, \\
    =            & \frac{1}{\kappa}X_n^* [P] \mathbf{U},
\end{align*}
where,
$$
P=
    \begin{bmatrix}- i k_{y} & i k_{x} & 0 \\ i k_{x} &  i
        k_{y}     &
        0                       \\0 & 0 & \kappa
\end{bmatrix}.
$$
It is also straightforward to show that the magnitude of the normal modes
equals the total energy as:
\begin{align*}
    \mathbf{B}^*\mathbf{B}
    = & \frac{1}{\kappa^2} \mathbf{U}^* [P]^*X_n  X_n^* [P] \mathbf{U}
    = & \mathbf{U}^*\mathbf{U},
\end{align*}
implying,
$$
(E_K+E_P)=\frac{1}{2}\sum_i B^{(i)}{B}^{*(i)}=
 \frac{1}{2}\kappa^{2}(\psi {\psi}^* +\kappa^{2} \phi {\phi}^* + c^{2} \eta {\eta}^*)
    = \frac{1}{2}(uu^* + vv^* + c^2\eta\eta^*).
$$
The primitive variables can be represented in terms of normal modes as,
$$\mathbf{U} = [Q]\mathbf{B}$${#eq:uqmatb}
where, the inversion matrix is
\begin{align}
\label{eq:qmat}
    Q
    = & \kappa [P]^{-1}{X_n}^{*^{-1}} \\
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
    \end{bmatrix}.
\end{align}
In tensor notation,
\begin{align}
    \label{eq:decomp_tensor_u}
    \hat{u}_l =   & \epsilon_{lm3} ik_m\left[ -\frac{c}{\sigma} B^{(0)} +
        \frac{f}{\sqrt{2}\sigma\kappa} (B^{(+)} + B^{(-)})
        \right]
    + k_l \frac{1}{\sqrt{2}\kappa}  (B^{(+)} - B^{(-)}),                       \\
    \label{eq:decomp_tensor_eta}
    c\hat{\eta} = & \frac{f}{\sigma} B^{(0)} + \frac{c\kappa}{\sqrt{2}\sigma}
    (B^{(+)} + B^{(-)}).
\end{align}

