from loguru import logger
from fastapi import HTTPException, status
from .models import StepsDesCrypt, ResultDesShow
from ....external.cryptography import des
from ....external.cryptography.exceptions import TextError, KeyError

exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="check your text or key"
)


def encrypt_des(text: str, key: str) -> ResultDesShow:
    try:
        all_steps: list[StepsDesCrypt] = []
        blocks = des.text_to_binary_blocks(text)
        for block in blocks:
            steps = des.encrypt(block, key)
            all_steps.append(StepsDesCrypt(**steps))
        return ResultDesShow(
            binary_text="".join(blocks),
            steps=all_steps,
            result=des.binary_str_to_text("".join([step.result for step in all_steps])),
        )
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception


def decrypt_des(text: str, key: str) -> StepsDesCrypt:
    try:
        all_steps: list[StepsDesCrypt] = []
        blocks = des.text_to_binary_blocks(text)
        for block in blocks:
            steps = des.decrypt(block, key)
            all_steps.append(StepsDesCrypt(**steps))
        return ResultDesShow(
            binary_text="".join(blocks),
            steps=all_steps,
            result=des.binary_str_to_text(
                "".join([step.result for step in all_steps])
            ).strip("\u0000"),
        )
    except TextError as exc:
        logger.error(str(exc))
        raise exception
    except KeyError as exc:
        logger.error(str(exc))
        raise exception
