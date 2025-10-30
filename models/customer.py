from db.database import db
from dataclasses import dataclass

# a type to represent the customer data
@dataclass
class CustomerType:
    id: int
    username: str
    email: str
    phone: str

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone
