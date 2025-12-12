import click
import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn import set_config
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeCV
from src.regression_metrics import regression_metrics


@click.command()
@click.option('--data-from', default="data/processed", help="Directory containing processed data")
@click.option('--figures-to', default="results/figures", help="Directory to output figures to")
@click.option('--tables-to', default="results/tables", help="Directory to output tables to")
@click.option('--model-to', default="results/models", help="Directory to output preprocessor to")

def main(data_from, figures_to, tables_to, model_to):
    set_config(transform_output="pandas")

    # read in the data
    train_df = pd.read_csv(os.path.join(data_from, "train_df.csv"))
    test_df = pd.read_csv(os.path.join(data_from, "test_df.csv"))
    X_train = pd.read_csv(os.path.join(data_from, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(data_from, "y_train.csv")).squeeze()
    X_test = pd.read_csv(os.path.join(data_from, "X_test.csv"))
    y_test = pd.read_csv(os.path.join(data_from, "y_test.csv")).squeeze()
    
    # OLS model
    predictor_cols = [col for col in train_df.columns if col != 'quality']
    formula = "quality ~ " + " + ".join(predictor_cols)
    model_ols = smf.ols(formula, data=train_df)
    results = model_ols.fit()
    with open(os.path.join(tables_to, "ols_summary.html"), "w") as f:
        f.write(results.summary().as_html())
 
    # Saving metrics to refer to in qmd   
    ols_r_square = results.rsquared
    ols_metrics = pd.DataFrame({
        'Metric': ['R²'],
        'Value': [ols_r_square]
    })
    ols_metrics.to_csv(os.path.join(tables_to, "ols_metrics.csv"), index=False)

    # create model with pipeline
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("regressor", RidgeCV())
        ]
    )  
    # fit the model
    model.fit(X_train, y_train)

    pickle.dump(model, open(os.path.join(model_to, "model.pickle"), "wb"))  
    # use the model to predict on the testing data
    y_pred = model.predict(X_test)
    
    # MILESTONE FUNCTION Calculate metrics
    summary = regression_metrics(y_test, y_pred)
    print(summary.to_string(index=False))
    # save ridge metrics
    summary.to_csv(os.path.join(tables_to, "ridge_metrics.csv"), index=False)

    # get coefficients for each feature
    linreg = model.named_steps["regressor"]
    coef_df = pd.DataFrame(
        {"feature": X_train.columns, "coefficient": linreg.coef_}
    ).sort_values("coefficient", ascending=False)
    coef_df['coefficient'] = coef_df['coefficient'].round(4)
    coef_df.to_csv(os.path.join(tables_to, "ridge_coefficients.csv"), index=False)

    # Actual versus Predicted Quality Scatter Plot
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred, alpha=0.4)
    plt.plot([y_test.min(), y_test.max()],
            [y_test.min(), y_test.max()],
            linewidth=2, color='red')
    plt.xlabel("Actual Quality")
    plt.ylabel("Predicted Quality")
    plt.title("Actual vs Predicted Quality")
    plt.savefig(os.path.join(figures_to, "Actual_vs_Predicted_scatter.png"))
    plt.close()

    # Residual Plot
    residuals = y_test - y_pred
    plt.figure(figsize=(7,5))
    plt.scatter(y_pred, residuals, alpha=0.4)
    plt.axhline(0, color="red", linestyle="--")
    plt.xlabel("Predicted Quality")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("Residual Plot")
    plt.savefig(os.path.join(figures_to, "Residual_plot.png"))
    plt.close()

    # Actual versus Predicted Quality boxplot
    df_viz = pd.DataFrame({
        "Actual Quality": y_test,
        "Predicted Quality": y_pred
    })
    plt.figure(figsize=(8,5))
    sns.boxplot(x="Actual Quality", y="Predicted Quality", data=df_viz)
    plt.title("Actual vs Predicted Quality")
    plt.savefig(os.path.join(figures_to, "Actual_vs_Predicted_boxplot.png"))
    plt.close()

if __name__ == '__main__':
    main()
