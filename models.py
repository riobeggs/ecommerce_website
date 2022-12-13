from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    phone_number = Column(String(16))
    email_address = Column(String(64))

    shipping_id = Column(Integer, ForeignKey("address.id"))
    billing_id = Column(Integer, ForeignKey("address.id"), nullable=True)


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    suburb = Column(String(64), nullable=True)
    city = Column(String(64))
    postal_code = Column(String(64))
    country = Column(String(64))


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    total = Column(Integer)

    person_id = Column(Integer, ForeignKey("person.id"))
    shipping_id = Column(Integer, ForeignKey("address.id"))


class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    quantity = Column(Integer)


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    price = Column(Integer)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    stock = Column(Integer)


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))


class ShoppingCartItems(Base):
    __tablename__ = "shopping_cart_items"

    id = Column(Integer, primary_key=True)
    shopping_cart_id = Column(Integer, ForeignKey("shopping_cart.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    quantity = Column(Integer)
