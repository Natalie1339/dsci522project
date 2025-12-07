all: results/winequality-white.csv results/X_train.csv results/figures/ results/tables/ report/wine_quality_predictor_report.html

results:
	mkdir -p results

results/winequality-white.csv: scripts/data_download.py | results
	python scripts/data_download.py --write-to=results/

results/X_train.csv: scripts/data_processing.py results/winequality-white.csv
	python scripts/data_processing.py --raw-data=results/winequality-white.csv --data-to=results/ --preprocessor-to=results/

results/figures/: scripts/EDA.py results/X_train.csv
	mkdir -p results/figures/
	python scripts/EDA.py --input-x-train-path=results/X_train.csv --output-feature-dist-img-path=results/figures/

results/tables/: scripts/modeling.py results/model.pickle results/train_df.csv results/test_df.csv
	mkdir -p results/tables/
	python scripts/modeling.py --model-from=results/ --data-from=results/ --figures-to=results/figures/ --tables-to=results/tables/

report/wine_quality_predictor_report.html: report/wine_quality_predictor_report.qmd
	quarto render report/wine_quality_predictor_report.qmd
