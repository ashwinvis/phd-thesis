
from numpy.random import random

from proj import (
    proj as proj0,
    proj_loop as proj_loop0,
    proj_inplace as proj_inplace0,
    proj_inplace_loop as proj_inplace_loop0
)

from proj_pythran import (
    proj,
    proj_loop,
    proj_inplace,
    proj_inplace_loop
)

import proj_pythran

try:
    from proj_numba import (
        proj as proj_numba,
        proj_loop as proj_loop_numba,
        proj_inplace as proj_inplace_numba,
        proj_inplace_loop as proj_inplace_loop_numba
    )
except ImportError:
    pass

assert hasattr(proj_pythran, '__pythran__')

__all__ = [
    'proj0',
    'proj_loop0',
    'proj_inplace0',
    'proj_inplace_loop0',
    'proj',
    'proj_loop',
    'proj_inplace',
    'proj_inplace_loop',
    # 'proj_numba',
    # 'proj_loop_numba',
    # 'proj_inplace_numba',
    # 'proj_inplace_loop_numba',
]


n0 = n1 = n2 = 128

shape = (n0, n1, n2//2+1)

c0 = 1j*random(shape) + random(shape)
c1 = 1j*random(shape) + random(shape)
c2 = 1j*random(shape) + random(shape)

a0 = random(shape)
a1 = random(shape)
a2 = random(shape)
a3 = random(shape)

try:
    # JIT compiler
    for func in (proj_numba,
                 proj_loop_numba,
                 proj_inplace_numba,
                 proj_inplace_loop_numba):
        func(c0, c1, c2, a0, a1, a2, a3)
except NameError:
    pass
