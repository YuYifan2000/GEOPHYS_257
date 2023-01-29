#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --partition debug
#SBATCH --time=0-2
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --dependency=afterok:779
python ./summation.py
