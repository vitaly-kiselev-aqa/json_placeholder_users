from .strict_model import StrictModel


class Geo(StrictModel):
    lat: str
    lng: str


class Address(StrictModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(StrictModel):
    name: str
    catchPhrase: str
    bs: str


class User(StrictModel):
    """https://jsonplaceholder.typicode.com/users"""

    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company
