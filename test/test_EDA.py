import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from scripts.src.plot_EDA import EDA_helper

def is_histogram(ax):
    """Check if axes contains a histogram"""
    
    if not ax.patches:
        return False
    
    patches = ax.patches
    
	# All patches should be rectangles
    if not all(isinstance(p, plt.Rectangle) for p in patches):
        return False
    return True

def check_correlation_plot(corr, X_train): 
    spec_str = str(corr.to_dict())

    for col in X_train.select_dtypes("number").columns:
        if col not in spec_str: 
            return False
    return True

def test_EDA(): 
	input_x_train_path='data/processed/X_train.csv'
	input_train_path='data/processed/train_df.csv'
	output_feature_dist_img_path='results/figures/'

	images=EDA_helper(input_x_train_path, input_train_path, output_feature_dist_img_path)

	X_train=pd.read_csv(input_x_train_path)
	assert check_correlation_plot(images[0], X_train)
	for image in images[1:]: 
		assert 'Distribution' in image.gca().get_title(), 'Distribution is not in the title. '
		assert image.gca().get_xlabel() in X_train.columns, f'{image.gca().get_xlabel()} is not in the data. '
		assert is_histogram(image.gca()), f'{image.gca().get_xlabel()} is not a histogram. '

if __name__ == "__main__":
    test_EDA()