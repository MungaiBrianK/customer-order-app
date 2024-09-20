from customer_order_app import db, create_app
from customer_order_app.models import Order, Customer  # Updated import

# Initialize the app context
app = create_app()

with app.app_context():
    # Check for records in the Order table
    orders = Order.query.all()
    if orders:
        print(f"Found {len(orders)} records in the 'order' table.")
        for order in orders:
            print(f"Order ID: {order.id}, Item: {order.item}, Amount: {order.amount}, Time: {order.time}")
    else:
        print("No records found in the 'order' table.")
    
    # Check for records in the Customer table
    customers = Customer.query.all()
    if customers:
        print(f"Found {len(customers)} records in the 'customer' table.")
        for customer in customers:
            print(f"Customer ID: {customer.id}, Name: {customer.name}, Code: {customer.code}")
    else:
        print("No records found in the 'customer' table.")
