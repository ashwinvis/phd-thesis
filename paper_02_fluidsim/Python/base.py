from string import ascii_lowercase
import os
from fluiddyn.output.rcparams import set_rcparams
import matplotlib.pyplot as plt


titles = ['({})'.format(a) for a in ascii_lowercase]

curdir = os.path.dirname(__file__)

def matplotlib_rc(
        fontsize=8, dpi=300, tex=True, interactive=False):

    set_rcparams(fontsize, for_article=True, for_beamer=False)
    plt.rc('legend', fontsize=fontsize-2)
    plt.rc('font', size=fontsize)
    plt.rc('figure', dpi=dpi)
    plt.rc('xtick', direction='in')
    plt.rc('ytick', direction='in')

    if interactive:
         plt.ion()
    else:
         plt.ioff()
