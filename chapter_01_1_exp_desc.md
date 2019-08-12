# Experimental Setup

<div id="fig:scheme">
![Schematic of the Coriolis platform and mounted instruments (top
view)](./paper_05_milestone_issf/Figures/scheme_exp_grid_MILESTONE_Euhit.pdf){
#fig:scheme-coriolis width=52%}
![Top view of the setup](./imgs/MILESTONE/GOPR1465.JPG){#fig:exp-top width=45%}

![Chronogram of the position of the
carriage](./paper_05_milestone_issf/Figures/fig_movement_carriage.pdf){#fig:movement width=50%}

Experimental setup
</div>
The Coriolis platform is an experimental facility at LEGI, Universit\text{\'e}
Grenoble Alpes, which is 13 metres in diameter and is mounted on motors
allowing the entire platform to rotate. Both rotating and non-rotating
experiments were conducted in this project. The platform was filled with a
linear stratification of salinity up to a height of 81 cm using a double-bucket
method. A nine metre long and six metre wide rectangular enclosure, as shown in
@fig:scheme-coriolis, contained most of the equipment, including the
oscillating carriage which forces the fluid.

## Carriage


Anticipating a forward energy cascade [@riley_dynamics_2003;@Lindborg2006], we
chose to force at large scales. In the literature, various approaches can be
found to inject KE into the system. For instance in
@AugierBillantNegrettiChomaz2013 a series of flapping plates stationed along
the boundary are used to generate dipoles. A drawback of this method is that it
also produces smaller scales of motion in comparison with the size of the plate. In
@PraudFinchamSommeria2005, a rake consisting of series of flat plates were
towed through the fluid which also has the same drawback. Here we replaced the
rake with a carriage attached with a comb of six vertical cylinders, with
diameter 0.25 metre, attached to a motor-driven carriage towed through the
fluid. The oscillating comb injects kinetic energy in the form of eddies as
shown in @fig:eddies.  The wake of the comb has a characteristic
length scale of the cylinder diameter.
In contrast to @PraudFinchamSommeria2005, who carried out decaying
turbulence studies, here we make measurements while the carriage oscillates
back and forth along the rectangular enclosure. A chronogram of the movement is
shown in @fig:movement.
Several experiments with different levels of stratification ($N$) and
carriage velocity ($U_c$) were conducted. In order to characterize the
experiments we define a Froude number and a buoyancy Reynolds number,
$$
F_{hc} = \frac{U_c}{NM},\quad \R_c = \frac{U_c^3}{\nu N^2M}
$$
\noindent respectively where $N$, the Brunt-V\text{\"a}isala frequency is evaluated
*a priori* while the fluid is quiescent and $M$ is the characteristic size of the
vortices.

## Measuring instruments

### Density probes

Five conductometric probes calibrated for ambient temperature conditions and
the expected salinity range were installed at different locations, indicated with
blue dots in @fig:scheme-coriolis. The probes $P_p^1$ and $P_p^2$ are mounted
on vertical profilers and these dive into the fluid at regular time intervals at a
moderate speed, providing us with accurate one-dimensional estimates of the
stratification. Probe $P_c$ is attached on the carriage, at a constant height
of 0.395 meters. Since $P_c$ makes measurements along the direction of the
carriage oscillation, the data output from this probe is decomposed and
interpreted differently. When it
is ahead of the carriage it measures decaying turbulence and when it is in
the wake of the carriage it measures forced turbulence. $P_f^1$ and $P_f^2$ are
stationary probes which are placed at the top and bottom of the fluid to
measure temporal evolution of the mixed layer.

### Particle Image Velocimetry (PIV)

<div id="fig:eddies">
![Side view of the setup while the carriage is in
motion](./imgs/MILESTONE/GOPR1456.JPG){#fig:exp-side width=47%}
![Long exposure photograph of the eddies in the wake of the
carriage](./imgs/MILESTONE/DSC_0203.JPG){#fig:eddies width=53%}

Visuals from a test experiment with the laser sheets illuminating the flow.
</div>

Two sets of PIV techniques are applied in this setup. Firstly, a
two-dimensional, two-component (2D-2C) scanning PIV system is used for
measuring velocities along quasi-horizontal planes with a maximum tilt of
1.5$^\circ$ about the true horizontal plane. This system relies on a single
laser sheet deflected by an oscillating mirror controlled by a servo motor. For
the same experimental parameters two sets of measurements are carried out, one with
five horizontal planes and small scan amplitudes to obtain fine vertical
resolution, and another with typically eight planes and wider scan angles which
tend to be vertically decorrelated. The images are captured by three cameras,
one placed at a high altitude capturing a large field ($2.2 \times 2.5 \text{ m}^2$),
a second one placed at an intermediate altitude capturing a smaller field ($1.3
\times 1.0 \text{ m}^2$) and a third one placed under the platform capturing an even smaller
field ($1.18 \times 0.53 \text{ m}^2$). The fields of vision are demarcated in pink in
@fig:scheme-coriolis.  The cameras are placed progressively closer to the fluid
to get more illumination from the particles seeded and potentially increased
resolution.
Secondly, the velocity field in the vertical plane is measured using a
two-dimensional, three-component
(2D-3C) stereoscopic PIV system. This system captures a field of area $0.45
\times 0.45 \text{ m}^2$.
For both the PIV systems, up to 1300 images per oscillation of the carriage are
captured.


