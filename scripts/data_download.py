import pandas
import click
import os
from ucimlrepo import fetch_ucirepo 

@click.command()
@click.option('--write-to', type=str)
def main(write_to):
    wine_quality = fetch_ucirepo(id=186) 

    wine_df = wine_quality.data.original
    white_wine_df = wine_df[wine_df['color'] == 'white']

    white_wine_df.to_csv(os.path.join(write_to, "winequality-white.csv"))

if __name__ == '__main__':
    main()