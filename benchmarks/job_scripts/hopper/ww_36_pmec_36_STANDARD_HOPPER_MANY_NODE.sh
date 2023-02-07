#!/usr/bin/bash
#SBATCH --output ../../../benchmark_tests/standard_torsten/ww_36_pmec_36_Hopper_Standard_many_node
#SBATCH --error ../../../benchmark_tests/standard_torsten/ww_36_pmec_36_Hopper_Standard_many_node_err
#SBATCH --partition general
#SBATCH --ntasks=64
#SBATCH --nodes=2

#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --mail-user=ageyko@unm.edu

module load openmpi

srun --partition=general --nodes=2 --ntasks=48 --time=24:00:00 ../../../build/benchmarks/torsten_standard_comm ../../../test_data/ww_36_pmec_36.pm 5 ww_36_pmec_36 STANDARD
srun --partition=general --nodes=2 --ntasks=64 --time=24:00:00 ../../../build/benchmarks/torsten_standard_comm ../../../test_data/ww_36_pmec_36.pm 5 ww_36_pmec_36 STANDARD