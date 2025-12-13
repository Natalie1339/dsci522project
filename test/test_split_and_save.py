import sys
import os
import pytest
from pathlib import Path
import pandas as pd

from scripts.src.split_and_save import split_and_save

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Create small toy dataset for testing
def _create_toy_data():
    train_df = pd.DataFrame(
        {"feat_a": [1, 2, 3],
         "feat_b": ["a", "b", "c"],
         "target": [0, 1, 0]}
    )
    test_df = pd.DataFrame(
        {"feat_a": [1, 3],
         "feat_b": ["c", "d"],
         "target": [1, 0]}
    )
    return train_df, test_df


def test_save_datasets(tmp_path):
    train_df, test_df = _create_toy_data()
    outdir = tmp_path/"out"
    outdir.mkdir(parents=True, exist_ok=True)

    X_train_path, y_train_path, X_test_path, y_test_path = split_and_save(
        train_df, test_df, target_col="target", output_dir=str(outdir)
    )

    # Check that paths exist
    assert os.path.exists(X_train_path)
    assert os.path.exists(y_train_path)
    assert os.path.exists(X_test_path)
    assert os.path.exists(y_test_path)

    # Check filenames
    assert Path(X_train_path).name == "X_train.csv"
    assert Path(y_train_path).name == "y_train.csv"
    assert Path(X_test_path).name == "X_test.csv"
    assert Path(y_test_path).name == "y_test.csv"

    # Check column splits correctly
    X_train = pd.read_csv(X_train_path)
    y_train = pd.read_csv(y_train_path)
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path)

    assert "target" not in X_train.columns
    assert "target" not in X_test.columns
    assert list(y_train.columns) == ["target"]
    assert list(y_test.columns) == ["target"]


def test_missing_target_raises_error(tmp_path):
    train_df, test_df = _create_toy_data()
    outdir = tmp_path/"out"
    outdir.mkdir(parents=True, exist_ok=True)

    # Drop target column from test dataset
    test_df = test_df.drop(columns="target")

    with pytest.raises(Exception):
        split_and_save(train_df, test_df, target_col="target", output_dir=str(outdir))


def test_non_df_input_raises_error(tmp_path):
    train_df, test_df = _create_toy_data()
    outdir = tmp_path/"out"
    outdir.mkdir(parents=True, exist_ok=True)

    with pytest.raises(Exception):
        split_and_save("not a df", test_df, target_col="target", output_dir=str(outdir))

    with pytest.raises(Exception):
        split_and_save(train_df, ["not", "a", "df"], target_col="target", output_dir=str(outdir))