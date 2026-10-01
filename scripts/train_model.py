from src.data_ingestion import load_data
from src.features import make_features,FEATURES
from src.model import train
r,b=train(make_features(load_data()),FEATURES)
print(r); print("Selected:",b)
