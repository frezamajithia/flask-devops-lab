from app import app, MOTIVATION_QUOTES


def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"DevOps" in res.data


def test_motivator_status_and_content():
    client = app.test_client()
    res = client.get("/motivator")
    assert res.status_code == 200

    text = res.data.decode()
    assert text in MOTIVATION_QUOTES
    assert "DevOps" in text
