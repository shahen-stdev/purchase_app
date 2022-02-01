from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.utils import utils
from api.db import get_db
from api.schemas.purchase_schemas import PurchaseSchema, PurchaseUpdateSchema, PurchaseResponseSchema

purchase_router = APIRouter()


@purchase_router.get('', response_model=List[PurchaseResponseSchema])
def get_purchases_view(customer_id: int, db: Session = Depends(get_db)):
    return utils.get_customer_purchases(db, customer_id)


@purchase_router.post('', response_model=List[PurchaseResponseSchema])
def add_view(customer_id: int, data: PurchaseSchema, db: Session = Depends(get_db)):
    utils.add_purchase(customer_id, data, db)
    return utils.get_customer_purchases(db, customer_id)


@purchase_router.put('', response_model=List[PurchaseResponseSchema])
def update_view(customer_id: int, data: PurchaseUpdateSchema, db: Session = Depends(get_db)):
    utils.update_purchase(customer_id, db, new_data=data)
    return utils.get_customer_purchases(db, customer_id)


@purchase_router.delete('/{purchase_id:int}', response_model=List[PurchaseResponseSchema])
def delete_view(customer_id: int, purchase_id: int, db: Session = Depends(get_db)):
    utils.delete_purchase(customer_id, db, purchase_id)
    return utils.get_customer_purchases(db, customer_id)
