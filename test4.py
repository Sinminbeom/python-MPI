import time

from mpi4py import MPI

# mpirun -np 2 python sendRecvTest.py
# mpirun -np 3 python sendRecvTest.py
def main():
    comm = MPI.COMM_WORLD
    start = time.time()

    my_rank = comm.Get_rank()
    world_size = comm.Get_size()
    count = 0
    if (my_rank == 0):
        print(my_rank, "sender")
        comm.send(30, dest=1)
        comm.send(20, dest=2)

    if (my_rank == 1):
        data = comm.recv(source=0)
        print(my_rank, "-", my_rank * data)
        count = my_rank * data

    if (my_rank == 2):
        data = comm.recv(source=0)
        print(my_rank, "-", my_rank * data)
        count = my_rank * data

    count_x = comm.gather(count, root=0)
    if (my_rank == 0):
        print(sum(count_x))


if __name__ == '__main__':
    main()