FEATURES=["revenue_lag_1","revenue_lag_2","revenue_lag_3","revenue_lag_12","purchases","total_views","month","year","country_code"]
def make_features(df):
    x=df.copy().sort_values(["country","date"])
    x["month"]=x.date.dt.month; x["year"]=x.date.dt.year
    x["country_code"]=x.country.astype("category").cat.codes
    g=x.groupby("country").revenue
    for n in [1,2,3,12]: x[f"revenue_lag_{n}"]=g.shift(n)
    return x.dropna(subset=FEATURES+["revenue"]).copy()
