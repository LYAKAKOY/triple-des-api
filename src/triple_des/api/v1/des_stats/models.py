from pydantic import BaseModel, StringConstraints, field_validator
from typing import Annotated, Dict
from fastapi import HTTPException, status


class CryptInput(BaseModel):
    text: str
    key: Annotated[str, StringConstraints(max_length=16, min_length=16)]

    model_config = {
        "json_schema_extra": {
            "examples": [{"text": "Hi, my friend", "key": "3176F67A0DF673B4"}]
        }
    }

    @field_validator("key")
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
    block: str
    data_being: str
    after_initial_permutation: str
    info_rounds: Dict[int, Dict[str, str | int]]
    result: str

    def __init__(self, **kwargs):
        kwargs["info_rounds"] = {i: kwargs.pop(str(i)) for i in range(15)}
        super().__init__(**kwargs)


class ResultDesShow(BaseModel):
    binary_text: str
    steps: list[StepsDesCrypt]
    result: str
