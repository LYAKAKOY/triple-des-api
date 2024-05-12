import pytest
from fastapi.testclient import TestClient

from src.triple_des.create_app import create_app

block = "1011001110110011011100101011101100000001011001101000111101100101"
key = "3176F67A0DF673B4"

key1 = "5CD037E0B49EAD24"
key2 = "D98AC7FE6253BFA1"
key3 = "598AC7FE6253BFA2"


@pytest.fixture(scope="session")
def client():
    app = create_app()
    with TestClient(app) as c:
        yield c
