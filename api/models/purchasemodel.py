from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class PurchaseModel(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("CustomerModel", back_populates="purchases")
