from loguru import logger
from fastapi import HTTPException, status
from .models import StepsDesCrypt
from ....external.cryptography import des
from ....external.cryptography.exceptions import TextError, KeyError

exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="check your text or key"
)


def encrypt_des(text: str, key: str) -> StepsDesCrypt:
    try:
        steps = des.encrypt(text, key)
        return StepsDesCrypt(**steps)
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception


def decrypt_des(text: str, key: str) -> StepsDesCrypt:
    try:
        steps = des.decrypt(text, key)
        return StepsDesCrypt(**steps)
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception
