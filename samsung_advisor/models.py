from sqlalchemy import Column, Integer, String
from database import Base

class Phone(Base):
    __tablename__ = "samsung_phones"
    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String)
    display = Column(String)
    camera = Column(String)
    ram = Column(String)
    storage = Column(String)
    battery = Column(String)
    price = Column(String)
    
    