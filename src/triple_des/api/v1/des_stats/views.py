from fastapi.routing import APIRouter
from .models import CryptInput, ResultDesShow
from .controllers import decrypt_des, encrypt_des

des_router = APIRouter(prefix="/api", tags=["des"])


@des_router.post(
    "/des/encrypt",
    response_model=ResultDesShow,
    summary="encrypt text by key using des",
)
def des_encrypt(body: CryptInput) -> ResultDesShow:
    return encrypt_des(text=body.text, key=body.key)


@des_router.post(
    "/des/decrypt",
    response_model=ResultDesShow,
    summary="decrypt text by key using des",
)
def des_decrypt(body: CryptInput) -> ResultDesShow:
    return decrypt_des(text=body.text, key=body.key)
