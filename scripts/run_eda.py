from pathlib import Path
import matplotlib.pyplot as plt
from src.data_ingestion import load_data
Path("artifacts").mkdir(exist_ok=True); d=load_data()
g=d.groupby("date",as_index=False).revenue.sum()
plt.figure(figsize=(10,5)); plt.plot(g.date,g.revenue); plt.title("Monthly Revenue Trend"); plt.tight_layout(); plt.savefig("artifacts/revenue_trend.png"); plt.close()
g=d.groupby("country",as_index=False).revenue.sum()
plt.figure(figsize=(9,5)); plt.bar(g.country,g.revenue); plt.xticks(rotation=25); plt.title("Revenue by Country"); plt.tight_layout(); plt.savefig("artifacts/revenue_by_country.png"); plt.close()
