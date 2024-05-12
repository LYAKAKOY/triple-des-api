from ..conftest import block, key1, key2, key3


def test_encrypt_decrypt_using_triple_des_eee_endpoint(client):
    encrypt_data = {"block": block, "key1": key1, "key2": key2, "key3": key3}
    response = client.post("/api/triple_des_eee/encrypt", json=encrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    decrypt_data = {
        "block": resp_json[-1].get("result"),
        "key1": key1,
        "key2": key2,
        "key3": key3,
    }
    response = client.post("/api/triple_des_eee/decrypt", json=decrypt_data)
    resp_json = response.json()
    assert response.status_code == 200
    assert resp_json is not None
    assert block == resp_json[-1].get("result")
