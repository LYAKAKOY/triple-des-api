from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated, Dict
from fastapi import HTTPException, status


class CryptInput(BaseModel):
    block: Annotated[str, StringConstraints(max_length=64, min_length=64)]
    key1: Annotated[str, StringConstraints(max_length=16, min_length=16)]
    key2: Annotated[str, StringConstraints(max_length=16, min_length=16)]
    key3: Annotated[str, StringConstraints(max_length=16, min_length=16)]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "block": "1011001110110011011100101011101100000001011001101000111101100101",
                    "key1": "3176F67A0DF673B4",
                    "key2": "4176F67A0DF673B4",
                    "key3": "5176F67A0DF673B4",
                }
            ]
        }
    }

    @field_validator("block")
    def check_block(cls, value: str) -> str:
        if set(value) != {"0", "1"}:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="block must contains only 0 and 1",
            )
        return value

    @field_validator("key1", "key2", "key3")
    def check_keys(cls, value: str) -> str:
        try:
            int(value, 16)
            return value
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="key must be hex format",
            )


class StepsDesCrypt(BaseModel):
    data_being: str
    after_initial_permutation: str
    info_rounds: Dict[int, Dict[str, str | int]]
    result: str

    def __init__(self, **kwargs):
        kwargs["info_rounds"] = {i: kwargs.pop(str(i)) for i in range(15)}
        super().__init__(**kwargs)
