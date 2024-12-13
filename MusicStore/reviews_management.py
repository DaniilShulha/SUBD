from db_connection import DatabaseManager

def add_review(db_manager, user_id, instrument_id, description, rating):
    """Add a new review for an instrument."""
    query = """
    INSERT INTO review (user_id, instrument_id, description, rating)
    VALUES (%s, %s, %s, %s);
    """
    try:
        db_manager.execute_query(query, (user_id, instrument_id, description, rating))
        print("Review added successfully.")
    except Exception as e:
        print("Error adding review:", e)


def view_reviews(db_manager, instrument_id):
    """View all reviews for a specific instrument."""
    query = """
    SELECT r.id, u.user_name, r.description, r.rating
    FROM review r
    JOIN users u ON r.user_id = u.id
    WHERE r.instrument_id = %s;
    """
    try:
        result = db_manager.fetch_all(query, (instrument_id,))
        if result:
            print(f"\nReviews for Instrument ID {instrument_id}")
            for row in result:
                print(f"Review ID: {row[0]}, User: {row[1]}, Rating: {row[3]}, Description: {row[2]}")
        else:
            print("No reviews found for this instrument.")
    except Exception as e:
        print("Error viewing reviews:", e)


def update_review(db_manager, user_id, review_id, description, rating):
    """Update an existing review if the user owns it or is a manager/admin."""
    ownership_query = "SELECT user_id FROM review WHERE id = %s;"
    try:
        owner_result = db_manager.fetch_one(ownership_query, (review_id,))

        if not owner_result:
            print("Review not found.")
            return

        review_owner_id = owner_result[0]

        if review_owner_id != user_id:
            role_query = "SELECT role_id FROM users WHERE id = %s;"
            role_result = db_manager.fetch_one(role_query, (user_id,))
            if not role_result or role_result[0] < 2:  # Assuming role_id 2 (manager), 3 (admin)
                print("You do not have permission to update this review.")
                return

        query = """
        UPDATE review
        SET description = %s, rating = %s
        WHERE id = %s;
        """
        db_manager.execute_query(query, (description, rating, review_id))
        print("Review updated successfully.")
    except Exception as e:
        print("Error updating review:", e)


def delete_review(db_manager, user_id, review_id):
    """Delete a review if the user owns it or is a manager/admin."""
    ownership_query = "SELECT user_id FROM review WHERE id = %s;"
    try:
        owner_result = db_manager.fetch_one(ownership_query, (review_id,))

        if not owner_result:
            print("Review not found.")
            return

        review_owner_id = owner_result[0]

        if review_owner_id != user_id:
            role_query = "SELECT role_id FROM users WHERE id = %s;"
            role_result = db_manager.fetch_one(role_query, (user_id,))
            if not role_result or role_result[0] < 2:  # Assuming role_id 2 (manager), 3 (admin)
                print("You do not have permission to delete this review.")
                return

        query = "DELETE FROM review WHERE id = %s;"
        db_manager.execute_query(query, (review_id,))
        print("Review deleted successfully.")
    except Exception as e:
        print("Error deleting review:", e)

def view_user_reviews(db_manager, user_id):
    """View all reviews created by a specific user."""
    query = """
    SELECT r.id, i.instrument_name, r.description, r.rating
    FROM review r
    JOIN instrument i ON r.instrument_id = i.id
    WHERE r.user_id = %s;
    """
    try:
        result = db_manager.fetch_all(query, (user_id,))
        if result:
            print(f"\nReviews by User ID {user_id}")
            for row in result:
                print(f"Review ID: {row[0]}, Instrument: {row[1]}, Rating: {row[3]}, Description: {row[2]}")
        else:
            print("You have not written any reviews.")
    except Exception as e:
        print("Error viewing user reviews:", e)
