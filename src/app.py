from flask import Flask,request,jsonify
from pathlib import Path
import pandas as pd,joblib
from src.data_ingestion import load_data
from src.features import make_features
from src.monitoring import log_prediction
app=Flask(__name__)
MODEL=Path("models/revenue_model.joblib")
def predict(country=None):
    df=load_data()
    if country:
        df=df[df.country.str.lower()==country.lower()]
        if df.empty: raise ValueError("Unknown country.")
    x=make_features(df); bundle=joblib.load(MODEL)
    row=x.iloc[-1]
    p=float(bundle["model"].predict(pd.DataFrame([row[bundle["features"]].values],columns=bundle["features"]))[0])
    log_prediction({"country":country or "ALL","prediction":p}); return p
@app.get("/health")
def health(): return jsonify(status="ok")
@app.get("/predict")
def api_predict():
    try:
        c=request.args.get("country"); return jsonify(country=c or "ALL",predicted_revenue=round(predict(c),2))
    except Exception as e: return jsonify(error=str(e)),400
if __name__=="__main__": app.run(host="0.0.0.0",port=5000)
