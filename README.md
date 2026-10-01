# AI Workflow Business Solution — Revenue Forecasting API

A self-contained capstone demonstrating an end-to-end AI workflow: data ingestion, EDA, time-series feature engineering, multiple-model comparison, Flask deployment, unit testing, monitoring and Docker.

## Business problem
Forecast monthly revenue using historical revenue, purchases, views, country and time features. The API supports a specific country or all countries combined.

## Dataset
`data/business_timeseries.csv` is **synthetic data generated for this capstone** because no original course dataset was available. It is intended to demonstrate the engineering workflow, not real business performance.

## Run locally
```bash
pip install -r requirements.txt
python scripts/run_eda.py
python scripts/train_model.py
python run_tests.py
python -m src.app
```

API:
- `/health`
- `/predict?country=India`
- `/predict` (all countries)

## Docker
```bash
docker build -t revenue-forecast-api .
docker run -p 5000:5000 revenue-forecast-api
```

## Models compared
Linear Regression, Random Forest and Gradient Boosting. A chronological holdout is used because this is time-series data. The lowest-RMSE model is selected.

## Testing
`python run_tests.py` runs the complete test suite. Tests cover ingestion, models, API and logging. Test logging uses temporary paths rather than production logs.

## Monitoring
API predictions are logged to `logs/predictions.jsonl`. `monitor_performance()` supports threshold-based monitoring and writes a machine-readable report.

## EDA
The EDA script generates `artifacts/revenue_trend.png` and `artifacts/revenue_by_country.png`.
