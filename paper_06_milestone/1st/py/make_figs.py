from pathlib import Path
import os
import sys
from datetime import datetime
from runpy import run_path


def modification_date(filename):
    """Get the modification date of a file"""
    return datetime.fromtimestamp(os.path.getmtime(str(filename)))


def has_to_build(output_file: Path, input_file: Path):
    """Check if a file has to be (re)built"""
    output_file = Path(output_file)
    input_file = Path(input_file)
    if not output_file.exists():
        return True
    mod_date_output = modification_date(output_file)
    if mod_date_output < modification_date(input_file):
        return True
    return False


sys.argv.append("save_for_tex")

here = Path(__file__).parent.absolute()

scripts = sorted(here.glob("make_fig_*"))

path_tmp = here.parent / "tmp"

scripts = [
    script for script in scripts if script.name != "make_fig_other_studies.py"
]

figure_names = {path: path.name[5:-3] + ".png" for path in scripts}

for script, figure in figure_names.items():

    if has_to_build(path_tmp / figure, script):
        print("run", script)
        run_path(str(script))


script = here / "make_fig_other_studies.py"

figures = [
    "fig_R_vs_Fh_other_studies_with_milestone",
    "fig_R_vs_Fh_other_studies_with_milestone17",
]

for figure in figures:
    path_fig = path_tmp / (figure + ".png")
    if has_to_build(path_fig, script):
        sys.argv.append(figure.split("with_")[1])
        print("run", script)
        run_path(script)
        sys.argv.pop()


figures = [
    "fig_rho_vs_time.png",
    "fig_rho_vs_time_corrected.png",
    "fig_profiles_mixing.png",
    "fig_profiles_probe_averaged.png",
    "fig_energy_pot_vs_time.png",
]
script = here / "make_figs_probes.py"

if any(has_to_build(path_tmp / figure, script) for figure in figures):
    print("run", script)
    run_path(script)