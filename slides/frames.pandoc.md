### Disputation i Teknisk Mekanik

::: notes

  The chair describes the procedure

:::


**Fredag 2019-09-27, kl 10:00**

-------------------------- ----------------------------------------------------------------
           **Respondent:** Ashwin Vishnu Mohanan

                **Titel:** Advancements in stratified flows through simulation,
                           experiment and open research software development

           **Handledare:** Dr. Erik Lindborg

                           Dr. Pierre Augier

    **Fakultetsopponent:** Prof. James J. Riley, University of Washington, U.S.A.

          **Betygsnämnd:** Prof. Johan Nilsson, Stockholms Universitet, Sverige

                           Dr. Thorsten Mauritsen, Stockholms Universitet, Sverige

                           Dr. Clara Marika Velte, Danmarks Tekniske Universitet, Danmark

           **Ordförande:** Prof. Nicholas Apazidis

            **Sponsorer:** Vetenskapsrådet, SNIC

-------------------------- ----------------------------------------------------------------


### Procedure


-   **The respondent will present his thesis**

-   **The opponent will discuss the thesis**

-   **The grading committee will ask questions**

-   **The audience will ask questions**

-   **Public part of the defence will be closed**

-   **The result will be announced at Osquars Backe 18, floor 6**

### Outline

\tableofcontents

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




## Toy model equations



## Results

# Part 2: MILESTONE experiment

## Experimental setup

## Software systems

## Preliminary results


# Part 3: Open research software

## Methods and tools for software development

## Python programming language

## FluidDyn project

## Performance

