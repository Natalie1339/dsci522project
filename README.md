# Wine Quality Predictor

- authors: Zhihao Xie, Natalie Trusdell, Oswin Gan, Sam Lokanc

## About

In this project, we ask if we can use a machine learning model to predict wine quality from various physiochemical attributes. Specifically the question we aim to address is: can linear modeling be useds to adequately predict wine quality based solely on physiochemical properties? Our goal is to create an interpretable linear regression model trained on wine data related to vinho verde white wines from the Minho region of Portugal which contains the physicochemical and sensory data of 4898 wines (1). The utility of such a model is two-fold as it can be used as a tool to help less experienced wine makers and sommeliers get a sense of the quality of a given wine. In this report we built a linear ridge regression model trained on variables such as citric acid, residual sugar, etc. to predict the quality rating (1-10) given to a particular white wine. While our model explained only about 30% of the variation in wine quality, we were able to identify which features had the strongest positive effect on quality (residual sugar and alcohol content), as well as those with the strongest negative effect (density, volatile acidity). Based on these results, we can conclude that the physiochemical and sensory data listed in the dataset are helpful with predicting the wine quality, but since preferences regarding wine quality is so subjective, additional input from actual sommeliers might always be needed.

## Report

The final report can be found [on our GitHub repository](https://github.com/Natalie1339/dsci522project/blob/main/report/wine_quality_predictor_report.html).

## Usage

1. Using the command line, navigate to the root of this project and enter the following command:
```docker compose up --build```
The terminal should output a url starting with `http://127.0.0.1:8888/lab?token=`. Open the URL in your browser.

2. Make sure you are in the root of the directory. `pwd` should return `/workplace`.

3. Run the Makefile by entering `make`. You can clear previous Makefile output using `make clean`.

4. To shut down the container, use `ctrl + c` in the terminal and enter `docker compose rm`.

## Dependencies

- `conda` (version 23.9.0 or higher)
- `conda-lock` (version 2.5.7 or higher)
- `jupyterlab` (version 4.0.0 or higher)
- `nb_conda_kernels` (version 2.3.1 or higher)
- Python and packages listed in [`environment.yml`](environment.yml)

## Scripts

The following scripts are used to carry out the entirety of the analysis and can be found in the scripts/src directory:

| Script | Utility |
| --- | --- |
| data_download.py | Downloads and filters for white wine data using the ucimlrepo python package. Saves as csv file to data/raw directory |
| data_processing.py | Performs data validation checks using pointblank python package. Creates train test splits of data and saves them to data/processed directory in csv format|
| EDA.py | Plots a bar graph for each feature and show a correlation graph. Saves each plot to results/figures directory |
| modeling.py | Creates and fits ridge regression model to the training data. Saves model to results/model directory. Reports performance metrics and coefficients and saves them in results/tables directory |

## License

If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See [the license file](LICENSE) for more information.

## References

1. Cortez P, Cerdeira A, Almeida F, Matos T, Reis J. Modeling wine preferences by data mining from physicochemical properties. Decis Support Syst. 2009 Nov;47(4):547–53. <https://doi.org/10.1016/j.dss.2009.05.016.>

2. Kelly M, Longjohn R, Nottingham K. The UCI Machine Learning Repository. <https://archive.ics.uci.edu>
