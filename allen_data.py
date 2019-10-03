#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:11:06 2019

@author: silvia
"""

import numpy as np
import pandas as pd

from pathlib2 import Path

# FUNCTIONS TO GET THE ALLEN BRAIN ATLAS DATA

###############################################################################



################################## LOAD DATA ##################################

def read_data_single_donor(path_data):
    data = pd.read_csv(path_data, sep=',', header=(0))
    return data

################################### GET DATA ##################################

def get_probes_data_single_donor(data):
    
    probe_id = data['probe_id']
    probe_name = data['probe_name']
    
    gene_id = data['gene_id']
    gene_symbol = data['gene_symbol']
    gene_name = data['gene_name']
    
    entrez_id = data['entrez_id']
    chromosome = data['chromosome']
    
    return probe_id, probe_name, gene_id, gene_symbol, gene_name, entrez_id, chromosome
    
################################## SAVE DATA ##################################

def save_data(path_save, matrix, matrix_name):
    path_matrix = Path(path_save)/'{}.npy'.format(matrix_name)
    if not path_matrix.exists():
        np.save(str(path_save/'{}.npy'.format(matrix_name)), matrix)
    else:
        print('This file already exists.')


#################################### MAIN #####################################

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_data')
    parser.add_argument('--donor')
    
    parser.add_argument('--path_save_data')
    args = parser.parse_args()

    # VARIABLES     
    path_data = args.path_data
    donor = int(args.donor)
    
    path_save_data= args.path_save_data
    path_probes_data_donor=Path(path_data)/'normalized_microarray_donor{}/Probes.csv'.format(donor)
    path_microarray_donor=Path(path_data)/'normalized_microarray_donor{}/MicroarrayExpression.csv'.format(donor)
    
    data_probes=read_data_single_donor(path_probes_data_donor) 
    probe_id, probe_name, gene_id, gene_symbol, gene_name, entrez_id, chromosome=get_probes_data_single_donor(data_probes)
    print('')
    print('Loading microarray data for Donor {}...'.format(donor))
    
    data_microarray=read_data_single_donor(path_microarray_donor)
    print('Number of probes, number of voxels')
    print(data_microarray.shape)
    print('Saving...')
    matrix_name='data_matrix_donor_{}.npy'.format(donor)
    save_data(Path(path_save_data), data_microarray, matrix_name)
    print('Done')    
        
if __name__ == '__main__':
    main()