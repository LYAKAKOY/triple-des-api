from ..conftest import text, key


def test_encrypt_decrypt_using_des_endpoint(client):
    encrypt_data = {"text": text, "key": key}
    response = client.post("/api/des/encrypt", json=encrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    decrypt_data = {"text": resp_json.get("result"), "key": key}
    response = client.post("/api/des/decrypt", json=decrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    assert text == resp_json.get("result")
