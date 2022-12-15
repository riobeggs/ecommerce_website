import models
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from address import Address

engine = create_engine("sqlite:///test.sqlite", echo=True, future=True)

models.Base.metadata.create_all(bind=engine)


class Person:
    def create_person(self) -> None:
        """
        Add a user to the Person table.
        """
        with Session(engine) as session:

            user = models.Person(
                first_name="Rio Beggs",
                last_name="Beggs",
                phone_number="0226940256",
                email_address="riobeggs1@gmail.com",
                shipping_id=Address().create_address(),
                billing_id=Address().create_address(),
                shopping_cart_id=None,
            )

            session.add(user)
            session.commit()


def main() -> None:
    p = Person()
    p.create_person()


if __name__ == "__main__":
    main()
