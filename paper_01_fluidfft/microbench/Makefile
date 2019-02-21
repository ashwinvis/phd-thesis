
# modpythran=proj_pythran.pypy3-60-x86_64-linux-gnu.so
modpythran=proj_pythran.so

FLAGS=-O3 -march=native

perf: perfpythran

clean: cleanfortran
	rm -f *.so

cleanfortran:
	rm -f bench_proj_fortran.out

code = 'func(c0, c1, c2, a0, a1, a2, a3)'
end=as func, c0, c1, c2, a0, a1, a2, a3

perfnumpy: $(modpythran)
	# numpy proj
	@python -m perf timeit -s 'from bench import proj0 $(end)' $(code)
	@# python -m perf timeit -s 'from bench import proj_loop0 $(end)' $(code)
	# numpy proj_inplace
	@python -m perf timeit -s 'from bench import proj_inplace0 $(end)' $(code)
	@# python -m perf timeit -s 'from bench import proj_inplace_loop0 $(end)' $(code)

perfpythran: $(modpythran)
	# pythran proj_loop
	@python -m perf timeit -s 'from bench import proj_loop $(end)' $(code)
	# pythran proj_inplace_loop
	@python -m perf timeit -s 'from bench import proj_inplace_loop $(end)' $(code)
	# pythran proj
	@python -m perf timeit -s 'from bench import proj $(end)' $(code)
	# pythran proj_inplace
	@python -m perf timeit -s 'from bench import proj_inplace $(end)' $(code)


perfnumba:
	@# numba proj
	@# python -m perf timeit -s 'from bench import proj_numba $(end)' $(code)
	@# numba proj_inplace
	@# python -m perf timeit -s 'from bench import proj_inplace_numba $(end)' $(code)
	# numba proj_loop
	@ python -m perf timeit -s 'from bench import proj_loop_numba $(end)' $(code)
	# numba proj_inplace_loop
	@python -m perf timeit -s 'from bench import proj_inplace_loop_numba $(end)' $(code)


# we don't use -DUSE_BOOST_SIMD because it is not yet implemented for complex.

$(modpythran): proj.py
	pythran -v proj.py $(FLAGS) -o $(modpythran)


perffortran: bench_proj_fortran.out bench_proj_fortran_inplace.out
	./bench_proj_fortran.out
	./bench_proj_fortran_inplace.out

bench_proj_fortran.out: bench_proj_fortran.f90
	gfortran bench_proj_fortran.f90 $(FLAGS) -o bench_proj_fortran.out

bench_proj_fortran_inplace.out: bench_proj_fortran_inplace.f90
	gfortran bench_proj_fortran_inplace.f90 $(FLAGS) -o bench_proj_fortran_inplace.out
