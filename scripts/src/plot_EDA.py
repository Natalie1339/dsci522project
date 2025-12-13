import matplotlib.pyplot as plt
import altair_ally as aly
import pandas as pd
import os

def EDA_helper(input_x_train_path, input_train_path, output_feature_dist_img_path): 
    X_train=pd.read_csv(input_x_train_path)
    train_df=pd.read_csv(input_train_path)
    correlation=aly.corr(train_df)
    correlation.save(os.path.join(output_feature_dist_img_path, 'correlation_plot.png'))
    images=[correlation]
    for feat in X_train.columns.tolist():
        plt.figure()
        plt.hist(X_train[feat], bins = 20, edgecolor='black')
        plt.xlabel(feat)
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {feat}')
        images.append(plt)
        plt.savefig(os.path.join(output_feature_dist_img_path, f"feature_{feat}_dist.png"))	

    return images