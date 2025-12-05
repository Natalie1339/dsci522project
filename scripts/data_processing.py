import click
import os
import pickle
import numpy as np
import pandas as pd
import pointblank as pb

from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import FeatureLabelCorrelation

from sklearn import set_config
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV

@click.command()
@click.option('--raw-data', type=str)
@click.option('--data-to', type=str)
@click.option('--preprocessor-to')
@click.option('--seed', type=int, default=123)

def main(raw_data, data_to, preprocessor_to, seed):
    np.random.seed(seed)
    set_config(transform_output="pandas")

    expected_cols = ['fixed_acidity',
                     'volatile_acidity',
                     'citric_acid',
                     'residual_sugar',
                     'chlorides',
                     'free_sulfur_dioxide',
                     'total_sulfur_dioxide',
                     'density',
                     'pH',
                     'sulphates',
                     'alcohol',
                     'quality']
  
    origin_df = pd.read_csv(raw_data, sep=',', encoding='utf-8')

    schema = pb.Schema(columns=[('fixed_acidity', 'float64'),
                                ('volatile_acidity', 'float64'),
                                ('citric_acid', 'float64'),
                                ('residual_sugar', 'float64'),
                                ('chlorides', 'float64'),
                                ('free_sulfur_dioxide', 'float64'),
                                ('total_sulfur_dioxide', 'float64'),
                                ('density', 'float64'),
                                ('pH', 'float64'),
                                ('sulphates', 'float64'),
                                ('alcohol', 'float64'),
                                ('quality', 'int64')])

    (pb.Validate(origin_df)
     .col_exists(columns=expected_cols)
     .col_vals_not_null(columns=expected_cols, thresholds=0.0)
     .col_schema_match(schema=schema)
     .rows_distinct()
     .interrogate())

    wine_quality_ds = Dataset(origin_df, label="quality", cat_features=[])

    check_feat_lab_corr = FeatureLabelCorrelation().add_condition_feature_pps_less_than(0.9)
    check_feat_lab_corr_result = check_feat_lab_corr.run(dataset=wine_quality_ds)

    if not check_feat_lab_corr_result.passed_conditions():
        raise ValueError("Feature-Label correlation exceeds the maximum acceptable threshold.")

    pb.Validate(origin_df).col_vals_between(columns="quality", left=0, right=10).interrogate()

    # split the dataset into train and test sets
    train_df, test_df = train_test_split(
        origin_df,
        test_size=0.25,
        random_state=seed,
        stratify=origin_df["quality"]
    )

    train_df.to_csv(os.path.join(data_to, "train_df.csv"), index=False)
    test_df.to_csv(os.path.join(data_to, "test_df.csv"), index=False)

    # separate the features and target
    X_train = train_df.drop(columns="quality")
    y_train = train_df["quality"]
    X_test = test_df.drop(columns="quality")
    y_test = test_df["quality"]

    X_train.to_csv(os.path.join(data_to, "X_train.csv"), index=False)
    y_train.to_csv(os.path.join(data_to, "y_train.csv"), index=False)
    X_test.to_csv(os.path.join(data_to, "X_test.csv"), index=False)
    y_test.to_csv(os.path.join(data_to, "y_test.csv"), index=False)

    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("regressor", RidgeCV())
        ]
    )

    pickle.dump(model, open(os.path.join(preprocessor_to, "model.pickle"), "wb"))

if __name__ == '__main__':
    main()
