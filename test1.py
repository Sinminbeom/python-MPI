import time

from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    start = time.time()

    myrank = comm.Get_rank()
    world_size = comm.Get_size()

    data_count = 100
    part_size = int(data_count / world_size)
    # print(part_size)

    i_start = myrank * part_size
    i_end = i_start + part_size



    if (myrank == (world_size - 1)):
        i_end = data_count

    x = []
    for i in range(i_start, i_end):
        x.append(i)

    print("My Rank = ", myrank, len(x), print(x))
    # print("My Rank = ", myrank, ", len = ", len(x))

    time_end = time.time()
    print("Total time taken = ", (time_end - start))

    gathered_x = comm.gather(x, root=0)
    # if (myrank == 0):
    #     print(gathered_x)


if __name__ == '__main__':
    main()
