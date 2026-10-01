import json
from pathlib import Path
from datetime import datetime
def log_prediction(payload,path="logs/predictions.jsonl"):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with open(path,"a") as f: f.write(json.dumps({"timestamp":datetime.utcnow().isoformat()+"Z",**payload})+"\n")
def monitor_performance(metrics,threshold=1000,path="artifacts/performance_monitor.json"):
    report={"status":"PASS" if metrics["mae"]<=threshold else "REVIEW","threshold_mae":threshold,**metrics}
    Path(path).parent.mkdir(exist_ok=True)
    json.dump(report,open(path,"w"),indent=2); return report
