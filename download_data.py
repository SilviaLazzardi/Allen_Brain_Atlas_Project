#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib2 import Path
import sys
import zipfile


def load_dataset(path_data):
    donor_list=['178238387', '178238373', '178238359', '178238316', '178238266', '178236545']
    donor_name_list = ['9861', '10021', '12876', '14380', '15496', '15697']
    if sys.version_info[0] == 2:
        from urllib import urlretrieve
    else:
        from urllib.request import urlretrieve

    def download(file, filename , source='https://human.brain-map.org/api/v2/well_known_file_download/'):
        print("Downloading %s" % filename)
        urlretrieve(source + file, filename)
        print('Downloaded.')
    
    for i,donor in enumerate(donor_list):
        donor_name = donor_name_list[i]
        filename = Path(path_data)/'normalized_microarray_donor{}'.format(donor_name)
        if not Path(filename).exists():
            download(donor, str('{}.zip'.format(filename)))
            with zipfile.ZipFile(str('{}.zip'.format(filename)), 'r') as zip_ref:
                zip_ref.extractall(str(filename))
        else:
            print('{} already exists!'.format(filename))
    
    print('done!')
    

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_data')
    args = parser.parse_args()
   
    path_data = args.path_data
    load_dataset(path_data)

if __name__ == '__main__':
    main()
    