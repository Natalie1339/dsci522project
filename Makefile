all: results/winequality-white.csv results/X_train.csv results/figures/ results/tables/ report/wine_quality_predictor_report.html

results:
	mkdir -p results

results/winequality-white.csv: scripts/data_download.py | results
	python scripts/data_download.py

results/X_train.csv: scripts/data_processing.py results/winequality-white.csv
	python scripts/data_processing.py

results/figures/: scripts/EDA.py results/X_train.csv
	mkdir -p results/figures/
	python scripts/EDA.py

results/tables/: scripts/modeling.py
	mkdir -p results/tables/
	python scripts/modeling.py

report/wine_quality_predictor_report.html: report/wine_quality_predictor_report.qmd
	quarto render report/wine_quality_predictor_report.qmd --to html
