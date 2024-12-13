from user_management import register_user, login_user, update_user_profile, delete_user_profile
from instrument_management import (
    view_all_instruments, add_instrument, update_instrument, delete_instrument,
    view_all_categories, add_category, update_category, delete_category
)
from order_management import (
    place_order, view_orders, change_order_status, delete_order, return_order
)
from db_connection import DatabaseManager
from payment_management import PaymentManager
from reviews_management import add_review, view_reviews, update_review, delete_review, view_user_reviews


def main_menu(db_manager):
    """Display the main menu for user interaction."""
    while True:
        print("\n=== Music Store Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            # Register a new user
            user_name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role_name = input("Enter role (customer/manager): ")
            country_name = input("Enter your country: ")
            register_user(db_manager, user_name, email, password, role_name, country_name)
        elif choice == '2':
            # Login existing user
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user_id, role_name = login_user(db_manager, email, password)
            if user_id:
                print(f"Access granted. You are logged in as a {role_name}.")
                if role_name == "customer":
                    customer_menu(db_manager, user_id)
                elif role_name == "manager":
                    manager_menu(db_manager, user_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


def customer_menu(db_manager, user_id):
    """Display the customer menu for available actions."""
    while True:
        print("\n=== Customer Menu ===")
        print("1. View Instruments")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Update Profile")
        print("5. Delete Profile")
        print("6. View My Reviews")  # New option
        print("7. Add Review")  # New option
        print("8. Update Review")  # New option
        print("9. Delete Review")  # New option
        print("10. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            view_all_instruments(db_manager, 1)
        elif choice == '2':
            instrument_id = int(input("Enter Instrument ID to order: "))
            quantity = int(input("Enter quantity: "))
            delivery_address = input("Enter delivery address: ")
            preferred_delivery_time = input("Enter preferred delivery time (YYYY-MM-DD HH:MM:SS): ")
            place_order(db_manager, 1, user_id, delivery_address, preferred_delivery_time, [(instrument_id, quantity)])
        elif choice == '3':
            view_orders(db_manager, 1, user_id)
        elif choice == '4':
            update_user_profile(db_manager, user_id)
        elif choice == '5':
            delete_user_profile(db_manager, user_id)
        elif choice == '6':
            view_user_reviews(db_manager, user_id)  # View user's reviews
        elif choice == '7':
            instrument_id = int(input("Enter Instrument ID to review: "))
            description = input("Enter your review: ")
            rating = int(input("Enter your rating (1-5): "))
            add_review(db_manager, user_id, instrument_id, description, rating)
        elif choice == '8':
            review_id = int(input("Enter Review ID to update: "))
            description = input("Enter new review description: ")
            rating = int(input("Enter new rating (1-5): "))
            update_review(db_manager, user_id, review_id, description, rating)
        elif choice == '9':
            review_id = int(input("Enter Review ID to delete: "))
            delete_review(db_manager, user_id, review_id)
        elif choice == '10':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


def manager_menu(db_manager, user_id):
    """Display the manager menu for available actions."""
    while True:
        print("\n=== Manager Menu ===")
        print("1. View Instruments")
        print("2. Add Instrument")
        print("3. Manage Orders")
        print("4. Update Instrument")
        print("5. Delete Instrument")
        print("6. View Categories")
        print("7. Add Category")
        print("8. Update Category")
        print("9. Delete Category")
        print("10. Process Payment")
        print("11. Add Payment")
        print("12. Update Payment Status")
        print("13. Refund Payment")
        print("14. View Reviews")  # New option
        print("15. Update Review")  # New option
        print("16. Delete Review")  # N
        print("17. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            view_all_instruments(db_manager, 2)
        elif choice == '2':
            instrument_name = input("Enter instrument name: ")
            category_id = int(input("Enter category ID: "))
            manufacturer_id = int(input("Enter manufacturer ID: "))
            description = input("Enter description: ")
            add_instrument(db_manager, 2, instrument_name, category_id, manufacturer_id, description)
        elif choice == '3':
            print("Viewing all orders:")
            view_orders(db_manager, 2)
            order_id = int(input("Enter Order ID to manage: "))
            new_status = int(input("Enter new status ID: "))
            change_order_status(db_manager, 2, order_id, new_status)
            delete_choice = input("Do you want to delete this order? (yes/no): ")
            if delete_choice.lower() == 'yes':
                delete_order(db_manager, 2, order_id)
        elif choice == '4':
            instrument_id = int(input("Enter Instrument ID to update: "))
            update_instrument(db_manager, 2, instrument_id)
        elif choice == '5':
            instrument_id = int(input("Enter Instrument ID to delete: "))
            delete_instrument(db_manager, 2, instrument_id)
        elif choice == '6':
            view_all_categories(db_manager, 2)
        elif choice == '7':
            category_name = input("Enter category name: ")
            add_category(db_manager, 2, category_name)
        elif choice == '8':
            category_id = int(input("Enter Category ID to update: "))
            new_category_name = input("Enter new category name: ")
            update_category(db_manager, 2, category_id, new_category_name)
        elif choice == '9':
            category_id = int(input("Enter Category ID to delete: "))
            delete_category(db_manager, 2, category_id)
        elif choice == '10':
            order_id = int(input("Enter Order ID to process payment: "))
            payment_method = input("Enter payment method: ")
            payment_manager = PaymentManager(db_manager)
            payment_manager.process_payment(order_id, payment_method)
        elif choice == '11':
            order_id = int(input("Enter Order ID for payment record: "))
            payment_method = input("Enter payment method: ")
            payment_manager = PaymentManager(db_manager)
            payment_manager.add_payment(order_id, payment_method)
        elif choice == '12':
            order_id = int(input("Enter Order ID to update payment status: "))
            new_status = input("Enter new payment status: ")
            payment_manager = PaymentManager(db_manager)
            payment_manager.update_payment_status(order_id, new_status)
        elif choice == '13':
            order_id = int(input("Enter Order ID to refund: "))
            payment_manager = PaymentManager(db_manager)
            payment_manager.refund_payment(order_id)
        elif choice == '14':
            instrument_id = int(input("Enter Instrument ID to view reviews: "))
            view_reviews(db_manager, instrument_id)  # View all reviews for the instrument
        elif choice == '15':
            review_id = int(input("Enter Review ID to update: "))
            description = input("Enter new review description: ")
            rating = int(input("Enter new rating (1-5): "))
            update_review(db_manager, user_id, review_id, description, rating)
        elif choice == '16':
            review_id = int(input("Enter Review ID to delete: "))
            delete_review(db_manager, user_id, review_id)
        elif choice == '17':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")




def main():
    """Main function to run the tests."""
    print("Starting Music Store Management System...")

    db_manager = DatabaseManager(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="znexie",
        password="123456"
    )

    try:
        # Display the main menu
        main_menu(db_manager)

    finally:
        db_manager.close()
        print("\nSystem shutdown.")


if __name__ == "__main__":
    main()