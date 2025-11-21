# Wine Quality Predictor

- authors: Zhihao Xie, Natalie Trusdell, Oswin Gan, Sam Lokanc

## About

In this report we attempt to build a linear regression model using ridge regression to predict the quality of a given wine based purely on its physicochemical properties. ***comment more on actual model***

The dataset used in this project cotains various physicochemical (pH, citric acid content, alcohol content, etc.) and sensory data (0 - 10 score) related to vinho verde white wines from the Minho region of Portugal. It was created by Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis (1). It was sourced from the UCI Machine Learning Repository (2) and can be found [here](https://archive.ics.uci.edu/dataset/186/wine+quality).

## Report

The final report can be found [here](add link to html)

## Usage

First time running the project,
run the following from the root of this repository:

    ``` bash
    conda-lock install --name 
    wine-quality-predictor conda-lock.yml
    ```

To run the analysis,
run the following from the root of this repository:

    ``` bash
    jupyter lab 
    ```

Open `notebooks/white_wine_quality.ipynb` in Jupyter Lab and under Switch/Select Kernel choose "Python [conda env:wine-quality-predictor]".

Next, under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Dependencies

- `conda` (version 23.9.0 or higher)
- `conda-lock` (version 2.5.7 or higher)
- `jupyterlab` (version 4.0.0 or higher)
- `nb_conda_kernels` (version 2.3.1 or higher)
- Python and packages listed in [`environment.yml`](environment.yaml)

## License

If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See [the license file](LICENSE.md) for more information.

## References

1. Cortez P, Cerdeira A, Almeida F, Matos T, Reis J. Modeling wine preferences by data mining from physicochemical properties. Decis Support Syst. 2009 Nov;47(4):547–53. <https://doi.org/10.1016/j.dss.2009.05.016.>

2. Kelly M, Longjohn R, Nottingham K. The UCI Machine Learning Repository. <https://archive.ics.uci.edu>
