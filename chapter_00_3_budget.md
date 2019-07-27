Spectral energy budget
======================

Spectral energy budget is a statistical analysis of the direction of energy
cascade, or in other words energy flux as a function of wavenumber and also
conversion of energy between different modes. The energy flux $\Pi$ is
computed by integrating a transfer function $T(\mathbf{k}, t)$ in all
wavenumbers in the interval $[k, k_{max}]$. The numerical equivalent of the
integration is a cumulative sum over the wavenumbers in the same range. The
range of integration and the direction of energy flux for a positive value of
$\Pi$ is depicted in @fig:spectral_flux.

![Spectral energy flux ($\Pi$) in two dimensions, computed numerically by a
cumulative sum of the transfer function ($T$) at all scales outside (in red) of
wavenumber shell $\kappa$ (in blue)$. Only one of the quadrants in the spectral
plane is shown.
](./imgs/spectral_flux.pdf){#fig:spectral_flux width=50%}

In this section, we start by deriving the transfer function for the toy model
equations. Then, we show that by combining the normal mode decomposition with
this calculation, one can distinguish interactions between different modes of
energy.

## Kinetic energy (KE)

In the case of the SWE, due to the fact that the expression for KE has a
non-quadratic expression,
$$
    E_K(\mathbf{r},t) = h\mathbf{u}\cdot\mathbf{u},
$$
it results in third- and fourth-order terms for the transfer terms, whereas
typically in turbulence studies, we conventionally encounter a quadratic
expression for KE and a cubic expression for the transfer function.  It was
observed while performing the study on SWE [@augier_shallow_2019] that the
contribution from the fourth-order transfer terms were small but not
negligible. This complicates the interpretation of spectral energy budget in
the case of the SWE.  In the toy model, the analysis is greatly simplified as
the expression for energy is quadratic:
$$
    E_K(\mathbf{r},t) = \mathbf{u}\cdot\mathbf{u}
$$
To determine what these terms are, we start from the
governing equations for the toy model. Consider the rate of change of kinetic
energy, Following [@eq:toy],
\begin{align*}
    \partial_t E_K(\mathbf{k},t)
    = & \frac{1}{2}\partial_t(\mathbf{\hat u}.\mathbf{\hat u^*})       \\
    = & \frac{1}{2}\left[ \mathbf{\hat u} \cdot\pder[\mathbf{\hat u^*}]{t}
        + \mathbf{\hat u^*}\cdot \pder[\mathbf{\hat u}]{t}\right]          \\
    = & \frac{1}{2}\left[ -\hat{u}_i (\widehat{ u_j^r\partial_j u_i })^*
        - \hat{u}_i (ik_i \hat{\theta})^*
        - \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*
        - ... \text{hermitian conjugate terms}
        \right]                                                        \\
    = & -\Re\left[ \hat{u}_i (\widehat{ u^r_j\partial_j u_i })^*
        + \hat{u}_i (ik_i \hat{\theta})^*
        + \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^* \right]
\end{align*}
where $^*$ represents the hermitian conjugate, and $u_j^r$ represents a
rotational component of the velocity computed using Helmholtz decomposition.
The last term. $\hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*$  drops out as due to
the fact that velocity is always perpendicular to the Coriolis acceleration.
Thus the rate of change of KE, without any approximations can be written as:
\begin{equation}
\label{eq:dtKE}
    \pder{t}E_K(\mathbf{k},t) = T_K + C_K
\end{equation}
where, $T_K$ and $C_K$ represents the transfer and conversion spectral
functions respectively.
\begin{align}
    \label{eq:TK}
    T_K= & -\Re\left[\hat{u}_i (\widehat{ u^r_j\partial_j u_i })^* \right] \\
    \label{eq:CK}
    C_K= & -\Re\left[   \hat{u}_i (ik_i \hat{\theta})^*  \right] \nonumber \\
       = & +\Re\left[   \hat{\theta} (ik_i \hat{u}_i)^* \right]
\end{align}
In the last step, the property that Fourier transforms of real functions are
hermitian is used [@bracewell_fourier_2014]. The conversion function $C_K$
represents the energy converted from APE into KE.

## Available potential energy (APE)
Available potential energy is defined as
$$
     E_P(\mathbf{r}, t) & = \frac{1}{2} { \theta^2 }
$$
Following [@eq:toy_theta], the rate of change of APE is given by,
\begin{align*}
    \pder{t}E_P(\mathbf{k},t)
    = & \frac{1}{2}\partial_t({\hat \theta}{\hat \theta^*})                 \\
    = & \frac{1}{2}\left[ \hat{\theta} .\pder[\hat{\theta}^*]{t}+ \hat
        \theta^*.\pder[\hat \theta]{t}\right]                                 \\
    = & \frac{1}{2}\left[
        - \hat{\theta} (ik_i\hat{ u_i } + ik_i\widehat{ \theta u^r_i })^*
        - \hat{\theta}^* (ik_i\hat{ u_i } + ik_i\widehat{ \theta u^r_i })  \right]
    \\
    = & -\Re\left[\hat{\theta} (ik_i\hat{ u_i } + ik_i\widehat{
            \theta u^r_i })^* \right]\end{align*}
Similar to equation [@eq:dtKE] we write the equation for $E_P$ as,
$$
\label{eq:dtPE}
    \pder{t}E_P(\mathbf{k},t) = T_P + C_P
$$
where, $T_P$ and $C_P$ represents the transfer and conversion spectral
functions of APE. Thus,
\begin{align}
    \label{eq:TP}
    T_P= & -\Re\left[\hat{\theta} (ik_i\widehat{ \theta u^r_i })^*  \right] \\
    \label{eq:CP}
    C_P= & -\Re\left[\hat{\theta} (ik_i\hat{u_i })^*\right]
\end{align}
Comparing @eq:CP with @eq:CK, we see that $C_K = -C_P$, with which we can
assert that, equivalent conversion occurs between KE and APE via these terms.

## Computing the spectral energy budget with normal mode decomposition

While using pseudospectral methods is advantageous to to solve the shallow
water equations in normal-modes, for a more accurate representation of the
viscous term[^viscous] and faster computation. Therefore note that the we have
the normal-modes ($\bf N$ as shown in @eq:nmode) in spectral space as the
input. The step-by-step algorithm for computing the spectral energy budget is
described below:

- Compute the inversion matrix $Q$ using @eq:qmat
- Divide the normal modes vector, $\bf N$, with the magnitude of Fourier modes, $\kappa$,
  to obtain $\bf B$ (@eq:bvec)
- Apply matrix multiplication of $Q$ on $\bf B$ (@eq:uqmatb) to obtain the normal
  mode decomposition of the primitive variables $\bf U$.
- Take the expressions for the transfer terms, $T_K$ and $T_P$ (@eq:TK and
  @eq:TP), and expand the primitive variables $\bf U$ using the decomposition
  calculated in the previous step. The result be a linear combination of
  $B^{(0)}, B^{(+)}$ and $B^{(-)}$, the normal modes as shown in @eq:decomp_tensor_u
  and @eq:decomp_tensor_eta.
- Compute the transfer terms using the expanded expression for primitive
  variables term-by-term. Note that some of the multiplication can be done in
  spectral space, and where derivatives are involved a couple of FFT and inverse
  FFT would have to be used.
- Classify the expanded transfer terms into four groups based on the kind of
  normal modes they are product of: $T_{VVV}, T_{VVW}, T_{VWW}$ and $T_{WWW}$.
  It is classified such that $V$ represent the potential vorticity mode
  $B^{(0)}$, and $W$ represents either one of the wave modes, $B^{(+)}$ or
  $B^{(-)}$. The classification does not take into account the order in which
  the modes appear (i.e., combinations are noted, and not permutations).
* Store transfer terms for every time instant as a one-dimensional array in
  $\kappa$ by taking sum along circular wavenumbers shells.
- After the simulation load the series of transfer terms. Take a cumulative sum
  along $\kappa$, which would give the instantaneous spectral energy flux
  $\Pi(\kappa, t)$.
- Take a time average of $\Pi(\kappa, t)$ over the interval when the simulation
  had reached a statistically, stationary state to get the desired spectral
  energy flux, $\Pi(\kappa)$ decomposed in groups.

[^viscous]: [See https://fluidsim.readthedocs.io/en/latest/generated/fluidsim.base.time_stepping.pseudo_spect.html#module-fluidsim.base.time_stepping.pseudo_spect](https://fluidsim.readthedocs.io/en/latest/generated/fluidsim.base.time_stepping.pseudo_spect.html#module-fluidsim.base.time_stepping.pseudo_spect)

