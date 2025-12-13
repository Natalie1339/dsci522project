import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pandas as pd
import pytest
from scripts.src.save_white_wine_data import save_white_wine_data


def test_save_white_wine_dataset(tmp_path):
    output_path = save_white_wine_data(write_to=tmp_path)

    assert os.path.exists(output_path), "Output CSV was not created"
    assert output_path.endswith("winequality-white.csv")

def test_only_white_wines_written(tmp_path):
    output_path = save_white_wine_data(tmp_path)
    df = pd.read_csv(output_path)

    assert set(df["color"]) == {"white"}
    assert len(df) == 4898

