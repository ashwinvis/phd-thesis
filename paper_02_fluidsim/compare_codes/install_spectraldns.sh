#!/bin/bash
mkdir spectralDNS
cd spectralDNS

## Use the following if you use virtualenvwrapper like me ;)
# mkvirtualenv -p python2 --system-site-packages spectraldns_python
# virtualenv -p python2 -system-site-packages spectraldns_python
virtualenv -p python2 spectraldns_python
source spectraldns_python/bin/activate

python -m pip install pytest nodepy mpi4py cython numpy scipy pythran numba colorlog h5py

git clone https://github.com/spectralDNS/mpiFFT4py.git
cd mpiFFT4py
python setup.py build_ext --inplace
python setup.py install
cd ..

git clone https://github.com/spectralDNS/mpi4py-fft.git
cd mpi4py-fft
python setup.py build_ext --inplace
python setup.py install
cd ..

git clone https://github.com/drwells/pyFFTW.git
cd pyFFTW
git checkout r2r-try-two
python setup.py install
cd ..


git clone https://github.com/spectralDNS/shenfun.git
cd shenfun
python setup.py build_ext --inplace
python setup.py install
cd ..

git clone https://github.com/spectralDNS/spectralDNS.git
cd spectralDNS
python setup.py build_ext --inplace
python setup.py install

pwd > $VIRTUAL_ENV/.project

cd tests
python -m pytest -v
