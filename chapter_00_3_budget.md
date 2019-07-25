Spectral energy budget
======================

### Kinetic energy

Kinetic energy being cubic for shallow water equations, it can be split
into quadratic and non-quadratic parts as follows:
\begin{align*}
    E_K(\mathbf{r},t)
    = & h\mathbf{u}\cdot\mathbf{u}                            \\
    = & (1+\eta)\mathbf{u}.\mathbf{u}                     \\
    = & \mathbf{u}\cdot\mathbf{u} + \eta\mathbf{u}\cdot\mathbf{u} \\
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
    = & \frac{1}{2}\left[ \mathbf{\hat u} \cdot\pder[\mathbf{\hat u^*}]{t}
        + \mathbf{\hat u^*}\cdot \pder[\mathbf{\hat u}]{t}\right]          \\
    = & \frac{1}{2}\left[ -\hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        - c^2 \hat{u}_i (ik_i \hat{\eta})^*
        - \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^*
        - ... \text{conjugate terms}
        \right]                                                        \\
    = & -\text{Re}\left[ \hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        + c^2 \hat{u}_i (ik_i \hat{\eta})^*
        + \hat{u}_i (\epsilon_{i3k} f \hat{u}_k)^* \right]\end{align*}
 we have,
\begin{align}
  \label{eq:Tke}
    T_K^{Q}= & -\text{Re}\left[\hat{u}_i (\widehat{ u_j\partial_j u_i })^*
        \right]                                                              \\
    C_K^{Q}= & -\text{Re}\left[   c^2 \hat{u}_i (ik_i \hat{\eta})^*  \right] \\
    =        & -\text{Re}\left[   c^2 \hat{u}_i^* ik_i \hat{\eta} \right]\end{align}

#### Non-quadratic K.E. budget:

The equation for the non-quadratic K.E. spectrum can be written as,
\begin{align*}
    \pder{t}E_K^{NQ}(\mathbf{k},t) = & T_K^{NQ} + C_K^{NQ}\end{align*}
From equations [@eq:dtu0] and [@eq:dtM], we find
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
Available potential energy is defined as
\begin{align*}
     E_P
     & = \frac{c^2}{2} { \eta^2}\end{align*}
The spectral equivalent is:
\begin{align*}
    E_P(\mathbf{k},t)
     & = \frac{c^2}{2} { \hat{\eta}\hat{\eta}^*}\end{align*}

Similar to equation [@eq:dtKE] we write the equation for $E_P$ as,
$$\label{eq:dtPE}
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
\begin{align}
  \label{eq:Tape}
    T_P= & -\text{Re}\left[c^2\hat{\eta} (ik_i\widehat{
            \eta u_i })^*  \right]                                 \\
    C_P= & -\text{Re}\left[c^2\hat{\eta} (ik_i\hat{u_i })^*\right]
\end{align}
 thus, $C^Q_K = -C_P$ which, in turn, makes the assertion that
equivalent conversion occurs between quadratic K.E. and A.P.E.


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
- Take the expressions for the transfer terms, $T_K^Q$ and $T_P$ (@eq:Tke and
  @eq:Tape), and expand the primitive variables $\bf U$ using the decomposition
  calculated in the previous step.
- Multiply the transfer terms using the expanded expression term-by-term. Note
  that some of the multiplication can be done in spectral space, and where
  derivatives are involved a couple of FFT and inverse FFT would have to be
  used.
- Group the expanded transfer terms into four groups based on the kind of
  normal modes they are composed of: $T_{VVV}, T_{VVW}, T_{VWW}$ and $T_{WWW}$
  where $V$ represent the potential vorticity mode, and $W$ represents either
  one of the wave modes. The grouping does not take into account the order in
  which the modes appear (i.e., combinations are noted, and not permutations).
* Store transfer terms for every time instant as a one-dimensional array in
  $\kappa$ by taking sum along circular wavenumbers shells.
- After the simulation load the series of transfer terms. Take a cumulative sum
  along $\kappa$ which would give the instantaneous spectral energy flux
  $\Pi(\kappa, t)$.
- Take a time average of $\Pi'(\kappa, t)$ over the interval when the simulation
  had reached a statistically, stationary state to get the desired spectral
  energy flux, $\Pi(\kappa)$ decomposed in groups.

[^viscous]: [See https://fluidsim.readthedocs.io/en/latest/generated/fluidsim.base.time_stepping.pseudo_spect.html#module-fluidsim.base.time_stepping.pseudo_spect](https://fluidsim.readthedocs.io/en/latest/generated/fluidsim.base.time_stepping.pseudo_spect.html#module-fluidsim.base.time_stepping.pseudo_spect)

