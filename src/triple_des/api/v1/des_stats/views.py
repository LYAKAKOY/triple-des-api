from fastapi.routing import APIRouter
from .models import CryptInput, StepsDesCrypt
from .controllers import decrypt_des, encrypt_des

des_router = APIRouter(prefix="/api", tags=["des"])


@des_router.post(
    "/des/encrypt",
    response_model=StepsDesCrypt,
    summary="encrypt text by key using des",
)
def des_encrypt(body: CryptInput) -> StepsDesCrypt:
    return encrypt_des(text=body.block, key=body.key)


@des_router.post(
    "/des/decrypt",
    response_model=StepsDesCrypt,
    summary="decrypt text by key using des",
)
def des_decrypt(body: CryptInput) -> StepsDesCrypt:
    return decrypt_des(text=body.block, key=body.key)
