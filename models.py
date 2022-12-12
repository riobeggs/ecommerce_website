from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    phone_number = Column(String(16))
    email_address = Column(String(64))
    # shipping_id = Column(Integer, ForeignKey(Address.id))

    # shipping = relationship("Address", foreign_key = )
    # billing = None
    # cart = None


class Address(Base):
    __tablename___ = "address"

    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    suburb = Column(String(64), nullable=True)
    city = Column(String(64))
    postal_code = Column(String(64))
    country = Column(String(64))

# # class Order(Base):
# #     __tablename__ = "order"

# #     id = Column(Integer, primary_key=True)
# #     items = Column(ARRAY)
# #     total = Column(Integer)

# #     address_id = None
# #     billing_id = None
