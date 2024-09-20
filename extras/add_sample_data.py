from customer_order_app import db, create_app
from customer_order_app.models import Customer, Order
from datetime import datetime

app = create_app()

with app.app_context():
    # Create sample customers
    customer1 = Customer(name="John Doe", code="JD001", phone_number="+254707203985")
    customer2 = Customer(name="Jane Smith", code="JS002")

    db.session.add(customer1)
    db.session.add(customer2)
    db.session.commit()

    # Create sample orders
    order1 = Order(customer_id=customer1.id, item="Laptop", amount=1200.50, time=datetime.utcnow())
    order2 = Order(customer_id=customer2.id, item="Smartphone", amount=799.99, time=datetime.utcnow())

    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

    print("Sample data added to the database.")
