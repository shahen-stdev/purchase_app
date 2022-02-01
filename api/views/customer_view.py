from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.db import get_db
from api.utils import utils
from api.schemas.customer_schema import CustomerSchema, CustomerResponseSchema

customer_router = APIRouter()

@customer_router.get('', response_model=List[CustomerResponseSchema])
def customers_view( db: Session = Depends(get_db)):
    return utils.get_all_customers(db)


@customer_router.get('/{customer_id:int}', response_model=CustomerResponseSchema)
def get_customers_view(customer_id: int, db: Session = Depends(get_db)):
    return utils.get_customer(db, customer_id)


@customer_router.post('', response_model=CustomerResponseSchema)
def add_view(data: CustomerSchema, db: Session = Depends(get_db)):
    print(data)
    return utils.add_customer(db, data)
