from util import plt, show, save

from fluidcoriolis.milestone17.time_signals import SignalsExperiment


def unset_title(fig):
    fig.axes[0].set_title(None)


iexp = 21
signals = SignalsExperiment(iexp)

signals.plot_vs_times()
fig = plt.gcf()
unset_title(fig)
save(fig, "fig_rho_vs_time.png")

signals.plot_vs_times(corrected=1)
fig = plt.gcf()
unset_title(fig)
save(fig, "fig_rho_vs_time_corrected.png")

probe = signals.probes_profiles[0]
probe.plot_profiles(corrected=1)
fig = plt.gcf()
save(fig, "fig_profiles_mixing.png")

signals.plot_profiles_probe_averaged(
    corrected=1, sort=1, extend=1, len_extend=0.005
)
fig = plt.gcf()
save(fig, "fig_profiles_probe_averaged.png")

signals.plot_energy_pot_vs_time()
fig = plt.gcf()
plt.gca().set_ylabel("normalized $E_P$")
unset_title(fig)
save(fig, "fig_energy_pot_vs_time.png")

show()
