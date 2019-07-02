\chapter{Two-dimensional models of geophysical turbulence}
<!-- \chapter{Shallow Water and Toy Model Equations} -->

Atmospheric turbulence is characterized by a wide range of scales, ranging from
the order of a millimetres to several thousands of kilometres. Understanding the
underlying interactions behind the energetics are essential to improve general
circulation models (GCM) while also recognizing the limits of predictability
[see @lorenz_predictability_1969; @vallis_atmospheric_2017 pp. 433--447]. As a
general rule of thumb, as our capabilities of modelling of the small scales
improve, so does the predictability, which has motivated researchers
to advance our understanding of geophysical turbulence.

<!-- TODO: Check or replace with correct figure -->
![From left to right: power spectra of zonal and meridional winds, and
potential temperature. The meridional wind and potential temperature power
spectra are shifted by one and two decades to the right each along the horizontal
axis.
Source: @NastromGage1985](imgs/NastromGage.eps){#fig:nastromgage}

The scaling laws for the energy distribution in the atmosphere were revealed
through the wind and temperature measurements made in Global Atmospheric
Sampling Program (GASP, see @nastrom_kinetic_1984 and @NastromGage1985). In
GASP, data spanning across the globe was collected using over 6900 commercial
flights during the years 1975-79. At least 80% of the data was measured between
altitudes of 9 and 14 kilometres, near the tropopause where most of the weather
activity is concentrated. The spectra thus calculated, shown in
@fig:nastromgage, identified that there were two separate ranges: energy in a
narrow synoptic range (wavelengths between 1000 and 3000 km) scaling as
$k^{-3}$, and in the mesoscale range (wavelengths between 2 and 500 km) scaling
as \mfivethird. For wavelengths just above 500  km there is also an overlap
region where these two ranges blend.
<!--  -->
Prior to this study the $k^{-3}$ scaling was well-known [@Charney1971] and
explained using theories for two-dimensional turbulence theory
[@Kraichnan1967]. However the theoretical explanation of \mfivethird mesoscale
spectra and the direction of energy cascade has remained an unsettled debate
for several decades  [@kitamura_energy_2010; @vallgren_possible_2011-1]. Two
hypotheses -- one suggesting a forward energy cascade [@Dewan:1979] and another
suggesting an inverse energy cascade [@Gage:1979; @Lilly:1983] have been at the
heart of this debate. Alternate hypotheses were also introduced in the later
years which will be described in the forthcoming sections. We will also see why
there is an emerging consensus that the mesoscale range is the result of a
dominant forward cascade of energy into the smaller scales
[@Lindborg1999;@ChoLindborg2001].

Of particular relevance for this thesis is the theoretical prediction,
estimating the vertical resolution required for reproducing the mesoscale
spectra. In @Lindborg2006 and @Waite-Bartello:2004 the vertical resolution was
estimated from the vertical length scale of the elongated structures in
stratified turbulence, i.e. $l_v \sim u/N \approx \order{1} \text{km}$. The
hypothesis of @Callies-Buhler-Ferrari:2016 implies that an even finer
resolution, of \order{0.1} km, would be needed to resolve gravity waves and
thus the mesoscales. Contrary to these expectations, in @AugierLindborg2013,
some GCM runs reproduced the energy spectrum at mesoscales, using a coarse
vertical resolution of only 24 pressure levels. Additionally, the spectral
energy budget calculations in @AugierLindborg2013 exhibited a forward flux of
energy in the mesoscale range. This result prompted the question, why this was
possible despite the theories predicting a finer resolution requirement. In
trying to answer this question, we have simulated the most extreme case: a
quasi-two dimensional model which accommodates both waves and vortices,
equivalent to simulating a single layer of fluid.

![Comparison of the divergence fields ($\mathbf{\nabla.u}$) from a shallow
water simulation (left) and a similar toy-model simulation (right). $L_f$ is
the forcing length scale. Source:
@LindborgMohanan2017.](./paper_03_toy_model/fig9.pdf){#fig:shallow-toy}

![Average shock separation distance $(d)$ in a series of shallow water
simulations plotted against the forcing Froude number $(F_f)$. The Froude
number is inversely proportional to the wave phase-speed, $c$. The theoretical
prediction $d \propto F_f^{1/2}$ is displayed as a dashed line.  Source:
@augier_shallow_2019.
](./paper_04_shallow_water/Pyfig/fig6.eps){#fig:shock-sep width=60%}

The first candidate for this exercise was the classical shallow water
equations. Large scale wave forcing in a narrow band of wavenumbers (forcing
wavenumber, $k_f = 6\delta k$) was used to excite the flow. Consistent with the
expectations, the resulting turbulence demonstrated forward cascade. However,
the waves simulated using the shallow-water equations tends to coalesce to form
shock fronts, which dominated the cascade as shown in the left plot of
@fig:shallow-toy. The resulting cascade was weaker than what is observed at
mesoscales and the spectrum scaled as $k^{-2}$. Nevertheless, the dynamics of
shock-dominated wave turbulence caught our interest and we derived novel
scaling theories for spectra, shock separations (see @fig:shock-sep), structure
functions and other related statistics. This theory and the results were
presented in @augier_shallow_2019. The study can be potentially extended to
other domains such as acoustics and cosmology, but is unlikely to find
application in geophysical turbulence. Therefore in a second study
[@LindborgMohanan2017] we modified the shallow water equations into a toy
model, which does not cause waves to evolve into shocks and has nice properties
such as a quadratic expression for kinetic energy. In the right plot of
@fig:shallow-toy, the divergence field consists of ripples of alternative
positive and negative values, indicating that simulation results in gravity
waves and not shocks.  Another advantage of using the toy-model is that we
obtain a $k^{-5/3}$ spectrum for $k > k_f$ and spectral energy fluxes with
similar dynamics as in the GCM can be reproduced as shown in @fig:sebgcmtoy.

<div id="fig:sebgcmtoy">
![](./paper_03_toy_model/fig1.eps){width=45%}
![](./paper_03_toy_model/fig10.eps){width=37%}

A comparison of the spectral energy budgets from a GCM simulation
[@AugierLindborg2013] and a toy model simulation [@LindborgMohanan2017]. The
total spectral energy flux $\Pi$ has been decomposed into kinetic ($\Pi_K$) and
available potential energy ($\Pi_A$) energy fluxes. The conversion from
available potential energy to kinetic energy is represented by $C_{cum}$. The
kinetic energy flux is further decomposed as $\Pi_{2D}$, the flux due to
geostrophic modes and the difference $\Pi_K - \Pi_{2D}$.
</div>

In the first section in this chapter, we present a background of the theoretical,
experimental and computational attempts towards understanding mesoscale energy
cascade. The next section describes some properties of the shallow water and
toy model equations. The subsequent sections showcase some interesting results
from @augier_shallow_2019 and @LindborgMohanan2017.


# Background


## Two-dimensional turbulence

The latter half of the twentieth century presented exciting insights into how
kinetic energy is distributed among different scales in the atmosphere. Several
researchers in the 1960s found that large-scale or *synoptic* circulation in
the atmosphere and the associated kinetic energy spectra, behaves differently
when compared with well-known theories for three-dimensional (3D) homogeneous
and isotropic turbulence by Kolmogorov. It was identified through observational
evidences [@horn_analysis_1963] and later on by GCM calculations
[@wellck_effect_1971] that the energy spectrum scales as $k^{-3}$. Therefore,
the underlying mechanism is different in comparison with 3D isotropic
turbulence, in which energy spectrum scales as $k^{-5/3}$.

It was also realized that in two-dimensional turbulence, vorticity and
enstrophy conservation and the absence of vortex stretching mechanism places a
strong constraint on the cascade [see for example, @fjortoft_changes_1953].
These developments led to the seminal work by @Kraichnan1967 wherein a theory
for a coexistence of a dual inertial range was formulated. The presence of a
large-scale inertial range dominated by an inverse-energy cascade was predicted
wherein, the energy spectrum scales as $E(k) \sim \epsilon^{2/3} k^{-5/3}$,
where $\epsilon$ is the energy dissipation. At smaller-scales there is a
forward enstrophy cascade with an associated spectrum, $E(k) \sim \eta^{2/3}
k^{-3}$, where $\eta$ is the enstrophy dissipation. One way to deduce these
power laws was to invoke similar assumptions as @Kolmogorov1941. It was assumed
that the $\mfivethird$ inertial range solely depends on wavenumber $k$ and mean
energy dissipation rate $\epsilon$, and likewise the $k^{-3}$ range would
depend on $k$ and mean enstrophy dissipation rate $\eta$. A more formal
approach relying on statistical mechanics arguments was formulated to arrive at
the same conclusion and predict the direction of the cascades.

Kraichnan studied how triad interactions would act in the context of
two-dimensional turbulence, using incompressible Navier-Stokes equations, which
has two quadratic inviscid invariants, energy and enstrophy. The spectral
energy and enstrophy fluxes can be expressed as,
\begin{align}
  \Pi(k) &= \
    \frac{1}{2} \int_0^k dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_{k}^\infty dk' \int dp \int dq T(k', p, q) \
    \text{and,} \\
  Z(k) &= \
    \frac{1}{2} \int_0^k k'^2 dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_k^\infty k'^2 dk' \int dp \int dq T(k', p, q)
\end{align}
where $T$ is the energy transfer function arising from the nonlinear term in
the Navier-Stokes equations. Thus, the fluxes were analysed as two classes of
mutually exclusive interactions, the range $k' \in [k, \infty)$ would interact
with all the wavenumbers $p, q < k$ and similarly the range $k' \in [0, k]$
would interact with all wavenumbers $p, q > k$. Using this as a starting point,
it was shown that one would obtain a constant energy flux $\Pi(k)$
when energy spectra scales as $\mfivethird$ and a constant enstrophy flux
$Z(k)$ when the energy spectra scales as $k^{-3}$. The directions of cascade,
i.e. the signs of the fluxes used in scaling the inertial ranges, were then
determined using statistical mechanics arguments [see also
@kraichnan_two-dimensional_1980].

<!-- It stated that a Gaussian initial state with an energy spectra $E(k) = \pi k -->
<!-- U(k)$ would reach an equilibrium distribution which scales as $U(k)~k^{n}$ -->
<!-- where $n \notin [0, 2]$. Therefore, it implies a bidirectional transfer of -->
<!-- energy starting from the initial intermediate scale. -->
<!-- Of particular interest was also the note that while the $\mfivethird$ spectrum -->
<!-- could arise from local interactions, the $k^{-3}$ spectrum would be non-local in -->
<!-- nature. Kraichnan identified that these results would have deep -->
<!-- impact in our understanding of mesoscale turbulence. -->

## Quasi-Geostrophic equations

Despite the firm foundations that the theory of @Kraichnan1967 presented, a gap
left to be bridged -- to connect the ideal two-dimensional turbulence to
atmospheric turbulence. @Charney1971 pondered if it was possible to realize the
predictions at all and if so, at what limits can the atmosphere be considered
two-dimensional. It is well-known that most chaotic motions at planetary scales
originates from baroclinic instabilities. The effects of rotation and
stratification were not considered in @Kraichnan1967. These "shortcomings" were
addressed to some extent by @Charney1971, who derived the $k^{-3}$ spectrum by
analysing the so-called quasi-geostrophic (QG) equation conserving an
approximate expression for potential vorticity:
$$ \Dt{} \left[\nabla^2 \psi + \frac{f_0^2}{\tilde \rho}\left(\frac{\tilde \rho}{N^2}
\p_z \psi \right) + \beta y \right] = 0 $${#eq:quasigeo}
where, $\psi$ is the horizontal stream function, $f$ is the solid body rotation
speed of the frame of reference, $\tilde \rho$ is the potential density, $N$ is
the Brunt-\text{V\"ais\"al\"a} frequency and $\beta \approx \p_y f$ is the beta
parameter. This equation is valid when a certain criteria are met such as:

* Rossby number $Ro < O(1)$, indicating strong rotation,
* Variations in the Coriolis force ($\beta$) are small, implying scales may not
  be as large as planetary length scales,

\noindent and some other scale restrictions [see chapter 5 in
@vallis_atmospheric_2017]. Using this equation and the result that both energy and
QG enstrophy are a conserved quantities it was shown that, for a sufficiently
high Reynolds number flow the energy cascade can be inhibited by the
geostrophic constraint, thus behaving like a two-dimensional flow. In
particular, the $k^{-3}$ scaling law was derived for the QG equations.
Observational results from @wellck_effect_1971 was then used to confirm the
existence of the $k^{-3}$ spectrum.

## Energy cascade in synoptic and mesoscale flows

![Left: A depiction of Kraichnan's conjecture on how at the dual energy cascade
might simultaneously occur in two-dimensional turbulence. Right: A schematic of
observed energy spectra in the atmosphere [@NastromGage1985]
](imgs/cascade.pdf){#fig:cascade}

Nowadays, it is understood that the $k^{-3}$ spectrum in the _synoptic_ scales
(typically, for wavelengths over a thousand kilometres) is an example of a
Kraichnan-Charney type of turbulence, with a constant enstrophy flux cascading
downscale. The left plot of @fig:cascade shows how @Kraichnan1967 anticipated
the two scaling laws would coexist -- a "stirring force" would inject
rotational energy at intermediate scales, which would then cascade towards
small wavenumbers, while enstrophy would cascade in the opposite direction. In
contrast to this picture, a study by @NastromGage1985, which compiled data from
over 6000 aircraft flights spanning several years, revealed spectra that were
similar to the sketch on the right plot of @fig:cascade. One should note that,
the $k^{-3}$ range dominates in terms of energy and spans across the synoptic
scales, whereas a lesser yet substantial $\mfivethird$ range characterizes the
_mesoscale_ flows. @Frisch described the appearance of the \mfivethird scaling
at mesoscales as "paradoxical". For the two-dimensional turbulence
interpretation to be valid in such scales,

What the mechanism behind the $\mfivethird$ mesoscale spectra is, has been an
open question ever since, and competing theories were put forth to address
this. @Dewan:1979 analysed the energy spectrum of velocity fluctuations in the
stratosphere up to wavelength of \order{10} kilometres and suggested that
internal gravity waves, feeding on turbulent layers trapped by large scale
shear flows, could be the driving mechanism behind this non-linear cascade of
energy. He considered the mesoscale spectrum to be analogous to the ocean
spectrum reported by @garrett_space-time_1972. It was also asserted that a
Kolmogorov-type _forward_ cascade of wave scales could be involved. This was
substantiated using a simple model for a shear flow due to a wave by @Phillips.

In @Gage:1979, a competing hypothesis was formulated that the mesoscale cascade
process would be similar to Kraichnan's prediction of inverse energy cascade.
To confirm the power law, the two-point temporal structure functions of winds
was derived and applied on data from balloon sounding measurements. Through
Taylor's transformation the author linked this to the spatial structure
function equivalent of $\mfivethird$ spectrum. In a contemporary paper,
@Lilly:1983 also made a similar inference of inverse energy cascade, while
studying decaying stably-stratified turbulence and its tendency to evolve into
enlarged vortices. A scale based decomposition of the Boussinesq equation into
waves and vortices by @riley_direct_1981, was used to study the interactions of
waves and stratification with an initial state of isotropic turbulence with a
$k^{-2}$ spectrum. It was hypothesized that the stratified turbulence would
then transfer energy to larger scale, resulting in a shallower $\mfivethird$
spectrum. The inverse energy cascade was revisited by @Xia2011 through
experiments, wherein a large scale planar vortex was forced from the small
scales electromagnetically to generate a $\mfivethird$ spectrum.

@Lindborg1999 contains a detailed review of the above and other hypotheses,
proposed in the light of the @nastrom_kinetic_1984 results, along with a
discussion of their pros and cons. The two-dimensional turbulence
interpretation seems unlikely since it would require an small-scale energy
source of \order{1} km, when the mesoscale to microscale transition is observed
[@vinnichenko_kinetic_1970]. However, at this scale three-dimensional motions
are dominant. It is also unlikely that there would be a physical mechanism
acting as a sink near the synoptic to mesoscale transition range as suggested
in @gage_theoretical_1986, since the transition appears rather smooth in the
spectrum, as noted by the same authors in the GASP analysis. Nevertheless,
@Lindborg1999 argues that, it is still possible to accommodate both $k^{-3}$
and $\mfivethird$ ranges without adding a sink at intermediate scales.  He
demonstrates the possibility of a inertial range determined by both
constant-energy and enstrophy fluxes, by allowing both a large scale and a
small energy source to exists.

An important contribution introduced in @Lindborg1999 were analytical relations
for second-, third- and fourth-order structure functions for two-dimensional
turbulence. Structure functions were used instead of spectral analysis, as it
can be applied on one-dimensional non-uniform data and does not require removal
of the mean flow. These novel relations were then tested upon MOZAIC
(Measurement of Ozone by Airbus in-service aircraft) dataset to investigate
whether the power law scaling in the inertial range, the direction of the
cascade, and the intermittency can be explained within the framework of
two-dimensional turbulence theory or not. The measurements seems to indicate a
weak agreement with second-order structure relation,
$$\braket{\delta {\bf u} \cdot \delta {\bf  u}}(r) = C_u \epsilon_K^{2/3}
r^{2/3}$${#eq:structfn2}
where, $\epsilon_K$ is the kinetic energy flux. The $r^{2/3}$ scaling is
equivalent to a $k^{-5/3}$ spectrum. However, the agreement was better for
larger separations, implying that three-dimensional effects becomes influential
at smaller scales. The third order structure function relation,
$$\braket{(\delta u_L)^3} + \braket{\delta u_L(\delta  u_T)^2}(r) = 2P_S + \frac{1}{4}Q_Lr^3$${#eq:structfn3}
where $P_S$ is a small scale forcing of kinetic energy and $Q_L$ is a large
scale forcing of enstrophy, is equivalent to spectral energy fluxes and
positive values of right hand side imply inverse energy cascade and forward
enstrophy cascade.  These third order structure functions reported in
@Lindborg1999 were later on, correctly computed in @ChoLindborg2001 as a test
for both the direction of cascade and two-dimensional turbulence. The analysis
separated the data into troposphere and stratosphere and also into five
latitudinal (or zonal) bands to account for inhomogeneities. The analysis
strongly suggests that in the stratosphere, for the range $10 < r < 150$ km the
overall third order function scales as $-r$, implying forward energy cascade
and correspondence with Kolmogorov's 4/5-law for three-dimensional turbulence
[@Frisch;@augier_kolmogorov_2012-1]; and in the range $540 < r < 1400$ km the
same scales as $r^3$ with positive values, implying forward enstrophy flux. The
authors also indicate that the overall tropospheric structure function were
negative for all mesoscales, although it did not converge to follow a
particular power law. These observations are perhaps the strongest evidence for
the forward energy cascade hypothesis for the mesoscales. Next, we turn to
question of what resolution is required to reproduce the mesoscale spectrum and
associated physics.

## Stratified turbulence

Troposphere, the lowest layer of the atmosphere, is relatively (10 to 20 km)
compared to Earth's radius 6400 km. Fluid motion is predominantly horizontal,
but it is also constantly influenced by background stratification resulting
from the vertical temperature gradient.  Stratified turbulence is a discipline
of fluid mechanics which studies such flows, and the term was coined by
@Lilly:1983 for flows affected by a stable, vertical gradient in density or
temperature, resulting in quasi-horizontal motions consisting of large eddies
and gravity waves. Stratification is characterized by the
Brunt-\text{V\"ais\"al\"a} frequency, $N=\sqrt{\frac{-g}{\rho_0}
\pder[\rho(z)]{z}}$ and the Froude number based on horizontal velocity and
length scale $Fr_h = u / (Nl_h)$.  When a fluid is under geostrophic balance
(equalizing hydrostatic and Coriolis force), one would expect the horizontal
vortices to follow the Taylor-Proudman theorem
[@taylor_motion_1917;@proudman_motion_1916] which is expressed as
$\partial_z \mathbf{u} = 0$.  Yet turbulence in strongly stratified fluids have
been observed to evolve into elongated "pancake"-like horizontal layers over
time which decouple the horizontal motion, resulting in vertical variability.
Such structures are thought to be the key, distinguishing the physics behind
stratified turbulence from two-dimensional turbulence [@riley_fluid_2000].
Understanding the vertical length scales were of paramount importance to
analyse the energy transport.

<div id="fig:atmo">
![Layers of the atmosphere and typical temperature lapse with altitude (source:
UCAR)](imgs/atmosphere_layers.jpg){#fig:atmo_layer width=60%}

![Annual zonal mean potential temperature - troposphere perspective (source:
ERA-40 atlas)](imgs/pot_temp_tropo_mean.eps){#fig:atmo_tropo width=45%}
![Annual zonal mean temperature - stratosphere perspective (source: ERA-40
atlas)](imgs/temp_strato_mean.eps){#fig:atmo_strat width=45%}

Stratification in the atmosphere
</div>

The analysis of @riley_direct_1981 and @Lilly:1983, involved a scale decomposition
into waves and vortices with the latter being associated with turbulence.
However no vertical length scales were predicted as the studies were
concerned with decaying stratified turbulence. Experimental
[@fincham_energy_1996;@billant_experimental_2000] and numerical [@herring_numerical_1989]
investigations of stratified turbulence demonstrated that layered structures
can emerge from purely horizontal base flows or forcing, which implied the
vertical length scale must depend on characteristic properties of the flow.
In other words, strongly stratified flows ($Fr_h \ll 1$) with sufficiently high
Reynolds number would spontaneously undergo a shear or "zig-zag" instability with
alternating elongated pancake-like horizontal structures. 
This led @Billant2001, to propose a new theory for stratified turbulence,
wherein, the vertical length scale of the turbulence, that this instability
leads to, was postulated to scale as, $l_v = u / N$. Using this result, along
with two hypotheses: $Fr_h \ll 1$ and advective time scale based on horizontal
length scale $T = l_h / u$, the authors demonstrate that it is possible to
simplify the Boussinesq equations into a set of dimensionless equations
describing turbulence proposed in @riley_direct_1981. Furthermore, enforcing
the aspect ratio parameter $\delta = l_v / l_h = Fr_h$ at the limit of strong
stratification $Fr \to 0$, a set of self-similar reduced-order equations were
also derived, which are invariant for a group of transformations of $N, z, u_z$
and $\rho$. The implications of this seminal study was that, unlike the
explanation in @Lilly:1983, by using a vertical length scale, $l_v = u / N$ one
can derive the reduced-order system and it allows the waves and vortices to be
of comparable sizes. @Billant2001 also introduced a parameter, now known as
buoyancy Reynolds number $Re_b = Re_h Fr_h^2$ and condition $1 \ll Re_b \ll
Re_h$ for the self-similarity to hold.  These results was also reproduced in
decaying [@riley_dynamics_2003] and forced [@Waite-Bartello:2004;@Lindborg2006]
simulations of stratified turbulence. In @Lindborg2006, it was also shown that
the energy cascade is analogous to Kolmogorov's turbulence picture, and that
the spectrum is determined by the rate of dissipation and the wavenumber as:
$$E_K(k_h) = C_K \epsilon_K^{2/3} k_h^{-5/3}$${#eq:EKspectra}
$$E_P(k_h) = C_P \epsilon_K^{-1/3} \epsilon_P k_h^{-5/3}$${#eq:EPspectra}
where, $\epsilon_K$ and $\epsilon_P$ are rates of dissipation of kinetic and
potential energies respectively and the coefficients were found from
simulations to be $C_K \approx C_P \approx 0.5$. Initially an equipartition,
$E_K \sim E_P$ and $\epsilon_K \sim \epsilon_P$ was assumed and total
dissipation was expected to scale as, $\epsilon = \epsilon_K + \epsilon_P \sim
u^3 / l_h$ [@taylor_statistical_1935]. For flow structures smaller than the
Ozmidov length scale, $l_0 = \epsilon^{1/2} / N^{3/2}$, stratified turbulence
transitions to local patches of isotropic turbulence.

@Lindborg2006 argued the stratified turbulence theory can explain the mesoscale
spectra reported in @NastromGage1985 for wavelengths between 2 and 500 km.  The
spectral energy fluxes were positive for all wavenumbers in the simulations
implying a forward energy cascade as @Dewan:1979 initially anticipated.
However, with $E_K(k_h) \sim 3 E_P(k_h)$ there was no equipartition of energy,
which suggests the physical mechanism is not linear gravity waves but
nonlinear layered motions resulting from stratified turbulence. In the light
of these new results, one can say the majority of results tend to favour the
forward-cascade hypothesis. Stratified turbulence might be a possible
explanation of mesoscale spectra, but as observed from the GCM simulations of
@AugierLindborg2013, it might not be necessary to simulate a fully resolved
stratified flow to mimic its dynamics. We shall now see how a simpler shallow
water model is used in the present thesis to study geophysical turbulence.

