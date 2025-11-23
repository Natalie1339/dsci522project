# Wine Quality Predictor

- authors: Zhihao Xie, Natalie Trusdell, Oswin Gan, Sam Lokanc

## About

In this report we attempt to build a linear regression model using ridge regression to predict the quality of a given wine based purely on its physicochemical properties. Our model demonstrated a root mean squared error ($RSME$) of 0.734, meaning that on average the predicted quality was 0.734 points off of the actual quality. The $R^2$ score of our model was 0.3, meaning it explained only 30% of the variance. Though interpretation of the coefficients of our linear model we were able to identify which features had the strongest positive effect on quality (residual sugar and alcohol content), as well as those with the strongest negative effect (density, volatile acidity).

The dataset used in this project cotains various physicochemical (pH, citric acid content, alcohol content, etc.) and sensory data (0 - 10 score) related to vinho verde white wines from the Minho region of Portugal. It was created by Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis (1). It was sourced from the UCI Machine Learning Repository (2) and can be found [here](https://archive.ics.uci.edu/dataset/186/wine+quality).

## Report

The final report can be found [here](https://github.com/Natalie1339/dsci522project/blob/28d13c128f5a5cee79e09125874c630ad695cbee/analysis/white_wine_quality.pdf).

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
- Python and packages listed in [`environment.yaml`](https://github.com/Natalie1339/dsci522project/blob/28d13c128f5a5cee79e09125874c630ad695cbee/environment.yml)

## License

If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See [the license file](https://github.com/Natalie1339/dsci522project/blob/28d13c128f5a5cee79e09125874c630ad695cbee/LICENSE) for more information.

## References

1. Cortez P, Cerdeira A, Almeida F, Matos T, Reis J. Modeling wine preferences by data mining from physicochemical properties. Decis Support Syst. 2009 Nov;47(4):547–53. <https://doi.org/10.1016/j.dss.2009.05.016.>

2. Kelly M, Longjohn R, Nottingham K. The UCI Machine Learning Repository. <https://archive.ics.uci.edu>
