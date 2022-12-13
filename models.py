from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    phone_number = Column(String(16))
    email_address = Column(String(64))

    shipping_id = Column(Integer, ForeignKey("address.address_id"))
    billing_id = Column(
        Integer,
        ForeignKey("address.address_id"),
        nullable=True,
    )
    shopping_cart_id = Column(
        Integer,
        ForeignKey("shopping_cart.shopping_cart_id"),
        nullable=True,
    )


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True)
    street = Column(String(64))
    suburb = Column(String(64), nullable=True)
    city = Column(String(64))
    postal_code = Column(String(64))
    country = Column(String(64))


class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey("person.person_id"))
    shipping_id = Column(Integer, ForeignKey("address.address_id"))


class OrderItems(Base):
    __tablename__ = "order_items"

    order_items_id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    order_id = Column(Integer, ForeignKey("order.order_id"))
    item_id = Column(Integer, ForeignKey("item.item_id"))


class Item(Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True)
    title = Column(String(64))
    price = Column(Integer)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    stock = Column(Integer)

    item_id = Column(Integer, ForeignKey("item.item_id"))


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    shopping_cart_id = Column(Integer, primary_key=True)

    person_id = Column(Integer, ForeignKey("person.person_id"))


class ShoppingCartItems(Base):
    __tablename__ = "shopping_cart_items"

    shopping_cart_items_id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    shopping_cart_id = Column(
        Integer,
        ForeignKey("shopping_cart.shopping_cart_id"),
        nullable=True,
    )
    item_id = Column(Integer, ForeignKey("item.item_id"))
