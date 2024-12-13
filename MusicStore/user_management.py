import hashlib
from db_connection import DatabaseManager


def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(db_manager, user_name, email, password, role_name, country_name):
    """Register a new user with a specified role and country."""
    try:
        # Hash the password
        hashed_password = hash_password(password)

        # Get role ID from role name
        role_query = "SELECT id FROM role WHERE role_name = %s"
        role_result = db_manager.execute_query(role_query, (role_name,))
        if not role_result:
            print(f"Role '{role_name}' does not exist.")
            return
        role_id = role_result[0][0]
        print(f"Assigned Role ID: {role_id} for role '{role_name}'.")

        # Get country ID from country name
        country_query = "SELECT id FROM country WHERE country_name = %s"
        country_result = db_manager.execute_query(country_query, (country_name,))
        if not country_result:
            print(f"Country '{country_name}' does not exist.")
            return
        country_id = country_result[0][0]

        # Insert new user into the database
        insert_query = """
        INSERT INTO users (user_name, email, password, role_id, country_id)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
        """
        user_id = db_manager.execute_query(insert_query, (user_name, email, hashed_password, role_id, country_id))
        if user_id:
            print(f"User '{user_name}' registered successfully.")
        else:
            print("Registration failed.")
    except Exception as e:
        print("Error registering user:", e)


def login_user(db_manager, email, password):
    """Authenticate a user and return their role."""
    try:
        # Hash the password
        hashed_password = hash_password(password)

        # Query to find user with matching email and password
        query = """
        SELECT u.id, u.user_name, r.role_name FROM users u
        JOIN role r ON u.role_id = r.id
        WHERE u.email = %s AND u.password = %s
        """
        result = db_manager.execute_query(query, (email, hashed_password))
        if result:
            user_id, user_name, role_name = result[0]
            print(f"Welcome, {user_name}! You are logged in as a {role_name}.")
            return user_id, role_name
        else:
            print("Invalid email or password.")
            return None, None
    except Exception as e:
        print("Error logging in user:", e)
        return None, None


def update_user_profile(db_manager, user_id, user_name=None, email=None, password=None, country_id=None):
    # Build the update query dynamically based on provided fields
    fields = []
    params = []

    if user_name:
        fields.append("user_name = %s")
        params.append(user_name)
    if email:
        fields.append("email = %s")
        params.append(email)
    if password:
        hashed_password = hash_password(password)
        fields.append("password = %s")
        params.append(hashed_password)
    if country_id:
        fields.append("country_id = %s")
        params.append(country_id)

    if not fields:
        print("No fields to update")
        return

    query = f"UPDATE users SET {', '.join(fields)} WHERE id = %s"
    params.append(user_id)

    try:
        db_manager.execute_query(query, tuple(params))
        print(f"User profile with ID {user_id} updated successfully.")
    except Exception as e:
        print("Error updating user profile:", e)


def delete_user_profile(db_manager, user_id):
    # Сначала проверяем, существует ли пользователь
    check_query = "SELECT id FROM users WHERE id = %s"
    try:
        result = db_manager.execute_query(check_query, (user_id,))
        if not result:
            print(f"User with ID {user_id} not found")
            return False

        # Если пользователь существует, удаляем его
        delete_query = "DELETE FROM users WHERE id = %s"
        db_manager.execute_query(delete_query, (user_id,))
        print(f"User profile with ID {user_id} deleted successfully.")
        return True
    except Exception as e:
        print("Error deleting user profile:", e)
        return False