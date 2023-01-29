#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --partition cpu
#SBATCH --time=0-2
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1

spack load python
python3 ./leib.py
