# Part 1: Two dimensional models of geophysical turbulence

## Background

:::::::::::::::: {.columns}
::: {.column width="50%"}

**Atmospheric energy spectrum**^[@NastromGage1985 © AMS]

![](../imgs/NastromGage.png){width=90% height=70%}
<!-- ![Power spectrum of velocities and potential temperature](../imgs/NastromGage.png){width=80% height=60%} -->


:::
::: {.column width="50%"}

. . .


Two inertial ranges, separated by scales:

\ 

- planetary / synoptic scales $E(k) \sim k^{-3}$
  ![](../imgs/synoptic.jpg){width=70% height=28%}


. . .

- mesoscales $E(k) \sim k^{-5/3}$
  ![](../imgs/mesoscale.jpg){width=70% height=28%}


:::
:::::::::::::::::::::::::::::

. . .

\centering{\alert{How do we theorize the mechanism behind these two inertial ranges?}}

### Two-dimensional turbulence

Kraichnan's theory of 2D turbulence[^kraichnan]

- **Vorticity** and **enstrophy** conservation: a strong constraint on cascade

- Dual cascade:
$$E(k) \sim \epsilon^{2/3}k^{-5/3},\quad E(k) \sim \eta^{2/3}k^{-3}$$

. . .

- Directions of cascades:

  - $k^{-5/3}$ range: constant energy flux[^kolmo] $\epsilon$, **inverse** cascade

  - $k^{-3}$ range: constant enstrophy flux $\eta$, **forward** cascade

. . .

- Spatial scales of inertial ranges: "a paradox"[^frisch]
  !["A paradox"[^frisch]](../imgs/cascade_horiz.png){width=70% height=40%}

[^kraichnan]: @Kraichnan1967
[^kolmo]: Similar to @Kolmogorov1941's theory
[^frisch]: @Frisch

### Quasi geostrophic equation

- Quasi-geostrophic equation conserves an approximate *potential vorticity*:
  $$\Dt{q} = 0,$$
  $$ q = \nabla^2 \psi + \frac{\alert<2>{f_0}^2}{\tilde \rho}
  \left(\frac{\tilde \rho}{\alert<3>{N}^2} \p_z \psi \right) + \alert<2>{\beta} y, $$

. . .

- Incorporates [rotation]{alert="<2>"} and [stratification]{alert="<3>"} in a 2D model

- Bridging **ideal 2D turbulence** to **atmospheric turbulence**

- Reproduces $k^{-3}$ spectrum^[@Charney1971]

- <4-> Valid for **strong rotation**, lengths scales **smaller than
  planetary** scales

- <5-> No ageostrophic motion, for example: **inertial gravity waves**

<6-> \centering{{\alert{What about the $k^{-5/3}$ mesoscale spectrum?}}}


### Possible explanations of mesoscale spectrum

#### Hypotheses for cascade directions {.cbox}

- @Gage:1979 & @Lilly:1983: **inverse energy cascade** as in @Kraichnan1967

- @Dewan:1979: **forward energy cascade** as in @Kolmogorov1941

#### {.endblock}

. . .

#### Vertical resolutions {.cbox}

* @Waite-Bartello:2004 and @Lindborg2006 : **stratified turbulence**. $l_v \sim u/N \approx 1 \text{km}$. 
* @Buhler-Callies-Ferrari:2014 : **inertia gravity waves**. Frequency
  $\omega \approx f$. i.e. $l_v \approx$ 100 metres.

#### {.endblock}

. . .

\ 

::::::::::::::::::::::::::::: {.columns}

::: {.column width=40%}

DNS of stratified turbulence supports:
^[@Lindborg2006 ]


* $k^{-5/3}$ spectrum

- **forward cascade**

- **fine vertical resolution** requirement

:::
::: {.column}

. . .

General circulation models^[@Augier-Lindborg:2013] shows:

* $k^{-5/3}$ spectrum

- **forward cascade** in mesoscales

- with **coarse resolution**: 24 pressure levels along vertical

:::
:::::::::::::::::::::::::::::::::::::::::

. . .

\centering{{\alert{Minimum number of vertical levels? Is it possible with a single level model?}}}

## Shallow water equations

### Properties of shallow water equations

#### Governing equations

::: notes

- Inviscid equations conserves in a periodic domain (no boundary fluxes)

:::

::::::::::{.columns}
:::{.column width=50%}

  \begin{align*}
  \partial_t \alert<2>{\mathbf{u}} &= - (\alert<2>{\mathbf{u}}.\nabla) \alert<2>{\mathbf{u}}
      - \alert<3>c^2 \nabla \alert<5>h - \alert<4>f\mathbf{e_z} \times \alert<2>{\mathbf{u}}, \\
  \partial_t \alert<5>h &= - \nabla \cdot (\alert<5>h \alert<2>{\mathbf{u}}).
  \end{align*}

- where,

  + <2-> $\alert<2>{\mathbf{u}}=$ horizontal velocity vector,
  + <3-> $\alert<3>{c} =$ wave speed,
  + <4-> $\alert<4>f$ = Coriolis parameter,
  + <5-> $\alert<5>{h} = H + \eta$, height of fluid^[@vallis_atmospheric_2017].

:::
:::{.column width=50%}

<5-> ![](../imgs/swe_eta_h.png){width=100% height=40%}
:::
:::::::::::::::::::

\onslide<6->


#### with **good properties** {.gbox}

  + Conserves **energy** $E = E_K + E_P$ 
  + Conserves **potential vorticity**, $Q = (\zeta + f)/h$
  + Equipartition of $E_K$ and $E_P$ over a wave period
  
#### {.endblock}

\ 
\onslide<7->

#### and some **downsides** {.rbox}

  + Waves $\to$ shocks
  + Cubic $E_K = h\mathbf{u.u} / 2$

#### {.endblock}

### Results: Energy cascade 1^[ @augier_shallow_2019 ]


#### SW analogue of @Kolmogorov1941's $\frac{4}{5}$ law for $3^{rd}$-order structure function {.cbox}
  \begin{equation*}
  \meane{ |\delta \uu|^2 \delta J_L }
  + c^2\meane{ (\delta h)^2 \delta u_L } = -4 \epsilon r,
  \end{equation*}
  where $J_L \equiv h \uu \cdot\rr / |\rr|$ and $u_L \equiv \uu\cdot\rr / |\rr|$

#### {.endblock}

. . .

![Spectral energy fluxes $\Pi(k)$ and $3^{rd}$-order structure
functions $\approx-4\epsilon r$](../paper_04_shallow_water/Pyfig/fig3-eps-converted-to.pdf){width=60%
height=40%}


- Positive flux $\Rightarrow$ **forward energy** cascade

### Results: Shock waves^[ @augier_shallow_2019 ]

![Visualization of shocks using divergence $\nabla.\uu$ and velocity component
$u_y$](../paper_04_shallow_water/Pyfig/fig5-eps-converted-to.pdf){width=60%
height=80%}

### Results: Spectra and higher-order statistics^[ @augier_shallow_2019 ]

#### Scaling laws for shock dominated turbulence {.cbox}

- <+-> Shock amplitudes, $| \Delta u | \sim | c \Delta h | \sim (\epsilon d)^{1/3}$

- <+-> $p^{th}$-order structure functions
  $$\meane{|\delta u |^p}  \sim \meane{(c|\delta h |)^p} \sim  (\epsilon
  d)^{p/3} \,  \frac{r}{d}$$

- <+-> Energy spectra:\, $E_K(k)  \sim  E_A(k) \sim \epsilon ^{2/3} d^{-1/3} k^{-2}$

#### {.endblock}

. . .

<div id="fig:scaling">

![](../paper_04_shallow_water/Pyfig/fig6.eps){#fig:D width=48% height=40%}
![](../paper_04_shallow_water/Pyfig/fig10.eps){#fig:E width=48% height=40%}

Shock separation $d$ and energy spectra $E(k)$ scaling
</div>

## Toy model equations

### Derivation of toy model equations^[@LindborgMohanan2017]

::: notes

with $\Psi$ and $\chi$ being the **stream function** and the **velocity potential** respectively.

:::

#### Helmholtz decomposition

$${\bf u} = \bf{u}_r + \bf{u}_d$$

 * ${\bf u}_r  = -\nabla \times ( {\bf e_z} \Psi)$ is the rotational component
 * $\bf {u}_d = \nabla \chi$ is the divergent component


. . .

#### Governing equations

- Starting from classical shallow water equations,

#### Assumptions & modifications {.cbox}

- <2-> Surface displacement much **smaller** compared to the mean fluid layer
  height, $\eta << 1$.

- <4->  Velocities in the large scale are **dominated by rotational part**,
  $|\bf u_r| >> |\bf u_d|$.

- <6-> Substitute $c\eta$ with $\theta$ (optional).


#### {.endblock}

\begin{align*}
\frac{\partial {\bf u}} {\partial t} + {
  \color<4>{purple}\only<-4>{{\uu}\, \cdot\, \nabla}
  \color<5->{teal}\only<5->{{\uu_r}\cdot \nabla}
  }
  {\bf u} +
  f {\bf e}_z \times {\bf u} &=
  \color<6>{purple}\only<-6>{-c^2 \nabla \eta} %
  \color<7->{teal}\only<7->{-c \nabla \theta} %
  \\
\frac{\partial 
  \color<6>{purple}\only<-6>\eta
  \color<7->{teal}\only<7->\theta
}{\partial t}+ {
  \color<4>{purple}\only<-4>{{\uu}\, \cdot\, \nabla}
  \color<5->{teal}\only<5->{{\uu_r}\cdot \nabla}
  }
  \color<6>{purple}\only<-6>\eta
  \color<7->{teal}\only<7->\theta
  &= -
  \color<7->{teal}\only<7->c
  \color<2>{purple}\only<2>{(1+\eta) \nabla \cdot {\bf u}}
  \color<3->{teal}\only<3->{\nabla \cdot {\bf u}}
\end{align*}

- <7-> Q.E.D.

### A good compromise^[@LindborgMohanan2017]

#### Pros {.gbox}

- No shocks

- KE and APE are **quadratic** and conserved

- Linearised potential vorticity $q$ conserved in the limit $Ro \to 0$, where $q=\zeta−f$

#### {.endblock}


#### Cons {.rbox}

-  Full potential vorticity $Q$ is not exactly conserved

#### {.endblock}


\centering{%
  {%
  \movie[
    width=8.5cm,
    height=4.3cm,
    showcontrols,
    poster,
    autostart, loop
  ]{}{./videos/toy_model_qa.mp4}

  Potential vorticity and wave fields in a toy model simulation}
}

### Energy spectra

<div id="fig:spectratoy">

![](../paper_03_toy_model/fig3.eps){ width=33% height=80% #fig:speck6}
![](../paper_03_toy_model/fig11.eps){width=33% height=80% #fig:speck30}

Time averaged energy spectra from two simulations by forcing at
(a) $k_f = 6\delta k$
(b) $k_f = 30\delta k$

</div>

---

::: notes

The total spectral energy flux $\Pi$
has been decomposed into kinetic ($\Pi_K$) and available potential energy
($\Pi_A$) energy fluxes. The conversion from available potential energy to
kinetic energy is represented by $C_{cum}$. The kinetic energy flux is further
decomposed as $\Pi_{2D}$, the flux due to geostrophic modes and the difference
$\Pi_K - \Pi_{2D}$.

:::

:::::::::::: {.columns}
::: {.column width="55%"}

#### Spectral energy budget

- **Spectral energy flux**, 
$\Pi(\mathbf{k},t) = \int_0^{\infty} T(\mathbf{k}',t) d\mathbf{k}'$

. . .

- $T=T_K + T_A$ are **transfer functions**,
  \begin{align*}
  \partial_t E_K(\mathbf{k},t) 
    &= \text{\textonehalf} \partial_t (\hat{\uu}\hat{\uu}^*)
    = T_K + C_K
    ,\quad\\
  \partial_t E_A(\mathbf{k},t) 
    &= \text{\textonehalf} \partial_t (\hat{\theta}\hat {\theta}^*)
    = T_A + C_A 
  \end{align*}
  which for the toy model equations
  are derived as $T_K=  \Im\left[\hat{u}_i^* k_j \widehat{u^r_j u_i}\right],\quad
  T_A  =  \Im\left[\hat{\theta}^* k_j \widehat{u^r_j \theta}\right]$.

:::
::: {.column}

. . .

#### Normal mode decomposition


- Linearization and diagonalization of the toy model equations yields the
  **normal modes**:
  \begin{align*}
      \mathbf{B}
      = & \frac{1}{\sqrt{2}\sigma}
      \begin{Bmatrix} \sqrt{2} c\left(-
          \kappa^{2} \hat \psi +  f\hat\eta \right)               \\
          \kappa \left(c^{2} \eta + f \hat{\psi} + i \hat{\chi} \sigma\right) \\
          \kappa \left(c^{2} \eta + f \hat{\psi} - i \hat{\chi} \sigma\right)
      \end{Bmatrix}.
  \end{align*}
  which can be transformed to $\mathbf{U} = \{\hat{u}_x,\hat{u}_y, \hat{\theta}\}^T$.

:::
:::::::::::::::::::::::::::::::::

. . .

![Spectral energy fluxes from two simulations with different forcing
schemes](../paper_03_toy_model/fig5.eps){height=52%}

### Comparison of a GCM^[@Augier-Lindborg:2013] with the toy model^[@LindborgMohanan2017] 
<div id="fig:sebgcmtoy">

![](../paper_03_toy_model/fig1.eps){width=50% height=60% #fig:sebgcm}
![](../paper_03_toy_model/fig10.eps){width=50% height=55% #fig:sebtoy}

Spectral energy budgets from (a) GCM and (b) toy model simulations. 

</div>

where, $\Pi_{2D} \equiv \Pi_{VVV}$.


# Part 2: MILESTONE experiment

## Motivation
## Setup
### Experimental setup
### Software systems
## Preliminary results


# Part 3: Reproducible open science through open source


## Open science


::::::::::: {.columns}
::: {.column}

![](../imgs/open_science.pdf){width=90%}

:::
::: {.column width="60%"}

#### Path to reproducible research

. . .

- Accessible knowledge: **open access**

. . .

- Tracking workflow: **version control**


- Accessible implementation: **license + source code**


- Reliable: **documentation**, **continuous integration**

. . .

- Open data: **citable datasets**

. . .

- Publish: **manuscript + data + code + workflow**

. . .


#### Arguments for open source

- Public money, public code^[https://publiccode.eu]

- Peer review for both manuscript and code

- Interoperable and sustainable

. . .

#### Arguments against open source

- Comparative advantage

- Lack of support

- Curb industrial usage

- Lack of documentation / not near production quality

:::
:::::::::::

### Python programming language

- One of the most popular languages^[Stack Overflow, GitHub, TIOBE index, IEEE
  spectrum] in the world

- General purpose

- Thriving scientific community

::::::::::: {.columns}
::: {.column width="50%"}

![](../imgs/python-sci-ecosystem.png){width=90%}

:::
::: {.column}

![](../imgs/python-popularity.png){width=90%}

:::
::::::::::::

### Why Python?

#### Advantages {.gbox}

- Elegant, expressive

- Automatic memory management and dynamic typing

- Extensible

- Batteries included: powerful standard libraries

#### {.endblock}

#### Issues and solutions {.cbox}

- CPU bounded performance
  + native (C, C++ or Fortran),  compiled (AOT or JIT)
    **extensions** for hotspots

- Concurrent, but no parallel threading
  + use **multiprocessing** / **MPI**

#### {.endblock}

## FluidDyn project

::::::::::: {.columns}
::: {.column width="40%"}

![Project to foster open-science and open-source in fluid
mechanics](../imgs/logo-fluiddyn.jpg){width="90%"}

. . .

- `fluiddyn`: base package

- `fluidfft`: API for Fast Fourier Transforms

- `fluidsim`: CFD framework

- `fluidimage`: asynchronously parallelized image processing, including PIV

- `fluidlab`: laboratory experiments

- `transonic`: front-end for generating Python extensions

:::
::: {.column}


![Standing on the shoulders of giants](../imgs/dependency.pdf){width="90%"}

:::
:::::::::::


---

::::::::::: {.columns}
::: {.column width="35%"}

#### Package `fluidfft`^[@fluidfft]

- FFT libraries: `FFTW`, `P3DFFT`, `PFFT`, `cuFFT`
  interfaced using `C++` and `Cython`

- "Operator" classes with `Pythran` methods

:::
::: {.column}


![Class hierarchy (pink: *sequential*, magenta: *CUDA*, green:
*MPI*)](../paper_01_fluidfft/Pyfig/fig_classes.pdf){width=100%}

:::
::::::::::: 

. . .

<div id="fig:">

![Strong scaling of 3D FFT upto 10000
cores](../paper_01_fluidfft/tmp/fig_beskow_1152x1152x1152.pdf){width=72%}
![Microbenchmarks of projection
function](../paper_01_fluidfft/tmp/fig_microbench.pdf){width=72%}

Performance of `fluidfft`

</div>

---

::::::::::: {.columns}
::: {.column width="40%"}

#### Package `fluidsim`^[@fluidsim]

- Extensible, object-oriented CFD framework

\small

```python

from fluidsim.solvers.ns3d.solver import Simul

params = Simul.create_default_params()

# Modify simulation parameters as needed

sim = Simul(params)
sim.time_stepping.start()

```

\normalsize

- On-the-fly post-processing

. . .

![Strong scaling for
`ns3d`](../paper_02_fluidsim/tmp/fig_bench_strong3d.pdf){width=110%}

:::
::: {.column}


<div id="fig">

. . .

![Profiling `ns3d`](../paper_02_fluidsim/tmp/fig_profile3d.pdf)

. . .

![Comparison of `fluidsim`'s `ns3d` with a Fortran based code
NS3D](../paper_02_fluidsim/tmp/fig_compare_with_ns3d.pdf)

</div>

:::
::::::::::: 

