all: data/raw/winequality-white.csv data/processed/X_train.csv data/processed/train_df.csv results/figures/ results/tables/ results/models/ report/wine_quality_predictor_report.html

results:
	mkdir -p results

results/winequality-white.csv: scripts/data_download.py | results
	python scripts/data_download.py --write-to=results/

data/processed/X_train.csv data/processed/train_df.csv: scripts/data_processing.py data/raw/winequality-white.csv
	mkdir -p data/processed
	python scripts/data_processing.py --raw-data=data/raw/ --data-to=data/processed/

results/figures/: scripts/EDA.py data/processed/X_train.csv data/processed/train_df.csv | results
	mkdir -p results/figures/
	python scripts/EDA.py --input-x-train-path=data/processed/X_train.csv --input-train-path=data/processed/train_df.csv --output-feature-dist-img-path=results/figures/

results/tables/ results/models/: scripts/modeling.py data/processed/train_df.csv data/processed/test_df.csv
	mkdir -p results/tables/
	mkdir -p results/models/
	python scripts/modeling.py --model-to=results/models/ --data-from=data/processed/ --figures-to=results/figures/ --tables-to=results/tables/

report/wine_quality_predictor_report.html: report/wine_quality_predictor_report.qmd results/figures/ results/tables/
	quarto render report/wine_quality_predictor_report.qmd --to html

clean:
	rm -rf data/raw
	rm -rf data/processed
	rm -rf results/
	rm -f report/wine_quality_predictor_report.html

#.PHONY: all clean
