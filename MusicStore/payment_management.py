from db_connection import DatabaseManager
from decorators import check_role


class PaymentManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def process_payment(self, order_id, payment_method):
        """Simulate payment processing for an order."""
        try:
            query = """
            UPDATE payment SET payment_status = 'completed', payment_method = %s
            WHERE customer_order_id = %s
            """
            self.db_manager.execute_query(query, (payment_method, order_id))
            print(f"Payment for Order ID {order_id} processed successfully.")
        except Exception as e:
            print("Error processing payment:", e)

    def update_payment_status(self, order_id, status):
        """Update the payment status for a given order."""
        try:
            query = "UPDATE payment SET payment_status = %s WHERE customer_order_id = %s"
            self.db_manager.execute_query(query, (status, order_id))
            print(f"Payment status for Order ID {order_id} updated to {status}.")
        except Exception as e:
            print("Error updating payment status:", e)

    def refund_payment(self, order_id):
        """Simulate a refund by setting the payment status to 'refunded'."""
        try:
            self.update_payment_status(order_id, 'refunded')
            print(f"Refund for Order ID {order_id} processed successfully.")
        except Exception as e:
            print("Error processing refund:", e)

    def add_payment(self, order_id, payment_method, payment_status='pending'):
        """Add a new payment entry for a given customer_order_id."""
        try:
            query = """
            INSERT INTO payment (customer_order_id, payment_method, payment_status)
            VALUES (%s, %s, %s)
            """
            self.db_manager.execute_query(query, (order_id, payment_method, payment_status))
            print(f"Payment record for Order ID {order_id} added successfully.")
        except Exception as e:
            print("Error adding payment record:", e)