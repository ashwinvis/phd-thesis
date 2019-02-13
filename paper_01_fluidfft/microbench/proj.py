
import numpy as np

# pythran export proj(
#     complex128[][][], complex128[][][], complex128[][][],
#     float64[][][], float64[][][], float64[][][], float64[][][])

def proj(vx, vy, vz, kx, ky, kz, inv_k_square_nozero):
    tmp = (kx * vx + ky * vy + kz * vz) * inv_k_square_nozero
    return vx - kx * tmp, vy - ky * tmp, vz - kz * tmp

# pythran export proj_loop(
#     complex128[][][], complex128[][][], complex128[][][],
#     float64[][][], float64[][][], float64[][][], float64[][][])


def proj_loop(vx, vy, vz, kx, ky, kz, inv_k_square_nozero):

    rx = np.empty_like(vx)
    ry = np.empty_like(vx)
    rz = np.empty_like(vx)

    n0, n1, n2 = kx.shape

    for i0 in range(n0):
        for i1 in range(n1):
            for i2 in range(n2):
                tmp = (kx[i0, i1, i2] * vx[i0, i1, i2]
                       + ky[i0, i1, i2] * vy[i0, i1, i2]
                       + kz[i0, i1, i2] * vz[i0, i1, i2]
                ) * inv_k_square_nozero[i0, i1, i2]

                rx[i0, i1, i2] = vx[i0, i1, i2] - kx[i0, i1, i2] * tmp
                ry[i0, i1, i2] = vz[i0, i1, i2] - kx[i0, i1, i2] * tmp
                rz[i0, i1, i2] = vy[i0, i1, i2] - kx[i0, i1, i2] * tmp

    return rx, ry, rz


# pythran export proj_inplace(
#     complex128[][][], complex128[][][], complex128[][][],
#     float64[][][], float64[][][], float64[][][], float64[][][])


def proj_inplace(vx, vy, vz, kx, ky, kz, inv_k_square_nozero):
    tmp = (kx * vx + ky * vy + kz * vz) * inv_k_square_nozero

    vx -= kx * tmp
    vy -= ky * tmp
    vz -= kz * tmp


# pythran export proj_inplace_loop(
#     complex128[][][], complex128[][][], complex128[][][],
#     float64[][][], float64[][][], float64[][][], float64[][][])


def proj_inplace_loop(vx, vy, vz, kx, ky, kz, inv_k_square_nozero):

    n0, n1, n2 = kx.shape

    for i0 in range(n0):
        for i1 in range(n1):
                for i2 in range(n2):
                    tmp = (kx[i0, i1, i2] * vx[i0, i1, i2]
                           + ky[i0, i1, i2] * vy[i0, i1, i2]
                           + kz[i0, i1, i2] * vz[i0, i1, i2]
                    ) * inv_k_square_nozero[i0, i1, i2]

                    vx[i0, i1, i2] -= kx[i0, i1, i2] * tmp
                    vy[i0, i1, i2] -= ky[i0, i1, i2] * tmp
                    vz[i0, i1, i2] -= kz[i0, i1, i2] * tmp
