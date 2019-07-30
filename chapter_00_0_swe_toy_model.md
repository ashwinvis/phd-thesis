\chapter{Two-dimensional models of geophysical turbulence}
<!-- \chapter{Shallow Water and Toy Model Equations} -->

Atmospheric turbulence is characterized by a wide range of scales, ranging from
the order of millimetres to several thousands of kilometres. Understanding the
underlying interactions behind the energetics is essential to improve general
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
altitudes of 9 and 14 kilometres, near the tropopause. The spectra thus
calculated, shown in
@fig:nastromgage, revealed that there are two separate ranges: energy in a
narrow synoptic range (wavelengths between 1000 and 3000 km) scaling as
$k^{-3}$, and in the mesoscale range (wavelengths between 2 and 500 km) scaling
as \kfivethird. For wavelengths just above 500  km there is also an overlap
region where these two ranges blend.
<!--  -->
Prior to this study the $k^{-3}$ scaling was well-known [@Charney1971] and
explained using theories for two-dimensional turbulence theory
[@Kraichnan1967]. However the theoretical explanation of \kfivethird\ mesoscale
spectra and the direction of energy cascade has remained an unsettled debate
for several decades  [@kitamura_energy_2010; @vallgren_possible_2011-1]. Two
hypotheses -- one suggesting a forward energy cascade [@Dewan:1979] and another
suggesting an inverse energy cascade [@Gage:1979; @Lilly:1983] have been at the
heart of this debate. Alternative hypotheses were also introduced in the later
years which will be described in the forthcoming sections. In
@sec:energy, we will also see why there is an emerging consensus that
the mesoscale range is the result of a dominant forward cascade of energy into
the smaller scales [@Lindborg1999;@ChoLindborg2001].

Of particular relevance for this thesis is the theoretical prediction,
estimating the vertical resolution required for reproducing the mesoscale
spectra. In @Lindborg2006 and @Waite-Bartello:2004 the vertical resolution was
estimated from the vertical length scale of the elongated structures in
stratified turbulence, i.e. $l_v \sim u/N \approx \order{1} \text{km}$. The
hypothesis of @Callies-Buhler-Ferrari:2016 implies that an even finer
resolution, of \order{0.1} km, would be needed to resolve inertia-gravity waves and
thus the mesoscale motions. Contrary to these expectations, in @AugierLindborg2013,
some GCM runs reproduced the energy spectrum at mesoscales, using a coarse
vertical resolution of only 24 pressure levels. Additionally, the spectral
energy budget calculations in @AugierLindborg2013 exhibited a forward
energy cascade in the mesoscale range. This result prompted the question, why this was
possible despite the theories predicting a finer resolution requirement. In
trying to answer this question, we have simulated the most extreme case: a
quasi-two dimensional model which accommodates both waves and vortices,
equivalent to simulating a single layer of fluid.

The first candidate for this exercise was the classical shallow water
equations. Large scale wave forcing in a narrow band of wavenumbers (forcing
wavenumber, $k_f = 6\delta k$) was used to excite the flow. Consistent with the
expectations, shallow water dynamics exhibited a forward cascade. However,
the waves simulated using the shallow-water equations tend to coalesce to form
shock fronts. The resulting cascade was weaker
than what is observed at
mesoscales and the spectrum scaled as $k^{-2}$. Nevertheless, the dynamics of
shock-dominated wave turbulence caught our interest and we derived novel
scaling theories for spectra, shock separations, structure
functions and other related statistics. These results are
presented in @augier_shallow_2019. The study can be potentially extended to
other domains such as acoustics, but is unlikely to find straightforward
applications in geophysical turbulence. Therefore in a second study
[@LindborgMohanan2017] we modified the shallow water equations into a toy
model, which does not cause waves to evolve into shocks and has nice properties
such as a quadratic expression for kinetic energy. Another advantage of using
the toy-model is that we obtain a $k^{-5/3}$ spectrum for $k > k_f$ and similar
dynamics, when compared against the GCM results reported in @AugierLindborg2013.

In the first section in this chapter, we present a background of the theoretical,
experimental and computational attempts towards understanding the mesoscale energy
cascade. The next section describes some properties of the shallow water and
toy model equations. The subsequent sections showcase some interesting results
from @augier_shallow_2019 and @LindborgMohanan2017.


# Background


## Two-dimensional turbulence

The latter half of the twentieth century presented exciting insights into how
kinetic energy is distributed among different scales in the atmosphere.
Several researchers in the 1960s found that  energy spectra associated with
synoptic scales of motion ($\sim 1000-3000$) km are very different from
spectra of small scale three-dimensional isotropic turbulence. Through
observational evidence [@horn_analysis_1963] it and later on by GCM
calculations [@wellck_effect_1971], it was found that the energy spectrum
scales as $k^{-3}$ at synoptic scales.
Therefore, the underlying mechanism is different in comparison with 3D
isotropic turbulence, in which energy spectrum scales as $k^{-5/3}$.

It was also realized that in two-dimensional turbulence, vorticity and
enstrophy conservation places a
strong constraint on the cascade [see for example, @fjortoft_changes_1953].
This development led to the seminal work by @Kraichnan1967 wherein a theory
for a coexistence of a dual cascade was formulated. A
large scale inverse-energy cascade was predicted
wherein, the energy spectrum scales as $E(k) \sim \epsilon^{2/3} k^{-5/3}$,
where $\epsilon$ is the energy dissipation. At smaller scales there is a
forward enstrophy cascade with an associated spectrum, $E(k) \sim \eta^{2/3}
k^{-3}$, where $\eta$ is the enstrophy dissipation. One way to deduce these
power laws was to invoke similar assumptions as @Kolmogorov1941. It was assumed
that the \kfivethird\ inertial range solely depends on wavenumber $k$ and mean
energy dissipation rate $\epsilon$, and likewise the $k^{-3}$ range would
depend on $k$ and mean enstrophy dissipation rate $\eta$. A more formal
approach relying on statistical mechanics arguments was also formulated by
@Kraichnan1967 to arrive at the same conclusion and predict the direction of
the cascades.

Kraichnan studied how triad interactions would act in
two dimensions, using the incompressible Navier-Stokes equations, which
have two quadratic inviscid invariants, energy and enstrophy. The spectral
energy and enstrophy fluxes can be expressed as,
\begin{align}
  \Pi(k) &= \
    \frac{1}{2} \int_0^k dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_{k}^\infty dk' \int dp \int dq T(k', p, q) \
    \\
  Z(k) &= \
    \frac{1}{2} \int_0^k k'^2 dk' \int dp \int dq T(k', p, q) - \
    \frac{1}{2} \int_k^\infty k'^2 dk' \int dp \int dq T(k', p, q)
\end{align}
where $T$ is the energy transfer function arising from the nonlinear term in
the Navier-Stokes equations. The fluxes were found to arise from two classes of
mutually exclusive interactions, the range $k' \in [k, \infty)$ would interact
with all the wavenumbers $p, q < k$ and similarly the range $k' \in [0, k]$
would interact with all wavenumbers $p, q > k$. Using this as a starting point,
it was shown that a constant energy flux $\Pi(k)$ is obtained where the
energy spectrum scales as \kfivethird\ as well as a constant enstrophy flux
$Z(k)$ where the energy spectrum scales as $k^{-3}$. The directions of cascades,
i.e. the signs of the fluxes used in scaling the inertial ranges, were then
determined using statistical mechanics arguments [see also
@kraichnan_two-dimensional_1980].

<!-- It stated that a Gaussian initial state with an energy spectra $E(k) = \pi k -->
<!-- U(k)$ would reach an equilibrium distribution which scales as $U(k)~k^{n}$ -->
<!-- where $n \notin [0, 2]$. Therefore, it implies a bidirectional transfer of -->
<!-- energy starting from the initial intermediate scale. -->
<!-- Of particular interest was also the note that while the \kfivethird\ spectrum -->
<!-- could arise from local interactions, the $k^{-3}$ spectrum would be non-local in -->
<!-- nature. Kraichnan identified that these results would have deep -->
<!-- impact in our understanding of mesoscale turbulence. -->

## Quasi-Geostrophic equations

Despite the firm foundations that the theory of @Kraichnan1967 presented, a gap
left to be bridged -- to connect the ideal two-dimensional turbulence to
atmospheric turbulence. @Charney1971 pondered if it was possible to realize the
predictions at all and if so, within what limits the atmosphere can be considered
two-dimensional. It is well-known that most chaotic motions at planetary scales
originates from baroclinic instability [@vallis_atmospheric_2017]. The effects of rotation and
stratification were not considered in @Kraichnan1967. These "shortcomings" were
addressed to some extent by @Charney1971, who derived the $k^{-3}$ spectrum by
analysing the so-called quasi-geostrophic (QG) equation, conserving an
approximate expression for potential vorticity:
$$\Dt{q} = 0$$
$$ q = \nabla^2 \psi + \frac{f_0^2}{\tilde \rho}\left(\frac{\tilde \rho}{N^2}
\p_z \psi \right) + \beta y $${#eq:quasigeo}
where, $\psi$ is the horizontal stream function, $f_0$ is the solid body rotation
speed of the frame of reference, $\tilde \rho$ is the potential density, $N$ is
the Brunt-\text{V\"ais\"al\"a} frequency and $\beta \approx \p_y f$ is the beta
parameter. This equation is valid when certain criteria are met:

 * strong rotation, implying that the Rossby number, $Ro = UL/f_0$ is much
   smaller than unity, where $U$ and $L$ are characteristic horizontal
   velocity and length scales, respectively,
<!-- * Rossby number $Ro < \order{1}$, indicating strong rotation and the flow in -->
<!--   near-geostrophic balance, -->
* characteristic length scales of motion are of the same order as Rossby radius
  of deformation, i.e. $L \sim L_d = HN/f_0$ or $Ro (\frac{L}{L_d})^2 =
  \order{Ro}$. Here, $H$ is a characteristic vertical length scale,
  <!-- Combining this with a scaling analysis of the hydrostatic -->
  <!-- relation for a Boussinesq fluid, which is an equillibrium between pressure -->
  <!-- gradient and Coriolis force, -->
  <!-- \begin{align*} -->
  <!-- | \nabla \phi' | &\sim | {\bf f} \times {\bf u} |\\ -->
  <!-- \phi' &\sim f_o U L \\ -->
  <!-- b' = \p_z{\phi'} &\sim \frac{f_0 U L}{H}\\ -->
  <!-- \frac{\p_zb'}{N^2} &\sim  \frac{f_0 U L}{H^2N^2} -->
  <!-- \sim Ro \left( \frac{f_0L}{HN} \right)^2 -->
  <!-- \sim Ro \left( \frac{L}{L_d} \right)^2 \\ -->
  <!-- \therefore \frac{\p_zb'}{N^2} &\sim \order{Ro} < \order{1} -->
  <!-- \end{align*} -->
  <!-- where $b'$ stands for fluctuations in buoyancy and its evolution equation is -->
  <!-- $\Dt b' = - N^2 w$. -->
  <!-- This scaling would imply that variations in -->
  <!-- stratification are small in comparison with background stratification. -->
* variations in the Coriolis force ($\beta$) are small, implying scales may not
  be as large as planetary length scales,

\noindent and some other scale restrictions [see chapter 5 in
@vallis_atmospheric_2017]. Using @eq:quasigeo and the result that both energy
and QG enstrophy ($q^2 / 2 $) are conserved quantities it was shown that,
the forward energy cascade can be inhibited by the geostrophic constraint. In
this respect the QG equation behave similar to the 2D Navier-Stokes equations.
The $k^{-3}$ scaling law was derived for the QG equations in @Charney1971 and
GCM results from @wellck_effect_1971 were used to confirm the existence of the
$k^{-3}$ spectrum.

## Energy cascade in synoptic and mesoscale flows{#sec:energy}

![Left: A depiction of Kraichnan's conjecture on how at the dual energy cascade
might simultaneously occur in two-dimensional turbulence. Right: A schematic of
observed energy spectra in the atmosphere [@NastromGage1985]
](imgs/cascade.pdf){#fig:cascade}

Nowadays, it is understood that the $k^{-3}$ spectrum at the _synoptic_ scales
(typically, for wavelengths over a thousand kilometres) is an example of a
Kraichnan-Charney type of turbulence, with enstrophy cascading
downscale. The left plot of @fig:cascade shows how @Kraichnan1967 anticipated
the two scaling laws would coexist -- a "stirring force" would inject
energy at intermediate scales, which would then cascade towards
small wavenumbers, while enstrophy would cascade in the opposite direction. In
contrast to this picture, the study by @NastromGage1985,
<!-- which compiled data from over 6000 aircraft flights spanning several years, -->
revealed spectra that were similar to the sketch on the right plot of
@fig:cascade.
Here, the synoptic scale $k^{-3}$-range is found at larger scales than the
mesoscale $k^{-5/3}$-range, an observation that @Frisch found 'paradoxical'.

By what the mechanism the \kfivethird\ mesoscale spectrum is produced, has been
an open question ever since, and competing theories were put forth to address
this issue. @Dewan:1979 analysed the energy spectrum of velocity fluctuations in the
stratosphere up to wavelengths of \order{10} kilometres and suggested that
internal gravity waves, feeding on turbulent layers trapped by large scale
shear flows, could be the driving mechanism behind the spectrum.
He considered the mesoscale spectrum to be analogous to the ocean
spectrum reported by @garrett_space-time_1972. It was also asserted that a
Kolmogorov-type _forward_ energy cascade of waves is present. This
was substantiated using a simple model for a shear flow by @Phillips.

In @Gage:1979, a competing hypothesis was formulated assuming that the mesoscale cascade
process would be similar to Kraichnan's prediction of inverse energy cascade.
To confirm the power law, the two-point temporal structure functions of winds
was derived and applied on data from balloon sounding measurements. Through
Taylor's transformation the author linked the temporal variability to the
spatial structure function equivalent of \kfivethird\ spectrum. In a
contemporary paper,
@Lilly:1983 also made a similar inference of an inverse energy cascade, while
studying decaying stably-stratified turbulence and its tendency to evolve into
enlarged vortices. A scale based decomposition of the Boussinesq equation into
waves and vortices by @riley_direct_1981, was used to study the interactions of
waves and stratification with an initial state of isotropic turbulence with a
$k^{-2}$ spectrum. It was hypothesized that the stratified turbulence would
transfer energy to larger scales, resulting in a $\kfivethird$
spectrum. The inverse energy cascade hypothesis was revisited by @Xia2011
through experiments, wherein a large scale planar vortex was forced from the
small scales electromagnetically to generate a \kfivethird\ spectrum.

@Lindborg1999 contains a detailed review of the above and other hypotheses,
proposed in the light of the @nastrom_kinetic_1984 results, along with a
discussion of their pros and cons. The two-dimensional turbulence
interpretation can be questioned since it would require an small-scale energy
source of \order{1} km, when the mesoscale to microscale transition is observed
[@vinnichenko_kinetic_1970]. However, at this scale three-dimensional motions
are dominant. It is also unlikely that there would be a physical mechanism
acting as a sink near the synoptic to mesoscale transition range as suggested
in @gage_theoretical_1986, since the transition appears to be rather smooth in the
spectrum, as noted by the same authors in the GASP analysis. Nevertheless,
@Lindborg1999 argues that, it is still possible to accommodate both $k^{-3}$
and \kfivethird\ ranges without adding a sink at intermediate scales.  He
demonstrates the possibility of a inertial range determined by both
constant-energy and enstrophy fluxes, by allowing both a large scale and a
small energy source to exists.

An important contribution introduced in @Lindborg1999 was analytical relations
for second-, third- and fourth-order structure functions for two-dimensional
turbulence. Structure functions were used instead of spectral analysis, as it
can be applied on one-dimensional non-uniform data and does not require removal
of the mean flow. These relations were then tested upon MOZAIC
(Measurement of Ozone by Airbus in-service aircraft) dataset to investigate
whether the power law scaling in the inertial range, the direction of the
cascade, and the intermittency can be explained within the framework of
two-dimensional turbulence theory or not. The measurements indicate an
agreement with second-order structure relation,
$$\braket{\delta {\bf u} \cdot \delta {\bf  u}}(r) = C_u \epsilon_K^{2/3}
r^{2/3}$${#eq:structfn2}
where, $\epsilon_K$ is the kinetic energy flux. The $r^{2/3}$ scaling is
equivalent to a $k^{-5/3}$ spectrum. @Lindborg1999  also remarked that the
scaling was found to fit better for larger separations and was conjectured to
be caused by three-dimensional effects becoming influential at smaller scales.
The third order structure function relation,
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
overall third order function is negative and scales as $-r$, implying a forward
energy cascade and a correspondence with Kolmogorov's 4/5-law for
three-dimensional turbulence
[@Frisch;@augier_kolmogorov_2012-1]; and in the range $540 < r < 1400$ km the
same scales as $r^3$ with positive values, implying forward enstrophy flux. The
authors also indicate that the overall tropospheric structure function were
negative for all mesoscales, although it did not converge to follow a
particular power law. These observations are perhaps the strongest evidence for
the forward energy cascade hypothesis for the mesoscales. Next, we turn to
question of what resolution is required to reproduce the mesoscale spectrum and
associated physics.

## Stratified turbulence

The troposphere, the lowest layer of the atmosphere, is relatively thin (10 to 20 km)
compared to Earth's radius 6400 km. Fluid motion is predominantly horizontal.
The troposphere is also constantly influenced by background stratification resulting
from the vertical potential temperature gradient.  Stratified turbulence is a discipline
of fluid mechanics which studies such flows. The term was coined by
@Lilly:1983 for flows affected by a stable, vertical gradient in density or
temperature, resulting in quasi-horizontal motions consisting of large eddies
and gravity waves. Stratification is characterized by the
Brunt-\text{V\"ais\"al\"a} frequency, $N=\sqrt{\frac{-g}{\rho_0}
\pder[\rho(z)]{z}}$ and the Froude number based on horizontal velocity and
length scale, $Fr_h = u / (Nl_h)$.  When a fluid is under geostrophic balance
(equalizing hydrostatic and Coriolis force), one would expect the horizontal
vortices to follow the Taylor-Proudman theorem
[@taylor_motion_1917;@proudman_motion_1916] which is expressed as
$\partial_z \mathbf{u} = 0$.  Yet turbulence in strongly stratified fluids have
been observed to evolve into elongated "pancake"-like horizontal layers over
time which decouple the horizontal motion, resulting in vertical variability.
Such structures are thought to be important elements, distinguishing the
physics of stratified turbulence from two-dimensional turbulence
[@riley_fluid_2000].  Understanding the vertical structure of stratified
turbulence is of paramount importance to analyse the energy transport.

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
However, it was unclear what the characteristic vertical length scale of
stratified turbulence is. Experimental
[@fincham_energy_1996;@billant_experimental_2000] and numerical [@herring_numerical_1989]
investigations of stratified turbulence demonstrated that layered structures
can emerge from purely horizontal base flows or forcing, which implied the
vertical length scale must depend on characteristic properties of the flow.
In other words, strongly stratified flows ($Fr_h \ll 1$) with sufficiently high
Reynolds number would spontaneously undergo a shear or "zig-zag" instability with
alternating elongated  horizontal structures.
This led @Billant2001, to propose a new scaling for stratified turbulence,
wherein, the vertical length scale of the turbulence, that this instability
leads to, was postulated to scale as, $l_v = u / N$. Using this result, along
with two hypotheses: $Fr_h \ll 1$ and advective time scale based on horizontal
length scale $T = l_h / u$, the authors demonstrate that it is possible to
simplify the Boussinesq equations into a set of dimensionless equations
describing stratified turbulence. Furthermore, enforcing
the aspect ratio parameter $\delta = l_v / l_h = Fr_h$ at the limit of strong
stratification $Fr \to 0$, a set of self-similar reduced-order equations were
also derived, which are invariant for a group of transformations of $N, z, u_z$
and $\rho$. The implications of this seminal study was that, unlike the
explanation in @Lilly:1983, by assuming a vertical length scale, $l_v = u / N$ one
can derive the reduced-order system in which waves and vortices evolve on
similar time and length scales. @Billant2001 also suggested that the
buoyancy Reynolds number $Re_b = Re_h Fr_h^2$, where $Re_h$ is the Reynolds
number based on horizontal length scales, must meet the condition $1 \ll Re_b
\ll Re_h$, for the self-similarity to hold.  These results were also reproduced
in decaying [@riley_dynamics_2003] and forced
[@Waite-Bartello:2004;@Lindborg2006] simulations of stratified turbulence. In
@Lindborg2006, it was also shown that the energy cascade is analogous to
Kolmogorov's turbulence picture, and that the kinetic and potential energy
spectra are determined by the rate of dissipation and the wavenumber as:
$$E_K(k_h) = C_K \epsilon_K^{2/3} k_h^{-5/3}$${#eq:EKspectra}
$$E_P(k_h) = C_P \epsilon_K^{-1/3} \epsilon_P k_h^{-5/3}$${#eq:EPspectra}
where, $\epsilon_K$ and $\epsilon_P$ are rates of dissipation of kinetic and
potential energies respectively and the coefficients were found from
simulations to be $C_K \approx C_P \approx 0.5$. Approximate equipartition,
$E_K \sim E_P$ and $\epsilon_K \sim \epsilon_P$, was assumed and total
dissipation was expected to scale as, $\epsilon = \epsilon_K + \epsilon_P \sim
u^3 / l_h$ [@taylor_statistical_1935]. For flow structures smaller than the
Ozmidov length scale, $l_0 = \epsilon^{1/2} / N^{3/2}$, stratified turbulence
transitions to local patches of isotropic turbulence.

@Lindborg2006 argued the stratified turbulence theory can explain the mesoscale
spectra reported in @NastromGage1985 for wavelengths between 2 and 500 km.  The
spectral energy fluxes were positive for all wavenumbers in the simulations
implying a forward energy cascade as @Dewan:1979 initially anticipated.
However, with $E_K(k_h) \sim 3 E_P(k_h)$ there was no perfect equipartition of
energy between kinetic and potential energy
suggesting that the physical mechanism is not linear gravity waves but
nonlinear layered motions resulting from stratified turbulence. In the light
of these new results, one can say the majority of results tend to favour the
forward-cascade hypothesis. Stratified turbulence might be a possible
explanation of mesoscale spectra, but as observed from the GCM simulations of
@AugierLindborg2013, it might not be necessary to simulate a fully resolved
stratified flow to mimic its dynamics. We shall now see how a simpler shallow
water model is used in the present thesis to study geophysical turbulence.

