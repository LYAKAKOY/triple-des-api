from pydantic import BaseModel, ConfigDict, StringConstraints, field_validator
from typing import Annotated
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


class RoundInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    round: 1
    lefthalf: str
    righthalf: str
    subkey: str


class StepsDesCrypt(BaseModel):
    block: str
    data_being: str
    after_initial_permutation: str
    info_rounds: dict[int, RoundInfo]
    result: str

    def __init__(self, **kwargs):
        kwargs["info_rounds"] = {i: RoundInfo(**kwargs.pop(str(i))) for i in range(16)}
        super().__init__(**kwargs)


class ResultDesShow(BaseModel):
    binary_text: str
    steps: list[StepsDesCrypt]
    result: str
