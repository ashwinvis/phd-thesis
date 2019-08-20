# Preliminary results

The experiment was conducted as two campaigns in the years 2016 and 2017,
hitherto referred to with the prefixes M16 and M17.
The two experimental setups are nearly identical. They differ mainly on the
precise location of the density and temperature probes, the number and
location of the cameras used for PIV, and the stroke pattern of the oscillating
comb.
Here we highlight some of the important results reported in @campagne2016 and
ongoing post-experiment analysis.

The experiment with parameters $N = 0.8$ rad/s, $U_c = 6$ cm/s, $F_{hc} = 0.1$
and $\R_c = 450$ from M16 campaign is described here. The oscillating comb was
observed to inject kinetic energy $u^2 \approx 0.08 U_c^2$. The emergence of
layered structures with vertical length scale of \order{1} cm can be visually
observed in the velocity fields plotted in @fig:field, thereby conforming to
the prediction $l_v \sim u / N$. Note that, there is a time delay when similar
dynamics are captured in the horizontal (top row) and vertical (bottom row) PIV
fields.

\begin{figure}[htb]
\centerline{
\includegraphics[width=4.14cm]{paper_05_milestone_issf/Figures/exp21/vh_400.pdf}
\includegraphics[width=3.44cm]{paper_05_milestone_issf/Figures/exp21/vh_655.pdf}
\includegraphics[width=4.72cm]{paper_05_milestone_issf/Figures/exp21/vh_890.pdf}}
\vspace{0mm}
\centerline{
\includegraphics[width=4.16cm]{paper_05_milestone_issf/Figures/exp21/vv_890.pdf}
\includegraphics[width=3.48cm]{paper_05_milestone_issf/Figures/exp21/vv_655.pdf}
\includegraphics[width=4.63cm]{paper_05_milestone_issf/Figures/exp21/vv_400.pdf}
}
\vspace{-2mm}
\caption{Instantaneous horizontal large fields (top, $z=40$~cm) and vertical
fields (bottom) for $t/T = [1.31,~1.5,~1.68]$, $F_{hc} = 0.1$ and
$\mathcal{R}_c=450$. Background colors indicate the norm of the 2D field
normalized by $U_c$, which is $(u_x^2 + u_y^2)/U_c$ and $(u_x^2 + u_z^2)/U_c$,
respectively.}
\label{fig:field}
\end{figure}

In @fig:S2, we plot the normalized second-order structure function,
defined as
\begin{eqnarray}
S_h(r) = (S_{xx} + S_{yy} + S_{xy} + S_{yx})/2,
\end{eqnarray}
with $S_{ij} = \langle\overline{(u_i({\bf x}+r{\bf e}_j)-u_i({\bf
x}))^2}\rangle$, and $\overline{}$ as time average when the carriage is moving.
For fully developed turbulence undergoing forward cascade we expect second
order structure functions to scale as  $S_h(r) = C (\varepsilon r)^{2/3}$
[@Lindborg2006;@AugierBillantChomaz2015]. In @fig:S2
the normalized structure function $S_h(rU_c^3/M)^{-2/3}$ is plotted for
different times after one stroke of the carriage. As can be seen, there is a
range where the curves are flat consistent with the prediction $S_h \sim
r^{2/3}$.

\begin{figure}[htb]
\centerline{
\includegraphics[width=0.7\textwidth]{paper_05_milestone_issf/Figures/exp28/normalized_S2_exp28.pdf}}
\vspace{-2mm}
\caption{Normalized second-order structure $S_h$ function as a function of
$r/M$ for $F_{hc} = 0.1$ and $\mathcal{R}_c=450$. The arrow represents the
progress of time as the total energy decays.}
\label{fig:S2}
\end{figure}


\begin{figure}[htp!]
\centerline{
\includegraphics[width=0.45\textwidth]{paper_06_milestone/1st/tmp/fig_energy_pot_vs_time}
\includegraphics[width=0.55\textwidth]{paper_06_milestone/1st/tmp/fig_dt_pot_energy}
}
\caption{Evolution of potential energy normalized by linear stratification for
experiment M17-21 (left) and normalized mixing coefficient $\eps_P /
(3\times10^{-3} {U_c}^3/D_c)$ for some MILESTONE 17 experiments (right).}%
\label{fig:dt:pot:energy}

\end{figure}

The evolution of the background potential energy is shown in the left plot of
@fig:dt:pot:energy for an experiment from M17-21 with parameters $N = 0.55$
rad/s, $U_c = 12$ cm/s, $F_{hc} = 0.436$ and $\R_c = 11425$.  The value
-1 would correspond to a linear stratification with the same initial
\text{Brunt-V\"ais\"al\"a} frequency. Since the profiles at the beginning of the
experiment are already eroded from previous experiments, the initial normalized
potential energy is slightly smaller than -0.6. We see that it increases
approximately linearly with time while the fluid is stirred and stabilize at a
constant value after the stop of the carriage. From this curve, we can evaluate
the mean rate of increase of the average background potential energy
$\eps_P$ during an experiment.
This quantity $\eps_P$ is normalized by an estimation of the dissipation of
kinetic energy $3\times10^{-3} {U_c}^3/D_c$ where $D_c$ is the diameter of the
cylinder and is approximately proportional to the mixing coefficient $\Gamma$.
It is plotted as a function of the Froude number in
figure~\ref{fig:dt:pot:energy}.
The colors represent the buoyancy Reynolds number
such that the yellow points correspond to $\R > 15$. We see that the yellow
points fall on a power law fit of $F_h^{-1.2}$, while there are more variations
for smaller values of buoyancy Reynolds number. The yellow points at high
$F_h$ are more consistent with a ${F_h}^{-2}$ scaling law observed and
predicted with @maffioli_mixing_2016.

At this stage, these results seem promising but should be taken with a grain of
salt as they are not final. Since we observe too much spread in some results
and some values are larger than what has been theoretically and numerically
observed, there might be overlooked errors in the interpretation of the
results. A third series of experiments might be needed to confirm the findings.
