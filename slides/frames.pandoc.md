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

**Atmospheric energy spectrum**\footnote[frame]{\tiny \citet{NastromGage1985} \textcopyright AMS}

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

- Spatial scales of inertial ranges:
  !["A paradox"[^frisch]](../imgs/cascade_horiz.png){width=70% height=40%}

[^kraichnan]: \tiny @Kraichnan1967
[^kolmo]: \tiny Similar to @Kolmogorov1941's theory
[^frisch]: @Frisch

### Quasi geostrophic equation

- Quasi-geostrophic equation conserves an approximate *potential vorticity*:
  $$\Dt{q} = 0,$$
  $$ q = \nabla^2 \psi + \frac{\alert<2>{f_0}^2}{\tilde \rho}
  \left(\frac{\tilde \rho}{\alert<3>{N}^2} \p_z \psi \right) + \alert<2>{\beta} y, $$

. . .

- Incorporates \alert<2>{rotation} and \alert<3>{stratification} in a 2D model

- Bridging **ideal 2D turbulence** to **atmospheric turbulence**

- Reproduces $k^{-3}$ spectrum^[\tiny @Charney1971]

- <4-> Valid for **strong rotation**, lengths scales **smaller than
  planetary** scales

- <5-> No ageosophic motion, for example: **inertial gravity waves**

<6-> \centering{{\alert{What about the $k^{-5/3}$ mesoscale spectrum?}}}


### Possible theoretical explanations

#### Propositions {.cbox}

Here

#### {.endblock}

. . .

#### Stratified turbulence {.cbox}


#### {.endblock}

\end{mycolorbox}

Mamma mia


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

