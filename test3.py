import time

from mpi4py import MPI

# mpirun -np 2 python sendRecvTest.py
# mpirun -np 3 python sendRecvTest.py
def main():
    comm = MPI.COMM_WORLD
    start = time.time()

    my_rank = comm.Get_rank()
    world_size = comm.Get_size()

    if (my_rank == 0):
        print(my_rank)
        comm.send("hello receiver1", dest=1)
        comm.send("hello receiver2", dest=2)

    if (my_rank == 1):
        print(my_rank)
        data = comm.recv(source=0)
        print(data)

    if (my_rank == 2):
        print(my_rank)
        data = comm.recv(source=0)
        print(data)


if __name__ == '__main__':
    main()
