import pandas as pd
REQUIRED={"date","country","revenue","purchases","total_views","stream_ids","stream_count"}
def load_data(path="data/business_timeseries.csv"):
    df=pd.read_csv(path,parse_dates=["date"])
    missing=REQUIRED-set(df.columns)
    if missing: raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df.empty: raise ValueError("Input dataset is empty.")
    return df.sort_values(["country","date"]).reset_index(drop=True)
