import click

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.plot_EDA import EDA_helper

@click.command()
@click.option('--input-x-train-path', default='data/processed/X_train.csv', help='Path to X_train CSV file')
@click.option('--input-train-path', default='data/processed/train_df.csv', help='Path to train_df CSV file')
@click.option('--output-feature-dist-img-path', default='results/figures', help='Directory to save distribution and correlation plots')

def EDA(input_x_train_path, input_train_path, output_feature_dist_img_path):
    """
    Plot a bar graph for each feature and show a correlation graph.

    Parameters:
    ----------
    input_x_train_path : string
        Path to a CSV file of training data, excluding target.
	input_train_path : string
        Path to a CSV file of training data, including target.
    output_feature_dist_img_path : str
        Directory to save distribution and correlation plots.

    Returns:
    -------
    A list of generated figures. 

    Examples:
    --------
    python scripts/EDA.py --input-x-train-path=data/processed/X_train.csv --input-train-path=data/processed/train_df.csv --output-feature-dist-img-path=results/figures/

    Notes:
    -----
    This function uses the pandas altair_ally and matplotlib.pyplot library to perform distribution and correlation
    of class observations in the input DataFrame.

    """

    EDA_helper(input_x_train_path, input_train_path, output_feature_dist_img_path)

if __name__ == '__main__':
    EDA()
