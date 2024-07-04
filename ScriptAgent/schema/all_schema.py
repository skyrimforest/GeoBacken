from pydantic import BaseModel


class CommandInfo(BaseModel):
    command: str
    arguments: list
    pattern: str
    power: str