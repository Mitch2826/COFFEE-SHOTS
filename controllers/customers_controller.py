from models.customer import Customer, CustomerType
from db.database import db


def create_customer(username: str, email: str, phone: str) -> CustomerType:
    new_customer = Customer(username=username, email=email, phone=phone)
    db.session.add(new_customer)  # INSERT INTO customers (username, email, phone) VALUES (...)
    db.session.commit()
    return CustomerType(id=new_customer.id, username=new_customer.username, email=new_customer.email,
                        phone=new_customer.phone)


def get_customer_by_id(customer_id: int) -> CustomerType | None:
    customer = Customer.query.get(customer_id)  # SELECT * FROM customers WHERE id = customer_id
    if customer:
        return CustomerType(id=customer.id, username=customer.username, email=customer.email, phone=customer.phone)
    return None


def get_all_customers() -> list[CustomerType]:
    customers = Customer.query.all()  # SELECT * FROM customers
    return [CustomerType(id=c.id, username=c.username, email=c.email, phone=c.phone) for c in customers]


def delete_customer(customer_id: int) -> bool:
    customer = Customer.query.get(customer_id)
    if customer:
        db.session.delete(customer)  # DELETE FROM customers WHERE id = customer_id
        db.session.commit()
        return True
    return False


def update_customer(customer_id: int, username: str | None = None, email: str | None = None,
                    phone: str | None = None) -> CustomerType | None:
    customer = Customer.query.get(customer_id)
    if customer:
        if username:
            customer.username = username
        if email:
            customer.email = email
        if phone:
            customer.phone = phone
        db.session.commit()  # UPDATE customers SET ... WHERE id = customer_id
        return CustomerType(id=customer.id, username=customer.username, email=customer.email, phone=customer.phone)
    return None
