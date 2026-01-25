from app.extensions import get_db_connection

class UserModel:

    @staticmethod
    def create(email, password_hash):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO users (email, password_hash)
                VALUES (%s, %s)
            """
            cursor.execute(query, (email, password_hash))
            conn.commit()
            user_id = cursor.lastrowid
            return user_id
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, email, created_at FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
            return user
        finally:
            cursor.close()
            conn.close()
