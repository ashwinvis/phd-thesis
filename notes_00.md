# Atmospheric turbulence: Shallow Water and Toy Model Equations

## 2D turbulence

It stated that a Gaussian initial state with an energy spectra $E(k) = \pi k
U(k)$ would reach an equilibrium distribution which scales as $U(k)~k^{n}$
where $n \notin [0, 2]$. Therefore, it implies a bidirectional transfer of
energy starting from the initial intermediate scale.
Of particular interest was also the note that while the \kfivethird\ spectrum
could arise from local interactions, the $k^{-3}$ spectrum would be non-local in
nature. Kraichnan identified that these results would have deep
impact in our understanding of mesoscale turbulence.

## Quasi-geostrophic turbulence
* Rossby number $Ro < \order{1}$, indicating strong rotation and the flow in
  near-geostrophic balance,
* Combining this with a scaling analysis of the hydrostatic
  relation for a Boussinesq fluid, which is an equillibrium between pressure
  gradient and Coriolis force,
  \begin{align*}
  | \nabla \phi' | &\sim | {\bf f} \times {\bf u} |\\
  \phi' &\sim f_o U L \\
  b' = \p_z{\phi'} &\sim \frac{f_0 U L}{H}\\
  \frac{\p_zb'}{N^2} &\sim  \frac{f_0 U L}{H^2N^2}
  \sim Ro \left( \frac{f_0L}{HN} \right)^2
  \sim Ro \left( \frac{L}{L_d} \right)^2 \\
  \therefore \frac{\p_zb'}{N^2} &\sim \order{Ro} < \order{1}
  \end{align*}
  where $b'$ stands for fluctuations in buoyancy and its evolution equation is
  $\Dt b' = - N^2 w$.
  This scaling would imply that variations in
  stratification are small in comparison with background stratification.

## Atmospheric energetics
@NastromGage1985 which compiled data from over 6000 aircraft flights spanning several years,

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
latitudinal (or zonal) bands to account for inhomogeneities.

Next, we turn to question of what resolution is required to reproduce the
mesoscale spectrum and associated physics.

## Stratified turbulence

The troposphere, the lowest layer of the atmosphere, is relatively thin (10 to 20 km)
compared to Earth's radius 6400 km. Fluid motion is predominantly horizontal.
The troposphere is also constantly influenced by background stratification resulting
from the vertical potential temperature gradient.  Stratified turbulence is a discipline
of fluid mechanics which studies such flows.

Stratification is characterized by the
Brunt-\text{V\"ais\"al\"a} frequency, $N=\sqrt{\frac{-g}{\rho_0}
\pder[\rho(z)]{z}}$ and the Froude number based on horizontal velocity and
length scale, $Fr_h = u / (Nl_h)$.

vertical length scale must depend on characteristic properties of the flow.


Zig-zag instability led @Billant2001 to propose a new scaling for stratified turbulence,
wherein, the vertical length scale of the turbulence,
leads to, was postulated to scale as, $l_v = u / N$. Using this result, along
with two hypotheses: $Fr_h \ll 1$ and advective time scale based on horizontal
length scale $T = l_h / u$, the authors demonstrate that it is possible to
simplify the Boussinesq equations into a set of dimensionless equations
describing stratified turbulence. Furthermore, enforcing
the aspect ratio parameter $\delta = l_v / l_h = Fr_h$ at the limit of strong
stratification $Fr \to 0$, a set of self-similar
