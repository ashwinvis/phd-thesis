\chapter{Atmospheric turbulence and Shallow Water and Toy Model Equations}

Atmospheric turbulence is characterized by a huge scale separation of fluid
motion, ranging from the order of a hundred metres to several thousands of
kilometres. The knowledge of how energy is distributed across such scales in
the atmosphere and what kind of interactions leads to the energy cascade
between large and small scales is essential to improve our general circulation
models (GCM) while also recognizing the limits of predictability [see
@lorenz_predictability_1969;@vallis_atmospheric_2017 pp. 433--447].

This chapter introduces the work done to come up with the simplest possible
model which can emulate the atmospheric kinetic energy spectrum and the
advances which motivated this study. Before we delve into the details of the
present work, let us have a look at what we already know about the atmospheric
turbulence and what are the open questions.

# Background


## Two-dimensional turbulence

The latter half of the twentieth century presented exciting insights into how
energy scales in the atmosphere. Several researchers in the 1960s found that
large-scale or *synoptic* circulation in the atmosphere, and especially the
kinetic energy spectra, behaves differently when compared with well-known
theories for three-dimensional (3D) homogeneous and isotropic turbulence by
Kolmogorov. It was identified through observational evidences
[@horn_analysis_1963] and later on by GCM calculations [@wellck_effect_1971]
that energy scales as $k^{-3}$. Such spectra imply that the underlying
mechanism is different in comparison with 3D turbulence which expects an
inertial range which scales as $k^{-5/3}$ with forward energy cascade.

Postulates were also made that in two-dimensional turbulence, vorticity and
enstrophy conservation and the absence of vortex stretching mechanism places a
strong constraint on the cascade [see for example,
@fjortoft_changes_1953;@Charney1971].  These developments led to the seminal
work by @Kraichnan1971 wherein a theory for a coexistence of a dual inertial
range was conjectured. The presence of a large-scale inertial range dominated
by inverse-energy cascade was predicted wherein, the energy spectra scales as
$E(k) \sim \epsilon^{2/3} k^{-5/3}$. A smaller-scale spectra characterized by
forward enstrophy cascade was also predicted, which scales as $E(k) \sim
\eta^{2/3} k^{-3}$. One way to deduce these power laws was to invoke similar
assumptions as @Kolmogorov1941. It was assumed that the \m53 inertial range
only depends on wavenumber $k$ and mean energy dissipation rate $\epsilon$, and
likewise the -3 range would depend on $k$ and mean enstrophy dissipation rate
$\eta$.  A more formal approach relying on statistical mechanics arguments were
put forth to arrive at the same conclusion and additionally, predict the
direction of cascade.

Kraichnan studied how triad interactions would function in the context of
two-dimensional turbulence, using incompressible Navier-Stokes equations, which
would have to conserve both energy and scalar enstrophy. The spectral energy
and enstrophy fluxes expressed as,
<!-- -->
\begin{align}
  \Pi(k) &= \
    \frac{1}{2} \int_0^k dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_{k}^\infty dk' \int dp \int dq T(k', p, q) \
    \text{and,} \\
  Z(k) &= \
    \frac{1}{2} \int_0^k k'^2 dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_k^\infty k'^2 dk' \int dp \int dq T(k', p, q)
\end{align}
<!-- -->
respectively. Thus the fluxes were analysed as two classes of mutually
exclusive interactions, the range $k' \in [k, \infty)$ would interact with all
the wavenumbers $p, q \lt k$ and similarly the range $k' \in [0, k]$ would
interact with all wavenumbers $p, q \gt k$. Using this as a starting point, it
was shown that one would obtain a constant energy flux $\Pi(k)$ for all $k$
when energy spectra scales with the exponent \m53 and a constant enstrophy flux
for all $k$ when the energy spectra scales as -3.

The direction of the cascade was determined using statistical mechanics
arguments. The transfer terms themselves do not have any bias in their sign
(implying the direction of cascade). However, it was argued that for a general
equilibrium spectrum of the form,
<!---->
\begin{equation} U(k) = 1 / (\beta k^2 + \alpha), \end{equation}
<!---->
the vorticity spectrum would scale as $2 \pi k^3 U(k)$, which means vorticity
would tend to accumulate at high wavenumbers. This would result from a forward
cascade of enstrophy, which in turn implies the transfer term at $k=1$,
$T(1,p,q)$ would be negative. This hints towards a forward enstrophy cascade
complemented by an inverse energy cascade. 

Of particular interest was also the note that while the \m53 spectrum could arise
from local interactions, the -3 spectrum would be due to non-local in nature.
Kraichnan correctly identified that these results would have deep impact in our
understanding of mesoscale turbulence.

## Turbulence in synoptic and mesoscale flows

In @Charney1971 the existence of  
