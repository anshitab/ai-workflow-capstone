from src.model import models,evaluate
def test_multiple_models(): assert len(models())>=3
def test_metrics(): assert evaluate([1,2,3],[1,3,2])["mae"]>=0
