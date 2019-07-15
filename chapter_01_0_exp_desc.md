\chapter{Experimental investigation of mixing in stratified turbulence}

![Schematic of the global MOC conveyor
belt](./imgs/thermohaline-nasa.jpg){#fig:thermohaline-global width=80%}

The meridional overturning circulation (MOC) or the thermohaline circulation
refers to the ocean currents resulting from the melting of ice near the polar
region and upwelling elsewhere as shown in @fig:thermohaline-global. This
circulation is responsible for the bulk of heat transport from the equator to
the poles across the globe. Without this global conveyor belt, shown in
@fig:thermohaline-global, the temperatures at latitudes away from the equator
would be considerably lesser [@bryden_slowing_2005]. It is also responsible for
replenishing the surface water with nutrients and critical to the sustenance of
marine life.

![Conceptual sketch of the Atlantic meridional overturning
circulation (AMOC) in depth and latitude coordinates. The dashed lines represent
streamlines of overturning masses, the Antarctic bottom water (AABW) and the
North Atlantic deep water (NADW), the black solid lines are the isopycnals and
the red arrow represents the downward diapycnal heat flux due to mixing. (©
Copyright 2012, AMS, @nikurashin_theory_2012).
](./imgs/moc-nik-vallis.jpg){#fig:moc}

The MOC is thought to be driven by a combination of wind forcing, changes in
buoyancy and diapycnal mixing, as shown in @fig:moc for the Atlantic MOC. The
exact contribution of these three forces remain an open question [see chapter
21 in @vallis_atmospheric_2017]. It should be noted that the circulation
happens within a ocean with varying degrees of stable stratification in both
temperature and salinity. For illustrating this the time averaged temperature
and salinity in the Atlantic ocean [calculated from @carton_soda3_2018] are
plotted in @fig:atlantic-salt-temp. It is understood that through mixing,
kinetic energy is converted into available potential energy which allows the
streamlines to overturn and thus allowing bottom water from great depths to
resurface.


<div id="fig:atlantic-salt-temp">

![Time averaged salinity levels in practical salinity units
(PSU)](./imgs/ocean_mixing_salt.pdf){#fig:atlantic-salt width=100%}

![Time averaged temperature in degrees
Celsius](./imgs/ocean_mixing_temp.pdf){#fig:atlantic-temp width=100%}

Stratification in the Atlantic Ocean along a meridional
cross-section at 26.2$^{\circ}$ W, plotted from reanalysis data spanning years
2000-2010.
</div>

Stratified turbulence and the resulting mixing cannot be fully resolved in
ocean models with the current state of the art. Therefore it is typically
parametrized in eddy diffusivity models using a non-dimensional variable called
mixing coefficient, $\Gamma = \epsK / \epsA$, a ratio of kinetic (KE) and
available potential energy (APE) dissipation . A conservative estimate of
$\Gamma = 0.2$ is widely used in ocean models. As described in the previous
chapter, the theory of stratified turbulence introduced in @Billant2001, opened
an avenue for various scaling laws. The strongly stratified turbulence regime
is characterized by two non-dimensional numbers [@Brethouwer2007],

$$F_h = \frac{\epsK}{NU^2} \ll 1,\text{ and } \R = \frac{\epsK}{\nu N^2} > 10.$$

\noindent a Froude number based on horizontal velocity and buoyancy Reynolds
number respectively.  Due to the fact that buoyancy Reynolds number relates to
conventional horizontal Reynolds number ($Re_h$) as $\R = Re_hFr_h^2$, reaching
this regime is an expensive proposition, both numerically and experimentally.
The fluid has to be under a strong background stratification and high Reynolds
number forcing simultaneously. This state is difficult to maintain as mixing
tends to reduce stratification over time. Despite these difficulties numerical
simulations have pushed the limits to be as close to the predicted values of
$Fr_h$ and $\R$ as possible
[@Brethouwer2007;@BrethouwerLindborg2009;@Maffioli2016;@maffioli_mixing_2016]
of which some are depicted on @fig:stratified-regime. In the strongly
stratified regime, mixing coefficient values have been found to be in the
range, $\Gamma \in [0.26, 0.51]$
[@BrethouwerLindborg2009;@maffioli_mixing_2016], thus significantly larger than
the canonical value of $\Gamma = 0.2$. In @maffioli_mixing_2016, high
resolution DNS of Boussinesq equation suggested that the mixing coefficient
peaks at an intermediate $Fr \approx 0.29$ with $\Gamma \approx 0.51$ and then
for stronger stratifications a declining trend up to $Fr \approx 0.02$ with
$\Gamma \approx 0.33$ was recorded. Also note that, as shown in
@fig:stratified-regime, oceans measurements are considerably more stratified
[@gargett_composite_1981].

![In-situ measurements, experiments and numerical simulations classified by
their regime according to stratified turbulence
theory](./_paper_06_milestone/tmp/fig_R_vs_Fh_other_studies_with_milestone17.png){#fig:stratified-regime}

The question of what value the mixing coefficient would tend to at higher
levels of stratification, is at the heart of the project titled Mixing and
Length Scales in Stratified Turbulence (MILESTONE) [@ISSF2016].  This chapter
presents the project as follows: the first section briefly describes the
experimental setup; the second section introduces the open-source software
stack which was developed to perform the experiment and post-process the data;
and lastly we highlight some of the results.


# Experimental Setup

![Schematic of the Coriolis platform and mounted instruments (top
view)](./paper_05_milestone_issf/Figures/scheme_exp_grid_MILESTONE_Euhit.pdf){
#fig:scheme-coriolis width=60%}

The Coriolis platform is an experimental facility at LEGI, Universit\'e
Grenoble Alpes, which is 13 metres in diameter and is mounted on motors
allowing the entire platform to rotate. Both rotating and non-rotating
experiments were conducted in this project. The platform was filled with a
linear stratification of salinity up to a height of 81 cm using a double-bucket
method. A rectangular enclosure as shown in @fig:scheme-coriolis was $9 \times
6 \text{ m}^2$ area contains most of the equipment, including the oscillating carriage
which forces the fluid.

## Carriage

Anticipating a forward energy cascade [@riley_dynamics_2003;@Lindborg2006], we
chose to force at large scales. In the literature, various approaches can be
found to inject KE into the system. For instance in
@AugierBillantNegrettiChomaz2013 a series of flapping plates stationed along
the boundary ere used to generate dipoles. A drawback of this method is that it
also adds smaller scales in comparison with the size of the plate. In
@PraudFinchamSommeria2005, a rake consisting of series of flat plates were
towed through the fluid which. Here we replaced the rake with a carriage
attached with a grid of six vertical cylinders, with diameters of the 0.25
metres, attached to a motor-driven carriage was towed through the fluid. The
wake of the grid would have the characteristic length scale of the cylinder
diameter. In contrast to @PraudFinchamSommeria2005, which involved decaying
turbulence studies, here we make measurements while the carriage oscillates
back and forth along the rectangular enclosure as shown in @fig:movement.
Several experiments with different levels of stratification ($N$) and
carriage velocity ($U_c$) were conducted. In order to characterize the
experiments we define a Froude number and a buoyancy Reynolds number,

$$F_{hc} = \frac{U_c}{NM}, \R_c = \frac{U_c^3}{\nu N^2M}$$

\noindent respectively where $N$, the Brunt-V\text{\"a}isala frequency is evaluated
*a priori* while the fluid is quiescent and $M$ is the characteristic size of the
vortices.

![Chronogram of the position of the
carriage](./paper_05_milestone_issf/Figures/fig_movement_carriage.pdf){#fig:movement
width=60%}


## Measuring instruments

### Density probes

Five conductometric probes calibrated for ambient temperature conditions and
expected salinity range were installed at different locations, indicated with
blue dots in @fig:scheme-coriolis. The probes $P_p^1$ and $P_p^2$ are mounted
on vertical profilers and these dive into the fluid at even time intervals at a
moderate speed, providing us with accurate one-dimensional estimate of the
stratification. Probe $P_c$ is attached on the carriage, at a constant height
of 0.395 meters. Since $P_c$ makes measurements along an asymmetric direction
during oscillation, its data is decomposed and interpreted differently: when it
is ahead of the carriage it measures a decaying turbulence and when it is in
the wake of the carriage it measures forced turbulence. $P_f^1$ and $P_f^2$ are
stationary probes and they are placed at the top and bottom of the fluid to
measure temporal evolution of the mixed layer.

### Particle Image Velocimetry (PIV)

Two sets of PIV techniques are applied in this setup. Firstly, a
two-dimensional, two-component (2D-2C) scanning PIV system is used for
measuring velocities along quasi-horizontal planes with a maximum tilt of
1.5$^\circ$ about the true horizontal plane. This system relies on a single
laser sheet deflected by an oscillating mirror controlled by a servo motor. For
the same experimental parameters two sets of measurements are done, one with
five horizontal planes and small scan amplitudes to obtain fine vertical
resolution, and another with typically eight planes and wider scan angles which
tend to be vertically decorrelated. The images are captured by three cameras,
one placed at a high altitude capture the largest field ($2.2 \times 2.5 \text{ m}^2$),
a second one placed at an intermediate altitude capturing a smaller field ($1.3
\times 1.0 \text{ m}^2$) and a third one placed under the platform capturing a small
field ($1.18 \times 0.53 \text{ m}^2$).  The fields of vision are demarcated in pink in
@fig:scheme-coriolis.  The cameras are placed progressively closer to the fluid
to get more illumination from the particles seeded and potentially increased
resolution.

Secondly, a vertical plane is measured using a two-dimensional, three-component
(2D-3C) stereoscopic PIV system. This system captures a field of are $0.45
\times 0.45 \text{ m}^2$.

For both the PIV systems, up to 1300 images per oscillation of the carriage are
captured.




