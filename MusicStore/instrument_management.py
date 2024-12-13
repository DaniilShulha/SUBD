from db_connection import DatabaseManager
from decorators import check_role


@check_role(['customer', 'manager', 'administrator'])
def view_all_instruments(db_manager, role_id):
    """View all instruments in the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
    """
    query = """
    SELECT i.id, i.instrument_name, c.category_name, m.name as manufacturer_name, i.description
    FROM instrument i
    JOIN category c ON i.category_id = c.id
    JOIN manufacturer m ON i.manufacturer_id = m.id
    """
    try:
        result = db_manager.execute_query(query)
        if result:
            print("\nList of all instruments:")
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Manufacturer: {row[3]}, Description: {row[4]}")
            return result
        else:
            print("No instruments found")
            return []
    except Exception as e:
        print("Error viewing instruments:", e)
        return None


@check_role(['manager', 'administrator'])
def add_instrument(db_manager, role_id, instrument_name, category_id, manufacturer_id, description=None):
    """Add a new instrument to the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        instrument_name: Name of the instrument
        category_id: ID of the instrument category
        manufacturer_id: ID of the manufacturer
        description: Optional description of the instrument
    """
    query = """
    INSERT INTO instrument (instrument_name, category_id, manufacturer_id, description)
    VALUES (%s, %s, %s, %s)
    RETURNING id;
    """
    try:
        result = db_manager.execute_query(query, (instrument_name, category_id, manufacturer_id, description))
        if result:
            instrument_id = result[0][0]
            print(f"Instrument added successfully with ID: {instrument_id}")
            return instrument_id
        return None
    except Exception as e:
        print("Error adding instrument:", e)
        return None


@check_role(['manager', 'administrator'])
def update_instrument(db_manager, role_id, instrument_id, instrument_name=None, category_id=None, 
                     manufacturer_id=None, description=None):
    """Update an existing instrument in the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        instrument_id: ID of the instrument to update
        instrument_name: Optional new name of the instrument
        category_id: Optional new category ID
        manufacturer_id: Optional new manufacturer ID
        description: Optional new description
    """
    fields = []
    params = []

    if instrument_name:
        fields.append("instrument_name = %s")
        params.append(instrument_name)
    if category_id:
        fields.append("category_id = %s")
        params.append(category_id)
    if manufacturer_id:
        fields.append("manufacturer_id = %s")
        params.append(manufacturer_id)
    if description is not None:
        fields.append("description = %s")
        params.append(description)

    if not fields:
        print("No fields to update")
        return False

    query = f"""
    UPDATE instrument 
    SET {', '.join(fields)} 
    WHERE id = %s
    """
    params.append(instrument_id)

    try:
        check_query = "SELECT id FROM instrument WHERE id = %s"
        result = db_manager.execute_query(check_query, (instrument_id,))
        if not result:
            print(f"Instrument with ID {instrument_id} not found")
            return False

        db_manager.execute_query(query, tuple(params))
        print(f"Instrument with ID {instrument_id} updated successfully")
        return True
    except Exception as e:
        print("Error updating instrument:", e)
        return False


@check_role(['manager', 'administrator'])
def delete_instrument(db_manager, role_id, instrument_id):
    """Delete an instrument from the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        instrument_id: ID of the instrument to delete
    """
    try:
        check_query = "SELECT id FROM instrument WHERE id = %s"
        result = db_manager.execute_query(check_query, (instrument_id,))
        if not result:
            print(f"Instrument with ID {instrument_id} not found")
            return False

        delete_query = "DELETE FROM instrument WHERE id = %s"
        db_manager.execute_query(delete_query, (instrument_id,))
        print(f"Instrument with ID {instrument_id} deleted successfully")
        return True
    except Exception as e:
        print("Error deleting instrument:", e)
        return False


@check_role(['customer', 'manager', 'administrator'])
def view_all_categories(db_manager, role_id):
    """View all categories in the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
    """
    query = "SELECT id, category_name FROM category"
    try:
        result = db_manager.execute_query(query)
        if result:
            print("\nList of all categories:")
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}")
            return result
        else:
            print("No categories found")
            return []
    except Exception as e:
        print("Error viewing categories:", e)
        return None


@check_role(['manager', 'administrator'])
def add_category(db_manager, role_id, category_name):
    """Add a new category to the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        category_name: Name of the new category
    """
    query = """
    INSERT INTO category (category_name)
    VALUES (%s)
    RETURNING id;
    """
    try:
        result = db_manager.execute_query(query, (category_name,))
        if result:
            category_id = result[0][0]
            print(f"Category added successfully with ID: {category_id}")
            return category_id
        return None
    except Exception as e:
        print("Error adding category:", e)
        return None


@check_role(['manager', 'administrator'])
def update_category(db_manager, role_id, category_id, category_name):
    """Update an existing category in the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        category_id: ID of the category to update
        category_name: New name for the category
    """
    try:
        check_query = "SELECT id FROM category WHERE id = %s"
        result = db_manager.execute_query(check_query, (category_id,))
        if not result:
            print(f"Category with ID {category_id} not found")
            return False

        update_query = "UPDATE category SET category_name = %s WHERE id = %s"
        db_manager.execute_query(update_query, (category_name, category_id))
        print(f"Category with ID {category_id} updated successfully")
        return True
    except Exception as e:
        print("Error updating category:", e)
        return False


@check_role(['manager', 'administrator'])
def delete_category(db_manager, role_id, category_id):
    """Delete a category from the database.
    
    Args:
        db_manager: Database connection manager
        role_id: ID of the user's role
        category_id: ID of the category to delete
    """
    try:
        check_query = "SELECT id FROM category WHERE id = %s"
        result = db_manager.execute_query(check_query, (category_id,))
        if not result:
            print(f"Category with ID {category_id} not found")
            return False

        delete_query = "DELETE FROM category WHERE id = %s"
        db_manager.execute_query(delete_query, (category_id,))
        print(f"Category with ID {category_id} deleted successfully")
        return True
    except Exception as e:
        print("Error deleting category:", e)
        return False
