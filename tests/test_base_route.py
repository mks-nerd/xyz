def test_root(test_app) -> None:
    rsp = test_app.get("/")
    assert rsp.status_code == 200
    assert rsp.json() == {"environment": "dev", "testing": True}


def test_get_info(test_app):
    rsp = test_app.get("/info")
    assert rsp.status_code == 200
    assert rsp.json() == {"data": []}


def test_add_info(test_app):
    rsp = test_app.post("/info", json={"info": "test"})
    assert rsp.status_code == 200
    rsp.json() == {"id": "8b7aa76e-3ecb-499b-92de-ca0433dca428"}
