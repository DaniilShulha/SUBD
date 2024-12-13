from functools import wraps

def check_role(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(db_manager, role_id, *args, **kwargs):
            print(f"\nDEBUG: Checking access for role_id: {role_id}")
            print(f"DEBUG: Function name: {func.__name__}")
            print(f"DEBUG: Allowed roles: {allowed_roles}")
            print(f"DEBUG: Additional args: {args}")
            print(f"DEBUG: Additional kwargs: {kwargs}")
            
            # Проверяем роль пользователя
            query = "SELECT role_name FROM role WHERE id = %s"
            try:
                result = db_manager.execute_query(query, (role_id,))
                if not result:
                    print("Invalid role ID")
                    return None
                
                user_role = result[0][0]
                print(f"DEBUG: User role from database: {user_role}")
                
                if user_role not in allowed_roles:
                    print(f"Access denied. Required roles: {', '.join(allowed_roles)}")
                    return None
                
                # Вызываем оригинальную функцию с role_id
                return func(db_manager, role_id, *args, **kwargs)
            except Exception as e:
                print(f"Error checking role: {e}")
                return None
            
        return wrapper
    return decorator
