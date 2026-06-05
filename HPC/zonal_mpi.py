from mpi4py import MPI
import rasterio
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

filename = "/project/JehoPark_1421/Student_Files/CMC_Testpartial_ortho.tiff"

# ── Start timer ───────────────────────────────────────────
if rank == 0:
    t_start = MPI.Wtime()

# Load raster on root process
if rank == 0:
    with rasterio.open(filename) as src:
        data = src.read(1)
        nodata = src.nodata
        shape = data.shape
else:
    data = None
    nodata = None
    shape = None

# Broadcast metadata
shape = comm.bcast(shape, root=0)
nodata = comm.bcast(nodata, root=0)

# Scatter data
if rank == 0:
    rows_per_proc = shape[0] // size
    chunks = [data[i*rows_per_proc:(i+1)*rows_per_proc, :] for i in range(size)]
else:
    chunks = None

local_data = comm.scatter(chunks, root=0)

# Compute local mean (ignoring nodata)
local_mean = np.mean(local_data[local_data != nodata])

# Gather and compute global mean
global_mean = comm.reduce(local_mean, op=MPI.SUM, root=0)

# ── Results + timing ──────────────────────────────────────
comm.Barrier()
if rank == 0:
    elapsed = MPI.Wtime() - t_start
    global_mean /= size
    print(f"Average Elevation: {global_mean:.2f} meters")
    print(f"Ranks used:        {size}")
    print(f"Total wall time:   {elapsed:.4f} seconds")
