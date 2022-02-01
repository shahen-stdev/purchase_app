from fastapi import HTTPException
from typing import List

from sqlalchemy.orm import Session

from api.models import PurchaseModel, CustomerModel
from api.schemas.purchase_schemas import PurchaseSchema, PurchaseUpdateSchema
from api.schemas.customer_schema import CustomerSchema

def validate_purchase_data(data):
    # Can add some validations here.
    if data.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity can't be bellow or equal to zero.")

def add_purchase(customer_id: int, data: PurchaseSchema, db: Session) -> PurchaseModel:
    # Validate if customer exists before craeting a purchase.
    get_customer(db, customer_id)
    validate_purchase_data(data)
    purchase = PurchaseModel(
        name=data.name,
        quantity=data.quantity,
        customer_id=customer_id
    )
    db.add(purchase)
    db.commit()
    db.refresh(purchase)
    return purchase


def update_purchase(customer_id: int, db: Session, new_data: PurchaseUpdateSchema) -> PurchaseModel:
    get_customer(db, customer_id)
    validate_purchase_data(new_data)
    purchase = db.query(PurchaseModel).filter(
        PurchaseModel.id == new_data.id,
        customer_id == customer_id
    ).first()
    if purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    purchase.name = new_data.name
    purchase.quantity = new_data.quantity
    db.commit()
    db.refresh(purchase)
    return purchase


def delete_purchase(customer_id: int, db: Session, id_: int) -> None:
    get_customer(db, customer_id)
    purchase = db.query(PurchaseModel).filter(PurchaseModel.id == id_, customer_id == customer_id).first()
    if purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    db.delete(purchase)
    db.commit()


def get_customer_purchases(db: Session, customer_id: int) -> List[PurchaseModel]:
    get_customer(db, customer_id)
    purchases = db.query(PurchaseModel).filter(PurchaseModel.customer_id == customer_id).all()
    return purchases


def add_customer(db: Session, user_data: CustomerSchema) -> CustomerSchema:
    customer = CustomerModel(full_name=user_data.full_name, address=user_data.address)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def get_customer(db: Session, id_: int) -> CustomerModel:
    customer = db.query(CustomerModel).get(id_)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


def get_all_customers(db: Session) -> List[CustomerModel]:
    return db.query(CustomerModel).all()