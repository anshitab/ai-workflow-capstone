from src.data_ingestion import load_data
def test_ingestion():
    d=load_data(); assert len(d)>0; assert {"country","revenue","purchases"}.issubset(d.columns)
