import pandas
import click
from ucimlrepo import fetch_ucirepo 

@click.command()
@click.option('--path', type=str)
def main(path):
    wine_quality = fetch_ucirepo(id=186) 

    wine_df = wine_quality.data.original
    white_wine_df = wine_df[wine_df['color'] == 'white']

    white_wine_df.to_csv(path)

if __name__ == '__main__':
    main()