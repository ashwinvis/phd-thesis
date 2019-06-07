\chapter{Shallow Water and Toy Model Equations}

Atmospheric turbulence is characterized by a wide range of scales, ranging from
the order of a few metres to several thousands of kilometres. Understanding how
energy is distributed across the spectrum, and the underlying interactions
behind the energetics are essential to improve general circulation models (GCM)
while also recognizing the limits of predictability [see
@lorenz_predictability_1969;@vallis_atmospheric_2017 pp. 433--447]. As a
general rule of thumb, as our capabilities of modelling of the smaller scales
improve, so does the predictability. This intention has motivated researchers to
further our understanding of mesoscale flows. Of particular interest is
the direction of the mesoscale cascade, which has remained an open question
for a long time [@kitamura_energy_2010]. The first section in this chapter
presents a brief account of the theoretical, experimental and computation
works attempted towards modelling the mesoscale range. The studies described
below have led us towards an emerging consensus, which favours the forward energy
cascade explanation.

Relevant to this thesis were the theoretical predictions which estimated the
vertical resolution required for reproducing the mesoscale spectra. In
@Lindborg2006 and @Waite-Bartello:2004 the vertical resolution was estimated
from the vertical length scale of the elongated structures in stratified
turbulence, i.e.  $l_v \sim u/N \approx 1 \text{km}$.
On the other hand, @Callies-Buhler-Ferrari:2016 suggested a finer resolution
would be needed to resolve the gravity waves
to resolve the elongated structures as seen in stratified turbulence
simulations.  @AugierLindborg2013, wherein this result was produced by running
a GCM using 


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
work by @Kraichnan1967 wherein a theory for a coexistence of a dual inertial
range was conjectured. The presence of a large-scale inertial range dominated
by inverse-energy cascade was predicted wherein, the energy spectra scales as
$E(k) \sim \epsilon^{2/3} k^{-5/3}$. A smaller-scale spectra characterized by
forward enstrophy cascade was also predicted, which scales as $E(k) \sim
\eta^{2/3} k^{-3}$. One way to deduce these power laws was to invoke similar
assumptions as @Kolmogorov1941. It was assumed that the $\mfivethird$ inertial
range only depends on wavenumber $k$ and mean energy dissipation rate
$\epsilon$, and likewise `the -3 range would depend on $k$ and mean enstrophy
dissipation rate $\eta$. A more formal approach relying on statistical
mechanics arguments were put forth to arrive at the same conclusion and
additionally, predict the direction of cascade.

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
the wavenumbers $p, q < k$ and similarly the range $k' \in [0, k]$ would
interact with all wavenumbers $p, q > k$. Using this as a starting point, it
was shown that one would obtain a constant energy flux $\Pi(k)$ for all $k$
when energy spectra scales with the exponent $\mfivethird$ and a constant enstrophy flux
for all $k$ when the energy spectra scales as -3.

The directions of cascade, i.e. the signs of the fluxes used in scaling the
inertial ranges, were estimated using statistical mechanics arguments [see also
@kraichnan_two-dimensional_1980]. It stated that a Gaussian initial state with
an energy spectra $E(k) = \pi k U(k)$ would reach an equilibrium distribution
which scales as $U(k)~k^{n}$  where $n \notin [0, 2]$. Therefore it implies a
bidirectional transfer of energy starting from the initial intermediate scale.

Of particular interest was also the note that while the $\mfivethird$ spectrum
could arise from local interactions, the -3 spectrum would be non-local in
nature. Kraichnan correctly identified that these results would have deep
impact in our understanding of mesoscale turbulence.

## Turbulence in atmosphere

### Quasi-Geostrophic equations

Despite the firm foundations that the theory of @Kraichnan1967 presented, a gap
left to be bridged -- to connect the ideal two-dimensional turbulence to
atmospheric turbulence. @Charney1971 pondered if it was possible to realize the
predictions at all and if so, at what limits can the atmosphere be considered
two-dimensional. It is well known that most of turbulence, especially in
planetary scales, originates from baroclinic instabilities. The effects of
rotation and stratification were not considered in @Kraichnan1967. These
"shortcomings" were addressed to some extent in @Charney1971, wherein the -3
spectra scaling was derived by analysing the so-called quasi-geostrophic (QG)
equations which conserves an approximate expression for potential vorticity:

$$ \Dt{} \left[ \nabla^2 \psi + \frac{f_0^2}{\tilde \rho}\left( \frac{\tilde \rho}{N^2}
\p_z \psi \right) + \beta y  \right] = 0 $${#eq:quasigeo}

where $\psi$ is the horizontal stream function, $f$ is the solid body rotation
speed of the frame of reference, $\tilde \rho$ is the potential density, $N$ is
the Brunt-V\text{\"a}isala frequency and $\beta \approx \p_y f$ is the beta
parameter. These equations are valid when the certain criteria are met such as:

* Rossby number $Ro < O(1)$, indicating strong rotation,
* Variations in the Coriolis force ($\beta$) are small, implying scales may not
  be as large as planetary length scales,

and some other scale restrictions [see chapter 5 in @vallis_atmospheric_2017].
Using this equation and the result that energy and QG enstrophy are a conserved
quantity it was shown that, for a sufficiently high Reynolds number flow the
energy cascade can be inhibited by the geostrophic constraint, thus behaving
like two-dimensional flow. Also the -3 scaling law was derived for the QG
equations. Observational results from @wellck_effect_1971 was then used to
demonstrate the existence of -3 spectra.

### Energy cascade in synoptic and mesoscale flows

![Left: A depiction of Kraichnan's conjecture on how at the dual energy cascade
might simultaneously occur in two-dimensional turbulence. Right: A schematic of
observed energy spectra in the atmosphere [@NastromGage1985]
](imgs/cascade.pdf){#fig:cascade}

Nowadays, it is largely agreed upon that the -3 spectra in the _synoptic_
scales (typically, for wavelengths over a thousand kilometres) are
characterized by Kraichnan-type turbulence, with a constant enstrophy flux
cascading downscale. The left plot of @fig:cascade shows how Kraichnan
anticipated the two scaling laws would coexist -- a stirring force would inject
rotational energy at intermediate scales which would then cascade towards
either extrema. In contrast to this picture, a study by @NastromGage1985, which
compiled data from over 6000 aircraft flights spanning several years, revealed
a spectra that is similar to the sketch on the right plot of @fig:cascade. One
should note that, the -3 range dominates in terms of energy and spans across
the synoptic scales, whereas a lesser yet substantial $\mfivethird$ range
characterizes the _mesoscale_ flows.

The explanation for the mechanism behind the $\mfivethird$ mesoscale spectra
has been an open question ever since, and competing theories were put forth to
address this. @Dewan:1979 analysed the energy spectrum of velocity fluctuations
in the stratosphere up to wavelength of the order of 10 kilometres, which
displayed a $\mfivethird$ scaling. It was suggested that buoyancy or internal
gravity waves, feeding on turbulent layers trapped by large scale shear flows,
could be the driving mechanism behind this non-linear cascade of energy. It was
also asserted that a Kolmogorov-type _forward_ cascade of wave scales could be
involved. This was substantiated using a simple model for a shear flow due to a
wave by @Phillips.

In two contemporary articles by @Gage:1979 and @Lilly:1983, a competing view
that the mesoscale cascade process would be similar to Kraichnan's prediction
of inverse energy cascade was presented. In the former article, the temporal
variability of winds was derived structure functions and presented as evidence
for the existence of $\mfivethird$ spectra. @Lilly:1983 studied decaying wave
in stably-stratified turbulence and its tendency to evolve into enlarged
vortices for evidence of inverse cascade. A scale based decomposition of the
Boussinesq equation into waves and vortices from @riley_direct_1981, was used
to study the interactions of waves and stratification with an initial state of
isotropic turbulence with a $k^{-2}$ spectrum. It was hypothesized that the
stratified turbulence would then transfer energy to larger scale, resulting in
a shallower $\mfivethird$ spectrum. These ideas were also revisited fairly
recently by @Xia2011 through experiments, wherein a large scale planar vortex
was forced from the small scales electromagnetically to generate a
$\mfivethird$ spectrum.

### Stratified turbulence

In the early 

The question of direction of the mesoscale energy cascade has remained an
unsettled debate for a long time [@vallgren_possible_2011-1], however today one
can say the majority of results tend to favour the forward-cascade hypothesis.

