from src.app import app
def test_health():
    app.config["TESTING"]=True
    with app.test_client() as c: assert c.get("/health").status_code==200
