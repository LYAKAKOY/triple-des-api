from ..conftest import text, key1, key2, key3


def test_encrypt_decrypt_using_triple_des_ede_endpoint(client):
    encrypt_data = {"text": text, "key1": key1, "key2": key2, "key3": key3}
    response = client.post("/api/triple_des_ede/encrypt", json=encrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    decrypt_data = {
        "text": resp_json[-1].get("result"),
        "key1": key1,
        "key2": key2,
        "key3": key3,
    }
    response = client.post("/api/triple_des_ede/decrypt", json=decrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    assert text == resp_json[-1].get("result")
