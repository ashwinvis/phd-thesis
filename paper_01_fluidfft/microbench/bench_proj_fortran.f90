! benchmark of the function proj

program benchmark_proj
  implicit none
  integer, parameter :: N0=128, N1=128, N2=65, N=100
  double precision, allocatable :: vx(:,:,:,:), vy(:,:,:,:), vz(:,:,:,:)
  double precision, allocatable :: kx(:,:,:), ky(:,:,:), kz(:,:,:)
  double precision, allocatable :: inv_k_square_nozero(:,:,:)
  double precision, allocatable :: res(:,:,:,:,:)
  real :: start, finish, cumtime
  integer :: i

  allocate(vx(2, N2, N1, N0), vy(2, N2, N1, N0), vz(2, N2, N1, N0))
  allocate(kx(N2, N1, N0), ky(N2, N1, N0), kz(N2, N1, N0))
  allocate(inv_k_square_nozero(N2, N1, N0))

  call random_number(vx)
  call random_number(vy)
  call random_number(vz)
  call random_number(kx)
  call random_number(ky)
  call random_number(kz)
  call random_number(inv_k_square_nozero)

  cumtime = 0

  print*, "This program make some calculations."
  do i = 1, N
     call cpu_time(start)
     allocate(res(2, 3, N2, N1, N0))
     call proj(res, vx, vy, vz, kx, ky, kz, inv_k_square_nozero, N0, N1, N2)
     deallocate(res)
     call cpu_time(finish)
     cumtime = cumtime + finish - start
  enddo
  print '("Mean Time = ",f6.3," ms")', 1000*cumtime/N

  cumtime = 0

  print*, "without allocate/deallocate."
  allocate(res(2, 3, N2, N1, N0))
  do i = 1, N
     call cpu_time(start)
     call proj(res, vx, vy, vz, kx, ky, kz, inv_k_square_nozero, N0, N1, N2)
     call cpu_time(finish)
     cumtime = cumtime + finish - start
  enddo
  print '("Mean Time = ",f6.3," ms")', 1000*cumtime/N
  deallocate(res)

  deallocate(vx, vy, vz)
  deallocate(kx, ky, kz)
  deallocate(inv_k_square_nozero)
end program benchmark_proj


subroutine proj(res, vx, vy, vz, kx, ky, kz, inv_k_square_nozero, N0, N1, N2)

  implicit none

  ! Input/Output
  integer, intent(in) :: N0, N1, N2
  double precision, intent(in) :: vx(2, N2, N1, N0), vy(2, N2, N1, N0), vz(2, N2, N1, N0)
  double precision, intent(in) :: kx(N2, N1, N0), ky(N2, N1, N0), kz(N2, N1, N0)
  double precision, intent(in) :: inv_k_square_nozero(N2, N1, N0)
  double precision, intent(out) :: res(2, 3, N2, N1, N0)

  ! Locals
  double precision :: tmp(2)
  integer:: i, j, k

  do k = 1, N0
     do j = 1, N1
        do i = 1, N2
           tmp(1:2) = (kx(i,j,k) * vx(1:2,i,j,k) &
                + ky(i,j,k) * vy(1:2,i,j,k) &
                + kz(i,j,k) * vz(1:2,i,j,k)) * inv_k_square_nozero(i,j,k)

           res(1:2,1,i,j,k) = vx(1:2,i,j,k) - kx(i,j,k) * tmp(1:2)
           res(1:2,2,i,j,k) = vy(1:2,i,j,k) - ky(i,j,k) * tmp(1:2)
           res(1:2,3,i,j,k) = vz(1:2,i,j,k) - kz(i,j,k) * tmp(1:2)
        enddo
     enddo
  enddo

end subroutine proj
