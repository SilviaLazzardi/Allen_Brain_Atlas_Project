#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:55:44 2019

@author: silvia
"""
from sklearn.cluster import KMeans
import numpy as np
from pathlib2 import Path
import matplotlib.pyplot as plt

def load_data(path_data, donor):
    return np.load(str(Path(path_data)/'data_matrix_donor_{}.npy'.format(donor)))


def kmeans(data):
    kmeans = KMeans(n_clusters=500, random_state=0).fit(data)
    labels = kmeans.labels_
    plt.plot(labels)
    plt.show()
    return labels

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_data')
    parser.add_argument('--donor')
    args = parser.parse_args()
    
    path_data = args.path_data
    donor = args.donor
    
    data = load_data(path_data, donor)
    kmeans(data)

if __name__ == '__main__':
    main()