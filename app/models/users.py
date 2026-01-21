from app.extensions import get_db_connection

class UserModel:

    @staticmethod
    def create(email, password_hash):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO users (email, password_hash)
            VALUES (%s, %s)
        """
        cursor.execute(query, (email, password_hash))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def find_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
