\chapter{Atmospheric turbulence and Shallow Water and Toy Model Equations}

Atmospheric turbulence is characterized by a huge scale separation of fluid motion,
ranging from the order of a hundred metres to several thousands of kilometres.
The knowledge of how energy is distributed across such scales in the atmosphere and what
kind of interactions leads to the energy cascade between large and small scales is
essential to improve our general circulation models (GCM) while also recognizing the
limits of predictability [see @lorenz_predictability_1969;@vallis_atmospheric_2017
pp. 433--447].

This chapter introduces the work done to come up with the simplest possible model which
can emulate the atmospheric kinetic energy spectrum and the advances which motivated
this study. Before we delve into the details of the present work, let us have a look at
what we already know about the atmospheric turbulence and what are the open questions.

# Background

## Synoptic and Mesoscale circulation

The latter half of the twentieth century presented exciting insights into how energy
scales in the atmosphere. Several researchers in the 1960s found that large-scale or
*synoptic* circulation in the atmosphere, and especially the kinetic energy spectra,
behaves differently when compared with well-known theories for three-dimensional (3D)
homogeneous and isotropic turbulence by Kolmogorov. It was identified through
observational evidences [@horn_analysis_1963] and later on by GCM
calculations [@wellck_effect_1971] that energy scales as $k^{-3}$. Such a spectra
implies that the underlying mechanism is different in comparison with 3D turbulence
which expects a inertial range which scales as $k^{-5/3}$ with forward energy cascade.

Postulates were also made that in two-dimensional turbulence, vorticity and enstrophy
conservation and the absence of vortex stretching mechanism places a strong constraint
on the cascade [see for example, @fjortoft_changes_1953;@charney_geostrophic_1971].
These developments led to the seminal work by @kraichnan_inertial_1967 wherein a theory
for a coexistence of a dual inertial range was conjectured. The presence of a
large-scale inertial range dominated by inverse-energy cascade and energy spectra which
scales as $E(k) \sim \epsilon^{2/3} k^{-5/3}$, along with a smaller-scale
spectra with inertial range characterized by forward enstrophy cascade which scale as
$E(k) \sim \eta^{2/3} k^{-3}$ was predicted.
