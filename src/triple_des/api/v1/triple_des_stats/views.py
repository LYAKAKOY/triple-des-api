from fastapi.routing import APIRouter
from typing import List
from .models import CryptInput, ResultDesShow
from .controllers import (
    decrypt_triple_des_eee,
    encrypt_triple_des_eee,
    encrypt_triple_des_ede,
    decrypt_triple_des_ede,
)

triple_des_router = APIRouter(prefix="/api", tags=["triple_des"])


@triple_des_router.post(
    "/triple_des_eee/encrypt",
    response_model=List[ResultDesShow],
    summary="encrypt text using triple des EEE",
)
def des_encrypt_eee(body: CryptInput) -> List[ResultDesShow]:
    return encrypt_triple_des_eee(
        text=body.text, key1=body.key1, key2=body.key2, key3=body.key3
    )


@triple_des_router.post(
    "/triple_des_eee/decrypt",
    response_model=List[ResultDesShow],
    summary="decrypt text using triple des EEE",
)
def des_decrypt_eee(body: CryptInput) -> List[ResultDesShow]:
    return decrypt_triple_des_eee(
        text=body.text, key1=body.key1, key2=body.key2, key3=body.key3
    )


@triple_des_router.post(
    "/triple_des_ede/encrypt",
    response_model=List[ResultDesShow],
)
def des_encrypt_ede(body: CryptInput) -> List[ResultDesShow]:
    return encrypt_triple_des_ede(
        text=body.text, key1=body.key1, key2=body.key2, key3=body.key3
    )


@triple_des_router.post(
    "/triple_des_ede/decrypt",
    response_model=List[ResultDesShow],
)
def des_decrypt_ede(body: CryptInput) -> List[ResultDesShow]:
    return decrypt_triple_des_ede(
        text=body.text, key1=body.key1, key2=body.key2, key3=body.key3
    )
