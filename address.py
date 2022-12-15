import models
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///test.sqlite", echo=True, future=True)

models.Base.metadata.create_all(bind=engine)


class Address:
    def create_address(self) -> int:
        """
        Add a users address to the Address table.

        Returns ID for users address.
        """
        with Session(engine) as session:

            user_address = models.Address(
                street="23B Arahia Street",
                suburb="Northcote",
                city="Auckland",
                postal_code="0627",
                country="New Zealand",
            )

            session.add(user_address)
            session.commit()

            return user_address.id
