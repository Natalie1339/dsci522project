import pandas
import os
import click
import os
from ucimlrepo import fetch_ucirepo 
from src.save_white_wine_data import save_white_wine_data

@click.command()
@click.option('--write-to', default='data/raw', help='Directory for data to be downloaded to')
def main(write_to):
    save_white_wine_data(write_to)

if __name__ == '__main__':
    main()