#!/bin/bash
#SBATCH --job-name=zonal_mpi
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=1:00:00

echo "=========================================="
echo "SLURM_JOB_ID = $SLURM_JOB_ID"
echo "Running on: $(hostname)"
echo "=========================================="

module purge
module load gcc
module load openmpi

# Full path to your env - no conda activate needed
PYTHON=~/.conda/envs/workshop_test/bin/python
MPIEXEC=/apps/spack/2406/apps/linux-rocky8-x86_64_v3/gcc-13.3.0/openmpi-5.0.5-mufqd73/bin/mpiexec

export LD_LIBRARY_PATH=/apps/spack/2406/apps/linux-rocky8-x86_64_v3/gcc-13.3.0/openmpi-5.0.5-mufqd73/lib:$LD_LIBRARY_PATH

echo "Python:  $PYTHON"
echo "mpiexec: $MPIEXEC"
echo "=========================================="

$MPIEXEC -n 4 $PYTHON zonal_mpi.py
