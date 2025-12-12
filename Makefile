# Wine Quality Predictor - Makefile
# 
# This Makefile automates the data analysis pipeline for predicting wine quality.
#
# Usage:
#   make all     - Build the complete analysis pipeline (incremental)
#   make scratch - Clean all outputs and rebuild everything from scratch
#   make clean   - Remove all generated files and outputs

.PHONY: all clean scratch

# Builds the final report with all dependencies
all: report/wine_quality_predictor_report.html

# create results folder
results:
	mkdir -p results


# Loading, processing, and splitting data
data/raw/winequality-white.csv: scripts/data_download.py | results
	mkdir -p data/raw
	python scripts/data_download.py --write-to=data/raw

data/processed/X_train.csv data/processed/train_df.csv: scripts/data_processing.py data/raw/winequality-white.csv
	mkdir -p data/processed
	python scripts/data_processing.py --raw-data=data/raw/ --data-to=data/processed/


# Generating figures, tables, and models
results/figures/: scripts/EDA.py data/processed/X_train.csv data/processed/train_df.csv | results
	mkdir -p results/figures/
	python scripts/EDA.py --input-x-train-path=data/processed/X_train.csv --input-train-path=data/processed/train_df.csv --output-feature-dist-img-path=results/figures/

results/tables/ results/models/: scripts/modeling.py data/processed/train_df.csv data/processed/test_df.csv
	mkdir -p results/tables/
	mkdir -p results/models/
	python scripts/modeling.py --model-to=results/models/ --data-from=data/processed/ --figures-to=results/figures/ --tables-to=results/tables/


# Rendering final report to html
report/wine_quality_predictor_report.html: report/wine_quality_predictor_report.qmd results/figures/ results/tables/
	quarto render report/wine_quality_predictor_report.qmd --to html

# Remove all previously generated outputs
clean:
	rm -rf data/raw
	rm -rf data/processed
	rm -rf results/
	rm -f report/wine_quality_predictor_report.html


# Remove and regenerate all outputs
scratch:
	make clean
	make all
