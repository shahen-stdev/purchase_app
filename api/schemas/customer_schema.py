from typing import List

from pydantic import BaseModel

from api.schemas.purchase_schemas import PurchaseSchema


class CustomerSchema(BaseModel):
    full_name: str
    address: str

    class Config:
        orm_mode = True


class CustomerResponseSchema(CustomerSchema):
    id: int
