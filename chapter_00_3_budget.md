Spectral energy budget
======================

A spectral energy budget is a statistical analysis of energy exchanges between
different forms and different scales, carried out in spectral space.
The energy flux $\Pi(\mathbf{k}, t)$ is computed by integrating a transfer function
$T(\mathbf{k'}, t)$ over all wavenumbers in the interval $[\mathbf{k},
\mathbf{k}_{max}]$. The numerical equivalent of the integration is a cumulative
sum over the wavenumbers in the same range. The range of integration and the
direction of energy flux for a positive value of $\Pi$ is depicted in
@fig:spectral_flux.
In this section, we start by deriving the transfer function for the toy model
equations. Then, we show that by combining the normal mode decomposition with
this calculation, one can distinguish interactions between different forms of
energy.

![Spectral energy flux ($\Pi$) in two dimensions, computed numerically by a
cumulative sum of the transfer function ($T$) at all scales outside (in white)
of wavenumber shell $\kappa = |\mathbf{k}|$ (in black). Only one of the quadrants in the
spectral plane is shown.
](./imgs/spectral_flux.pdf){#fig:spectral_flux width=70%}

## Kinetic energy (KE)

In the case of the SWE, kinetic energy is not quadratic, but cubic,
$E_K = h {\bf u} \cdot {\bf u} /2$. As a result, the transfer term
does not only contain cubic terms but also terms which are of fourth
order in the basic flow variables.
In turbulence studies, we conventionally encounter a quadratic
expression for KE and a cubic expression for the transfer function. It was
observed while performing the study on SWE [@augier_shallow_2019] that the
contribution from the fourth-order transfer terms were small but not
negligible. This complicates the interpretation of the spectral energy budget in
the case of the SWE. In the toy model, the analysis is greatly simplified since
the expression for energy is quadratic. To identify the transfer terms, we
start from the governing equations for the toy model. The rate of
change of kinetic energy can be calculated from [@eq:toy],
\begin{align*}
    &\partial_t E_K(\mathbf{k},t) \\
    &= \frac{1}{2}\pder{t}(\mathbf{\hat u}.\mathbf{\hat u^*})
     = \frac{1}{2}\left[ \mathbf{\hat u} \cdot\pder[\mathbf{\hat u^*}]{t}
        + \mathbf{\hat u^*}\cdot \pder[\mathbf{\hat u}]{t}\right]          \\
    &= \frac{1}{2}\left[ -\hat{u}_i (\widehat{ u_j^r\partial_j u_i })^*
        - c \hat{u}_i (ik_i \hat{\theta})^*
        - \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*
        - ... \text{hermitian conjugate terms}  \right] \\
    &= -\Re\left[ \hat{u}_i (\widehat{ u^r_j\partial_j u_i })^*
        + c \hat{u}_i (ik_i \hat{\theta})^*
        + \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^* \right],
\end{align*}
where $^*$ represents the hermitian conjugate, and $u_j^r$ represents the
rotational component of the velocity, computed using the Helmholtz decomposition.
The last term $\hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*$ is zero due to
the fact that velocity is always perpendicular to the Coriolis acceleration.
Thus the rate of change of KE, without any approximations can be written as:
\begin{equation}
\label{eq:dtKE}
    \pder{t}E_K(\mathbf{k},t) = T_K + C_K,
\end{equation}
where $T_K$ and $C_K$ represent the transfer and conversion spectral
functions respectively,
\begin{align}
    \label{eq:TK}
    T_K= & -\Re\left[\hat{u}_i (\widehat{ u^r_j\partial_j u_i })^* \right]
         = -\Re\left[\hat{u}_i^* ik_j \widehat{u^r_j u_i}\right]
         =  \Im\left[\hat{u}_i^* k_j \widehat{u^r_j u_i}\right] ,\\
    \label{eq:CK}
    C_K= & -\Re\left[c \hat{u}_i (ik_i \hat{\theta})^*  \right]
          = \Re\left[c \hat{\theta} (ik_i \hat{u}_i)^* \right]
          = \Re\left[c \kappa^2 \hat{\theta}\hat{\chi}^*\right].
\end{align}
In @eq:TK the property that $\Re(iz) = -\Im(z)$ is used. In @eq:CK, the
property that Fourier transforms of real functions are hermitian is used
[@bracewell_fourier_2014]. In [@eq:TK;@eq:CK] the property that rotational
velocity is divergence-free is also used. The conversion function $C_K$
represents the energy converted from APE into KE.

## Available potential energy (APE)
Available potential energy is defined as
$$
     E_A(\mathbf{r}, t) = \frac{1}{2} { \theta^2 }.
$$
By @eq:toy_theta, the rate of change of APE is given by,
\begin{align*}
    \pder{t}E_A(\mathbf{k},t)
    = & \frac{1}{2}\pder{t}({\hat \theta}{\hat \theta^*})
    =  \frac{1}{2}\left[ \hat{\theta} .\pder[\hat{\theta}^*]{t}+ \hat
        \theta^*.\pder[\hat \theta]{t}\right]                                 \\
    = & \frac{1}{2}\left[
        - \hat{\theta} (ik_i\hat{ u_i } + ik_i\widehat{ \theta u^r_i })^*
        - \hat{\theta}^* (ik_i\hat{ u_i } + ik_i\widehat{ \theta u^r_i })  \right]
    \\
    = & -\Re\left[\hat{\theta} (ik_i\hat{ u_i } + ik_i\widehat{
            \theta u^r_i })^* \right].
\end{align*}
Similar to equation [@eq:dtKE] we write,
$$
\label{eq:dtPE}
    \pder{t}E_A(\mathbf{k},t) = T_A + C_A,
$$
where $T_A$ and $C_A$ represent the transfer and conversion spectral
functions of APE. Thus,
\begin{align}
    \label{eq:TP}
    T_A= & -\Re\left[\hat{\theta} (ik_i\widehat{ \theta u^r_i })^*  \right]
         = -\Re\left[\hat{\theta}^* ik_j \widehat{u^r_j \theta}\right]
         =  \Im\left[\hat{\theta}^* k_j \widehat{u^r_j \theta}\right] ,\\
    \label{eq:CP}
    C_A= & -\Re\left[c\hat{\theta} (ik_i\hat{u_i })^*\right]
         = -\Re\left[c \kappa^2 \hat{\theta}\hat{\chi}^*\right].
\end{align}
Comparing @eq:CP with @eq:CK, we see that $C_K = -C_A$, from which we can
assert that, equivalent conversion occurs between KE and APE via these terms.

## Algorithm for computing spectral energy budget

Using the normal modes ($\bf N$ as shown in @eq:nmode) in spectral space as
input, the spectral energy budget can be computed as described below:

1. Compute the inversion matrix $Q$ using @eq:qmat.
1. Divide the normal modes vector, $\bf N$, by the magnitude of Fourier modes, $\kappa$,
   to obtain $\bf B$ (@eq:bvec).
1. Apply matrix multiplication of $Q$ on $\bf B$ (@eq:uqmatb) to obtain the normal
   mode decomposition of the primitive variables $\bf U$.
1. Take the expressions for the transfer terms, $T_K$ and $T_A$ (@eq:TK and
   @eq:TP), and expand the primitive variables $\bf U$ using the decomposition
   calculated in the previous step. The result is a linear combination of
   $B^{(0)}, B^{(+)}$ and $B^{(-)}$, the normal modes as shown in @eq:decomp_tensor_u
   and @eq:decomp_tensor_eta.
1. Compute the transfer terms using the expanded expression for primitive
   variables term-by-term. While few terms can be computed in spectral space
   ($C_K, C_A$), where derivatives are involved ($T_K, T_A$) a couple of FFT and
   inverse FFT would have to be used.
1. Classify the expanded transfer terms into four groups based on the kind of
   normal modes they are product of: $T_{VVV}, T_{VVW}, T_{VWW}$ and $T_{WWW}$,
   where the subscript $V$ represents a potential vorticity mode
   $B^{(0)}$, and $W$ represents a wave mode, $B^{(+)}$ or $B^{(-)}$. The classification
   does not take into account the order in which
   the modes appear (i.e., combinations are noted, and not permutations).
1. Store transfer terms for every time instant as a one-dimensional array in
   $\kappa$ by taking sum along circular wavenumbers shells.
1. After the simulation, load the series of transfer terms. Take a cumulative sum
   along $\kappa$, which would give the instantaneous spectral energy flux
   $\Pi(\kappa, t)$.
1. Take a time average of $\Pi(\kappa, t)$ over the interval when the simulation
   had reached a statistically, stationary state to get the desired spectral
   energy flux, $\Pi(\kappa)$ decomposed in groups.

