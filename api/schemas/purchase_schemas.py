from pydantic import BaseModel


class PurchaseSchema(BaseModel):
    name: str
    quantity: int

    class Config:
        orm_mode = True


class PurchaseResponseSchema(PurchaseSchema):
    id: int


class PurchaseUpdateSchema(PurchaseSchema):
    id: int