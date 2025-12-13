import pandas
import os
import click
import os
from ucimlrepo import fetch_ucirepo 
from src.save_white_wine_data import save_white_wine_data

@click.command()
@click.option('--write-to', default='data/raw', help='Directory for data to be downloaded to')
def main(write_to):
    """
    Call save_white_wine_data function contained in src/
    The purpose of this is to download and filter for white wine data using the ucimlrepo python package
    
    Parameters:
    -----------

    write_to: the directory to write raw csv file to. defaults to data/raw.

    Examples:
    ---------
    >>> python scripts/data_download.py --write-to data/raw
    the above usage will download a file called winequality-white.csv to the data/raw directory.
    """
    save_white_wine_data(write_to)

if __name__ == '__main__':
    main()