from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base


class CustomerModel(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    address = Column(String)
    purchases = relationship("PurchaseModel", back_populates="customer", cascade="all, delete-orphan")
