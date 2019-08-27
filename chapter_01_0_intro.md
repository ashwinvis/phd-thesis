\chapter{The MILESTONE experiment}\label{ch:exp}

This chapter describes the experiment, _Mixing and Length Scales in
Stratified Turbulence_ [MILESTONE, @campagne2016] which aimed at testing the
theory of stratified turbulence [@Billant2001;@Lindborg2006]. The
development of this theory is briefly reviewed in @sec:strat. In particular this
experiment intended to:

1. verify that layered structures emerge with a vertical length scale of $u/N$,

1. verify that there is a forward energy cascade with spectrum scaling as $E(k) \sim
   \epsilon^{2/3} k^{-5/3}$, or alternatively the second order structure
   function scaling as $\braket{\delta \mathbf{u}. \delta \mathbf{u}} \sim
   \epsilon^{2/3} r^{2/3}$, and

1. measure the mixing efficiency in the strongly stratified regime.

Stratified turbulence theory can potentially lead to improved ocean models
which has profound implications in our ability to forecast weather and climate.
It is well known that
<!-- the oceans have a greater thermal capacity than the atmosphere, and that  -->
a global system of ocean currents are responsible for redistribution of heat
from the tropics to higher latitudes, replenishing nutrients to the surface
which are critical for sustenance of marine life, and melting of ice in high
latitudes.

![Schematic of the system of surface (red / light gray) and deep (blue / dark
gray) ocean currents ](./imgs/thermohaline-nasa.jpg){#fig:thermohaline
width=80%}

This phenomenon, interchangeably known as _thermohaline circulation_ or the
_meridional overturning circulation_ (MOC) shown in @fig:thermohaline, is driven by a
combination of wind forcing, fluxes of temperature and salinity at several
isolated regions near the surface and turbulent mixing in the interior of the
ocean [see chapter 21 in @vallis_atmospheric_2017].
Through mixing, the kinetic energy of the ocean currents get converted
into potential energy, resulting in a net upward flux of dense water. In ocean
models this flux of buoyancy is often represented using eddy diffusivity models
parametrized based on mixing:
$$
- \nabla \cdot (\uu b) \simeq \kappa_\tau \nabla^2 b
$$
In the literature, there are different but closely related quantities which
characterize mixing [@Gregg]:

- mixing efficiency, a ratio of dissipation of potential energy and total
  energy $\eta = \epsP / (\epsK + \epsP)$,
- mixing coefficient, $\Gamma = \epsP / \epsK$,
- flux Richardson number, a ratio of buoyancy flux to turbulence production,
  $Ri_f = B / (\epsK + B)$, where $B = -\braket{bu_z}$

Conventionally ocean models rely on a nominal value of $\Gamma = 0.2$ due to
@Osborn, to set the eddy diffusivity parameter $\kappa_\tau = \epsP / N^2 = \Gamma \epsK
/ N^2$ [@OsbornCox;@Lindborg-vertical-2008]. However numerical studies
[@BrethouwerLindborg2009;@Salehipour-diapycnal-2015;@maffioli_mixing_2016] have
shown that mixing efficiency is not a constant and depends on the strength of
stratification. In the limit of strong stratification it approaches a constant
value, and approaches zero in the limit of weakly stratified turbulence, scaling with
horizontal Froude number as $\Gamma \propto F_h ^{-2}$ [@maffioli_mixing_2016].
At intermediate levels of stratification, it is found to vary in the
interval $\Gamma \in [0.26, 0.51]$ and peaking at $F_h \approx 0.33$.

The strongly stratified turbulence regime is characterized by two
non-dimensional numbers [@Brethouwer2007],
$$
F_h = \frac{\epsK}{NU^2} \ll 1,\text{ and } \R = \frac{\epsK}{\nu N^2} > 10.
$$
a Froude number based on horizontal velocity and buoyancy Reynolds number
respectively.  The regime of strongly stratified turbulence, in which $F_h$ is
small and $\mathcal{R}$ is large, is highly relevant for applications in the
ocean [@gargett_composite_1981;@RileyDeBruynKops2003;@Lindborg2006].  However, due
to the fact that the buoyancy Reynolds number relates to the conventional
Reynolds number ($Re_h$) as $\R = Re_hF_h^2$, reaching this regime is a
challenging task, both numerically and experimentally.
In trying to reach the strongly stratified regime experimentally by increasing
the degree of stratification, the buoyancy Reynolds number often becomes so low
that turbulence is totally suppressed.
The fluid has to be under a strong background stratification and high Reynolds
number forcing simultaneously and this state is difficult to maintain as mixing
tends to reduce stratification over time.
In simulations, a
high resolution DNS is required to reach the stratified turbulence regime.
Despite these difficulties numerical simulations have pushed the limits to be
as close to the predicted values of $F_h$ and $\R$ as possible
[@Brethouwer2007;@BrethouwerLindborg2009;@Maffioli2016;@maffioli_mixing_2016]
of which some are depicted on @fig:stratified-regime along with estimates of
the values attained by the MILESTONE experiment.

![In-situ measurements, experiments and numerical simulations classified by
their regime according to stratified turbulence
theory](./paper_06_milestone/1st/tmp/fig_R_vs_Fh_other_studies_with_milestone17.pdf){#fig:stratified-regime}

Thus by testing the validity of the stratified turbulence theory, one can
have a good picture of the vertical length scales, the direction of energy
cascade, and of what parametrizations of mixing are appropriate,
which can greatly benefit modelling of ocean turbulence.  In the following
sections, the experimental setup and the open-source software stack which was
developed to perform the experiment and post-process the data are briefly
described, whereafter we
highlight some of the results.
