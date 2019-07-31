from pathlib import Path

from fluidcoriolis.milestone import Experiment
from fluidcoriolis.milestone17.exp import iexps_strat, create_exp
from fluidcoriolis.milestone17.time_signals import comments

from util import path_tmp, iexps_norot

path_tmp = Path(path_tmp)

lines = []

for iexp in iexps_norot:
    exp = Experiment(iexp)
    lines.append(
        fr" M16-{exp.iexp:02d} &  {100 * exp.Uc:2.0f} &  "
        fr"{100 * exp.Dc:2.0f} &  "
        fr"{exp.N_measured:.2f} &  {exp.Fhc:.3f} &  {exp.Rec:5.0f} &  "
        fr"{exp.Rc:5.0f}"
    )


iexps = [
    iexp
    for iexp in iexps_strat
    if iexp in comments and comments[iexp].startswith("ok")
]

iexps_bad = (
    24,  # too mixed at the beginning
    57,
    58,  # horizontal cylinders
    15,  # not long enough
)

iexps = [iexp for iexp in iexps if iexp not in iexps_bad]

for iexp in iexps:
    exp = create_exp(iexp)
    if exp.Uc == 0:
        continue

    lines.append(
        fr" M17-{exp.iexp:02d} &  {100 * exp.Uc:2.0f} &  "
        fr"{100 * exp.Dc:2.0f} &  "
        fr"{exp.N:.2f} &  {exp.Fhc:.3f} &  {exp.Rec:5.0f} &  "
        fr"{exp.Rc:5.0f}"
    )

code_line = " \\\\\n".join(lines)

latex_code = rf"""
\begin{{table}}
\caption{{\label{{table:exp}} Experiments used for this study.}}
\begin{{ruledtabular}}
\begin{{tabular}}{{l{6 * 'c'}}}
    &   $Uc$ &  $D_c$ &  $N$  &  $F_{{hc}}$ &  $Re_c$ &   $\R_c$  \\
    & (cm/s) &   (cm) &(rad/s)&           &         &           \\

{code_line} \\
\end{{tabular}}
\end{{ruledtabular}}
\end{{table}}
"""

# print(latex_code)

with open(path_tmp / "table.tex", "w") as file:
    file.write(latex_code)
