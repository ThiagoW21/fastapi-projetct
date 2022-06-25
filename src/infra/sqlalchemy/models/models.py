from sqlalchemy import Column, Integer, String, Float
from src.infra.sqlalchemy.config.data_base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class Colaborattor(Base):
    __tablename__ = 'contribuitors'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    gender = Column(String)
    tel = Column(String)
    email = Column(String)
    office = Column(String)
    cep = Column(Integer)
    city = Column(String)
    state = Column(String)
    public_place = Column(String)
    number = Column(Integer)
    complement = Column(String)
    district = Column(String)
    data_nasc = Column(String)
    reference_point = Column(String)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    title = Column(String)
    category = Column(String)
    url_image = Column(String)
    brand = Column(String)
    model = Column(String)
    description = Column(String)
    borrowed_to = Column(String)
    price = Column(Float)
