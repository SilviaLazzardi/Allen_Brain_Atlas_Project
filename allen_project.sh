#!/usr/bin/env bash

# VARIABLES

DONORS_LIST=(9861 10021 12876 14380 15496 15697)

#PATHS

mkdir DATA
mkdir DATA/RAW_DATA
mkdir DATA/PREPROCESSED_DATA

PATH_RAW_DATA=DATA/RAW_DATA
PATH_MATRIX_DATA=DATA/PREPROCESSED_DATA

# PYTHON COMMANDS

echo Each donor brain regions systematically sampled trought 58692 probes with the following parameters:
echo probe_id, probe_name, gene_id, gene_symbol, gene_name, entrez_id, chromosome
echo
echo The results is a matrix of microarray-based gene expression profiles.
echo
echo Now we are going to load these data (about 500 ng of RNA per sample) of gene expression profile, 
echo that contains information for over 58692 gene probes

python -u download_data.py \
          --path_data=${PATH_RAW_DATA}
          
for donor in ${DONORS_LIST[@]}
do
    python -u allen_data.py \
              --path_data=${PATH_RAW_DATA} \
              --donor=${donor}\
              --path_save_data=${PATH_MATRIX_DATA}
#    python -u allen_data_gaming.py \
#              --path_data=${PATH_MATRIX_DATA} \
#              --donor=${donor}
done

