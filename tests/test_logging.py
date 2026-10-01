from src.monitoring import log_prediction
def test_logging_isolated(tmp_path):
    p=tmp_path/"test.jsonl"; log_prediction({"prediction":1},str(p)); assert p.exists()
