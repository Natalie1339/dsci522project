import os
from typing import Tuple


def split_and_save(train_df, test_df, target_col, output_dir) -> Tuple[str, str, str, str]:
    """
    Splits training and testing datasets into feature and target sets by a specified column,
    and exports each to the specified directory as CSV files.

    Parameters
    ----------
    train_df : pandas.DataFrame
        Training dataset containing feature columns and target column.
    test_df : pandas.DataFrame
        Testing dataset containing feature columns and target column.
    target_col : str
        Name of the column to split by.
    output_dir : str
        Path to the directory where the resulting CSV files are saved.

    Returns
    -------
    tuple (str)
        Tuple containing the file paths of the saved CSV files:
        (X_train_path, y_train_path, X_test_path, y_test_path)

    Raises
    ------
    ValueError
        Either the training or test dataset is empty.
    KeyError
        The specified target column is missing in either dataset.
    """
    if train_df.empty or test_df.empty:
        raise ValueError("Input DataFrames must be non-empty.")
    if target_col not in train_df.columns or target_col not in test_df.columns:
        raise KeyError(f"Target column '{target_col}' is missing in at least one of the DataFrames.")

    X_train = train_df.drop(columns=target_col)
    y_train = train_df[target_col]
    X_test = test_df.drop(columns=target_col)
    y_test = test_df[target_col]

    X_train_path = os.path.join(output_dir, "X_train.csv")
    y_train_path = os.path.join(output_dir, "y_train.csv")
    X_test_path = os.path.join(output_dir, "X_test.csv")
    y_test_path = os.path.join(output_dir, "y_test.csv")

    X_train.to_csv(X_train_path, index=False)
    y_train.to_csv(y_train_path, index=False)
    X_test.to_csv(X_test_path, index=False)
    y_test.to_csv(y_test_path, index=False)

    return X_train_path, y_train_path, X_test_path, y_test_path
