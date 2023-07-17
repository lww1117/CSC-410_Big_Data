#~/usr/bin/env python
"""
The main script for running experiments
"""
from data import get_dataset


def main():
    dataset_directory = 'data'
    dataset = 'spam' #volcanoes #voting
    schema, X, y = get_dataset(dataset, dataset_directory)
    
    pass #add your code here
    
if __name__ == "__main__":
    main()
