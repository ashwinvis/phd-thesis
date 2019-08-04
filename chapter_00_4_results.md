# Research highlights

@Fig:flux_decomp is an example which shows a normal mode decomposition of the
spectral
energy fluxes. The figure is plotted from two toy model simulations with
different forcing schemes. In both cases, all energy which is injected at
$k_f$ is transferred to smaller scales, and the normalised total energy flux
(black curve) is equal to unity in a broad range of wavenumbers. The plot to
the left is from a run were we force in wave modes alone. As a result, the flux
is dominated by the contribution from vortical-wave-wave interactions, $\Pi_
{VWW}$, with a minor contribution from wave-wave-wave interactions,
$\Pi_{WWW}$, at large wave numbers. The plot to the right is from a run in
which we only force in vortical modes. As a result, the flux is dominated by
the contribution from vortical-vortical-wave interactions $\Pi_{VVW}$, at small
wave numbers, and by vortical-wave-wave interactions, $\Pi_{VWW}$ at large wave
numbers. In both cases, vortical-wave-wave interactions make an important
contribution to the downscale energy cascade.

![Comparison of spectral energy budget from a toy model simulation with two
different forcing
schemes](./paper_03_toy_model/fig5-eps-converted-to.pdf){#fig:flux_decomp}

The analysis also proved to be useful to compare with the energetics of a
GCM. The spectral energy budget of the GCM is shown in @fig:sebgcm as a
function $l$, the degree of spherical harmonics function which is similar
to wavenumbers $k$ in Cartesian coordinates. The GCM is forced at planetary
scales $l < 3$ in APE, indicated by the large bump in $\Pi_A$.  Around $l =
[8, 30]$, baroclinic instability is responsible for conversion from APE to KE.
This is reflected also in $C_{cum}$ curve. At $l > 50$ the total fluxes are
reasonably flat, implying a net forward energy cascade. There is also an
inverse energy cascade shown by $\Pi_{2D}$, which is essentially $\Pi_{VVV}$
following the terminology we used previously. $\Pi_{2D}$ becomes particularly
dominant at large scales. Similar dynamics are displayed by the toy model as
shown in @fig:sebtoy. Of course, the toy model is more idealized, and a
difference we see here is that the fluxes of KE and APE are equipartitioned at
smaller scales.

<div id="fig:sebgcmtoy">
![](./paper_03_toy_model/fig1.eps){width=50% #fig:sebgcm}
![](./paper_03_toy_model/fig10.eps){width=43% #fig:sebtoy}

A comparison of the spectral energy budgets from a GCM simulation and a toy
model simulation [@LindborgMohanan2017]. The total spectral energy flux $\Pi$
has been decomposed into kinetic ($\Pi_K$) and available potential energy
($\Pi_A$) energy fluxes. The conversion from available potential energy to
kinetic energy is represented by $C_{cum}$. The kinetic energy flux is further
decomposed as $\Pi_{2D}$, the flux due to geostrophic modes and the difference
$\Pi_K - \Pi_{2D}$. The plot on the left is from @AugierLindborg2013 "A
new formulation of the spectral energy budget of the atmosphere, with
application to two high-resolution general circulation models" _J. Atmos.
Sci._, **70**, 2293-2308. \textcopyright American Meteorological Society. Used
with permission.
</div>

![Comparison of the divergence fields ($\mathbf{\nabla.u}$) from a shallow
water simulation (left) and a similar toy-model simulation (right). $L_f$ is
the forcing length scale. Source:
@LindborgMohanan2017.](./paper_03_toy_model/fig9.pdf){#fig:shallow-toy
width=100%}

The toy model is visibly different from the SWE which exhibits shock dominated
wave turbulence as shown in @fig:shallow-toy. Both simulations are forced using
similar parameters. The plot on the left shows
sharp thin lines of negative divergence which are characteristic of shock
waves. There is always a sudden dip in the velocity if we follow along the
direction of shock propagation, which is reflected as negative values of the
divergence. On the right, the divergence field of the toy model simulation
consists of ripples of alternative positive and negative values, indicating
that there are no shocks.

<div id="fig:anticyclones">
![The Great Red Spot in the Jupiter, an example of an anticyclone (Courtesy:
[NASA/JPL/Space Science
Institute](https://www.nasa.gov/feature/goddard/jupiter-s-great-red-spot-a-swirling-mystery)
).](./imgs/red-spot-nasa.jpg){#fig:red-spot width=65%}\hfill
![Numerous cyclones and anticyclones with diameters of \order{1000} km
photgraphed in the south pole of Jupiter (Courtesy:
[NASA/JPL-Caltech/SwRI/MSSS/Betsy Asher Hall/Gervasio
Robles](https://www.nasa.gov/press-release/a-whole-new-jupiter-first-science-results-from-nasa-s-juno-mission).)
](./imgs/jupiter-pole-nasa.jpg){#fig:Jupiter-pole width=30%}

![Coherent anticyclonic vortices from a simulation using the toy model. On
left: linearised potential vorticity ($q$); on right: one of the
ageostrophic mode ($a^+$) model representing the wave field
[@LindborgMohanan2017].](./imgs/anticyclone-toy-model.jpg){#fig:anticyclone-toy-model
width=95%}

Anticyclones and coherent vortices in nature and from a simulation in
@LindborgMohanan2017
</div>

Another interesting feature of the toy model is revealed in
@fig:anticyclone-toy-model, a visualization of run 3 in @LindborgMohanan2017.
This figure shows that coherent vortices, predominantly anticyclonic emerge
during the course of the simulation. At time $t
/ \tau \approx 600$ vortical energy start to dominate over wave
energy and immediately after this, such anticyclones become visible.
Although in Earth's atmosphere there is a dominance of cyclones, a
noteworthy example of an anticyclone is the Great Red Spot in the planet
Jupiter shown in @fig:red-spot. Cyclonic-anticyclonic asymmetry has
been also studied in other shallow water simulations
[@showman_numerical_2007;@Polvani1994] in which, anticyclones were observed to
dominate over cyclones.


![Spectral energy flux and third-order structure functions from a SWE
simulation run W7 in
@AugierMohananLindborg2017](./paper_04_shallow_water/Pyfig/fig3.eps){#fig:flux-struct}

![Mean shock separation distance $(d)$ in a series of shallow water
simulations plotted against the forcing Froude number $(F_f)$. The Froude
number is inversely proportional to the wave phase-speed, $c$. The theoretical
prediction $d \propto F_f^{1/2}$ is displayed as a dashed line.  Source:
@augier_shallow_2019.
](./paper_04_shallow_water/Pyfig/fig6.eps){#fig:shock-sep width=70%}

Now we turn our attention to shallow water wave turbulence. Some interesting
scaling relations were developed in @AugierMohananLindborg2017 providing
insights into shock dominated turbulence. A Kolmogorov law for isotropic,
irrotational shallow water wave turbulence was derived which gives the
third-order structure functions,
\begin{equation}
\meane{ |\delta \uu|^2 \delta J_L }
+ c^2\meane{ (\delta h)^2 \delta u_L } = -4 \epsilon r, \label{eq:Kolmo}
\end{equation}
where $J_L \equiv \JJ\cdot\rr / |\rr|$ and $u_L \equiv \uu\cdot\rr / |\rr|$ are
longitudinal increments. This law was also verified accurately with numerical
simulation as shown in @fig:flux-struct. Using @eq:Kolmo and the central
assumptions that the dynamics is dominated by shocks, a simple model was
developed and scaling relations for higher order structure functions and
their ratios, skewness, flatness etc. were derived. These relations depend on
the mean separation distance between shocks. This was
numerically found to scale as, $d \propto F_f ^ {1/2}$, as shown in
@fig:shock-sep.


