import click
import matplotlib.pyplot as plt
import altair_ally as aly
import pandas as pd
import os

@click.command()
@click.option('--input-x-train-path', default='data/processed/X_train.csv', help='Path to X_train CSV file')
@click.option('--output-feature-dist-img-path', default='results/figures', help='Directory to save distribution plots')
# plotting a bar graph for each variable
def EDA(input_x_train_path, output_feature_dist_img_path):
    X_train=pd.read_csv(input_x_train_path)
    for feat in X_train.columns.tolist()[1:-1]:
        plt.figure()
        plt.hist(X_train[feat], bins = 20, edgecolor='black')
        plt.xlabel(feat)
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {feat}')
        plt.savefig(os.path.join(output_feature_dist_img_path, f"feature_{feat}_dist.png"))

if __name__ == '__main__':
    EDA()