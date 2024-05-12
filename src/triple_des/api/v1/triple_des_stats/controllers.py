from typing import List
from loguru import logger
from fastapi import HTTPException, status
from .models import StepsDesCrypt
from ....external.cryptography import des
from ....external.cryptography.exceptions import TextError, KeyError

exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="check your text or key"
)


def encrypt_triple_des_eee(
    text: str, key1: str, key2: str, key3: str
) -> List[StepsDesCrypt]:
    try:
        logger.info("Start encrypting with key1")
        steps_e1 = des.encrypt(text, key1)
        logger.info("Start encrypting with key2")
        steps_e2 = des.encrypt(steps_e1.get("result"), key2)
        logger.info("Start encrypting with key3")
        steps_e3 = des.encrypt(steps_e2.get("result"), key3)
        logger.info("End encrypting")
        return [
            StepsDesCrypt(**steps_e1),
            StepsDesCrypt(**steps_e2),
            StepsDesCrypt(**steps_e3),
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
        steps_d1 = des.decrypt(text, key3)
        logger.info("Start decrypting with key2")
        steps_d2 = des.decrypt(steps_d1.get("result"), key2)
        logger.info("Start decrypting with key1")
        steps_d3 = des.decrypt(steps_d2.get("result"), key1)
        logger.info("End encrypting")
        return [
            StepsDesCrypt(**steps_d1),
            StepsDesCrypt(**steps_d2),
            StepsDesCrypt(**steps_d3),
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
        steps_e1 = des.encrypt(text, key1)
        logger.info("Start decrypting with key2")
        steps_e2 = des.decrypt(steps_e1.get("result"), key2)
        logger.info("Start encrypting with key3")
        steps_e3 = des.encrypt(steps_e2.get("result"), key3)
        logger.info("End encrypting")
        return [
            StepsDesCrypt(**steps_e1),
            StepsDesCrypt(**steps_e2),
            StepsDesCrypt(**steps_e3),
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
        steps_d1 = des.decrypt(text, key3)
        logger.info("Start encrypting with key2")
        steps_d2 = des.encrypt(steps_d1.get("result"), key2)
        logger.info("Start decrypting with key1")
        steps_d3 = des.decrypt(steps_d2.get("result"), key1)
        logger.info("End encrypting")
        return [
            StepsDesCrypt(**steps_d1),
            StepsDesCrypt(**steps_d2),
            StepsDesCrypt(**steps_d3),
        ]
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception
