from typing import List
from loguru import logger
from fastapi import HTTPException, status
from .models import StepsDesCrypt, ResultDesShow
from ..des_stats.controllers import encrypt_des, decrypt_des
from ....external.cryptography import des
from ....external.cryptography.exceptions import TextError, KeyError

exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="check your text or key"
)


def encrypt_triple_des_eee(
    text: str, key1: str, key2: str, key3: str
) -> List[ResultDesShow]:
    try:
        logger.info("Start encrypting with key1")
        steps_e1 = encrypt_des(text, key1)
        logger.info("Start encrypting with key2")
        steps_e2 = encrypt_des(steps_e1.result, key2)
        logger.info("Start encrypting with key3")
        steps_e3 = encrypt_des(steps_e2.result, key3)
        logger.info("End encrypting")
        return [
            steps_e1,
            steps_e2,
            steps_e3,
        ]
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception


def decrypt_triple_des_eee(
    text: str, key1: str, key2: str, key3: str
) -> List[StepsDesCrypt]:
    try:
        logger.info("Start decrypting with key3")
        steps_d1 = decrypt_des(text, key3)
        logger.info("Start decrypting with key2")
        steps_d2 = decrypt_des(steps_d1.result, key2)
        logger.info("Start decrypting with key1")
        steps_d3 = decrypt_des(steps_d2.result, key1)
        logger.info("End decrypting")
        return [
            steps_d1,
            steps_d2,
            steps_d3,
        ]
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception


def encrypt_triple_des_ede(
    text: str, key1: str, key2: str, key3: str
) -> List[StepsDesCrypt]:
    try:
        logger.info("Start encrypting with key1")
        steps_e1 = encrypt_des(text, key1)
        logger.info("Start decrypting with key2")
        steps_e2 = decrypt_des(steps_e1.result, key2)
        logger.info("Start encrypting with key3")
        steps_e3 = encrypt_des(steps_e2.result, key3)
        logger.info("End encrypting")
        return [
            steps_e1,
            steps_e2,
            steps_e3,
        ]
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception


def decrypt_triple_des_ede(
    text: str, key1: str, key2: str, key3: str
) -> List[StepsDesCrypt]:
    try:
        logger.info("Start decrypting with key3")
        steps_d1 = decrypt_des(text, key3)
        logger.info("Start encrypting with key2")
        steps_d2 = encrypt_des(steps_d1.result, key2)
        logger.info("Start decrypting with key1")
        steps_d3 = decrypt_des(steps_d2.result, key1)
        logger.info("End encrypting")
        return [
            steps_d1,
            steps_d2,
            steps_d3,
        ]
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception
