class Person:
    def __init__(self):
        self._id = None
        self._first_name = None
        self._last_name = None
        self._phone_number = None
        self._email_address = None
        self._shipping_id = None
        self._billing_id = None
        self._cart_id = None

    def UpdateBilling() -> None:
        """
        Person can create or update an existing
        billing address which will be stored in a dictionary.

        A unique ID will be created and assigned to
        persons billing address.
        """
        billing_address = {
            "first_name": None,
            "last_name": None,
            "address": None,
            "post_code": None,
            "city": None,
            "country": None,
            "phone_number": None,
        }
