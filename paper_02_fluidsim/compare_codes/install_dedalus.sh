#!/bin/bash
# set -e

## Use the following if you use virtualenvwrapper like me ;)
# mkvirtualenv -p python3 --system-site-packages dedalus_python
# python3 -m venv --system-site-packages dedalus_python
python3 -m venv -p python3 dedalus_python
source dedalus_python/bin/activate

hg clone https://bitbucket.org/dedalus-project/dedalus
cd dedalus

pip install -r requirements.txt

# Set to help Dedalus find the proper libraries
# export FFTW_PATH=/usr
# export MPI_PATH=
# export MPI_INCLUDE_PATH=/usr/include/mpi
python setup.py build_ext --inplace
python setup.py install

pwd > $VIRTUAL_ENV/.project
# python -c 'from dedalus.tests.special_functions import airy; airy.test_airy()'
# python -c 'from dedalus.tests.special_functions import bessel; bessel.test_bessel()'
echo '*******************************************************************'
echo Example scripts:
echo python examples/ivp/2d_rayleigh_benard/rayleigh_benard.py
echo python examples/ivp/3d_rayleigh_benard/rayleigh_benard.py
echo '*******************************************************************'
