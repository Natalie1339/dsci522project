import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

def save_white_wine_data(write_to):
    """
    Fetch the UCI wine dataset, filter white wines, and save to CSV.

    Returns the full path of the written file.

    Parameters
    ----------
    write_to : str
        Directory to save white wine data to
    
    Returns
    -------
    output_path : str
        Full path of csv file that gets saved

    Examples
    --------
    >>> save_white_wine_data("/data/raw")
            - will save winequality-white.csv to data directory
    """
    wine_quality = fetch_ucirepo(id=186)

    wine_df = wine_quality.data.original
    white_wine_df = wine_df[wine_df["color"] == "white"]

    os.makedirs(write_to, exist_ok=True)

    output_path = os.path.join(write_to, "winequality-white.csv")
    white_wine_df.to_csv(output_path, index=False)

    return output_path