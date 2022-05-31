from typing import TypeVar, Generic, Optional

from pydantic.generics import GenericModel

T = TypeVar('T')


class ResponseModel(GenericModel, Generic[T]):
    result: Optional[T]


ok_response = ResponseModel(result='ok')
