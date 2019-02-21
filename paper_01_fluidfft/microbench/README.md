
Done on my (pa) laptop (see sys_info_laptop-pierre-kth.xml).

I used:

```
sudo python -m perf system tune
```

## outplace

### fortran with allocate/deallocate
Mean Time = 22.1 ms

### fortran without allocate/deallocate
Mean Time = 11.3 ms

### numpy proj
Mean +- std dev: 66.6 ms +- 0.7 ms

### pythran proj
Mean +- std dev: 36.2 ms +- 0.8 ms
Mean +- std dev: 38.8 ms +- 3.1 ms

(pypy)
Mean +- std dev: 30.6 ms +- 0.9 ms

### pythran proj_loop
Mean +- std dev: 19.1 ms +- 1.0 ms
Mean +- std dev: 19.8 ms +- 1.4 ms

(pypy)
Mean +- std dev: 25.9 ms +- 0.9 ms

### numba proj
Mean +- std dev: 78.1 ms +- 2.0 ms

### numba proj_loop
Mean +- std dev: 26.5 ms +- 2.5 ms
Mean +- std dev: 24.4 ms +- 0.2 ms


## inplace

### fortran inplace
Mean Time = 9.0 ms

### numpy proj_inplace
Mean +- std dev: 54.2 ms +- 2.4 ms

### pythran proj_inplace
Mean +- std dev: 18.3 ms +- 1.1 ms
Mean +- std dev: 18.7 ms +- 0.8 ms

(pypy)
Mean +- std dev: 18.8 ms +- 1.1 ms

### pythran proj_inplace_loop
Mean +- std dev: 8.41 ms +- 0.52 ms
Mean +- std dev: 8.60 ms +- 0.08 ms

(pypy)
Mean +- std dev: 8.12 ms +- 0.09 ms

### numba proj_inplace
Mean +- std dev: 65.9 ms +- 1.2 ms

### numba proj_inplace_loop
Mean +- std dev: 16.3 ms +- 1.5 ms
Mean +- std dev: 15.8 ms +- 2.6 ms
Mean +- std dev: 14.6 ms +- 0.9 ms
