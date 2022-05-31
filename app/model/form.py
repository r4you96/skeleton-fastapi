from pydantic import BaseModel


class Form(BaseModel):
    name: str = ""
    age: int = 1
