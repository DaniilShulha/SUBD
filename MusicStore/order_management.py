from db_connection import DatabaseManager
from decorators import check_role


@check_role(['customer', 'manager', 'administrator'])
def place_order(db_manager, role_id, user_id, delivery_address, preffered_delivery_time, items):
    """Place a new order with multiple items.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        user_id: ID of the user placing the order
        delivery_address: Address for delivery
        preffered_delivery_time: Preferred delivery time
        items: List of tuples (item_id, quantity)
    """
    try:
        # Calculate total price
        total_price = 0
        for item_id, quantity in items:
            price_query = "SELECT price FROM item WHERE id = %s"
            price_result = db_manager.execute_query(price_query, (item_id,))
            if price_result:
                total_price += price_result[0][0] * quantity
            else:
                print(f"Item with ID {item_id} not found")
                return None

        # Insert order into customer_order
        order_query = """
        INSERT INTO customer_order (user_id, delivery_address, preffered_delivery_time, order_status_id, total_price)
        VALUES (%s, %s, %s, 1, %s) RETURNING id;
        """
        order_result = db_manager.execute_query(order_query, (user_id, delivery_address, preffered_delivery_time, total_price))
        if order_result:
            order_id = order_result[0][0]
            print(f"Order placed successfully with ID: {order_id}")
            
            # Insert items into order_item
            for item_id, quantity in items:
                item_query = """
                INSERT INTO order_item (customer_order_id, item_id, quantity)
                VALUES (%s, %s, %s);
                """
                db_manager.execute_query(item_query, (order_id, item_id, quantity))
            return order_id
        return None
    except Exception as e:
        print("Error placing order:", e)
        return None


@check_role(['customer', 'manager', 'administrator'])
def view_orders(db_manager, role_id, user_id=None):
    """View orders for a user or all orders if user_id is None.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        user_id: Optional ID of the user to view orders for
    """
    query = """
    SELECT co.id, u.user_name, co.delivery_address, co.order_time, os.status_name, co.total_price
    FROM customer_order co
    JOIN users u ON co.user_id = u.id
    JOIN order_status os ON co.order_status_id = os.id
    """
    if user_id:
        query += " WHERE co.user_id = %s"
        params = (user_id,)
    else:
        params = ()
    
    try:
        result = db_manager.execute_query(query, params)
        if result:
            print("\nList of orders:")
            for row in result:
                print(f"Order ID: {row[0]}, User: {row[1]}, Address: {row[2]}, Date: {row[3]}, Status: {row[4]}, Total: {row[5]}")
            return result
        else:
            print("No orders found")
            return []
    except Exception as e:
        print("Error viewing orders:", e)
        return None


@check_role(['manager', 'administrator'])
def change_order_status(db_manager, role_id, order_id, status_id):
    """Change the status of an order.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        order_id: ID of the order to change status
        status_id: New status ID
    """
    query = "UPDATE customer_order SET order_status_id = %s WHERE id = %s"
    try:
        rowcount = db_manager.execute_query(query, (status_id, order_id))
        if rowcount > 0:
            print(f"Order ID {order_id} status changed to {status_id}")
            return True
        else:
            print(f"Order with ID {order_id} not found")
            return False
    except Exception as e:
        print("Error changing order status:", e)
        return False


@check_role(['manager', 'administrator'])
def delete_order(db_manager, role_id, order_id):
    """Delete an order.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        order_id: ID of the order to delete
    """
    query = "DELETE FROM customer_order WHERE id = %s"
    try:
        rowcount = db_manager.execute_query(query, (order_id,))
        if rowcount > 0:
            print(f"Order with ID {order_id} deleted successfully")
            return True
        else:
            print(f"Order with ID {order_id} not found")
            return False
    except Exception as e:
        print("Error deleting order:", e)
        return False


@check_role(['customer', 'administrator'])
def return_order(db_manager, role_id, order_id):
    """Return an order.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        order_id: ID of the order to return
    """
    query = "UPDATE customer_order SET active = FALSE, time_canceled = NOW() WHERE id = %s AND active = TRUE"
    try:
        rowcount = db_manager.execute_query(query, (order_id,))
        if rowcount > 0:
            print(f"Order with ID {order_id} returned successfully")
            return True
        else:
            print(f"Order with ID {order_id} not found or already inactive")
            return False
    except Exception as e:
        print("Error returning order:", e)
        return False
