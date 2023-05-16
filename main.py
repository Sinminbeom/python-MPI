from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD

    myrank = comm.Get_rank()
    rank_size = comm.Get_size()

    if (myrank == 0):
        print("I will do dishwashing, says A with rank ", myrank)
        print("World size is ", rank_size)

    if (myrank == 1):
        print("I will do clothes folding, says B with rank ", myrank)
        print("World size is ", rank_size)


if __name__ == '__main__':
    main()