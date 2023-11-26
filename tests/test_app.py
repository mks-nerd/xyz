from . import client


def test_root() -> None:
    rsp = client.get("/")
    assert rsp.status_code == 200
    # assert rsp.json() == {"environment": "dev", "testing": False}
