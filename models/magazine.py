from database.connection import get_db_connection
class Magazine:
    def __init__(self, id: int, name: str, category: str):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into the database if ID is None, otherwise set the existing ID
        if id is None:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (name, category)
            )
            self.id = cursor.lastrowid
        else:
            self.id = id

        conn.commit()
        conn.close()

        self.name = name
        self.category = category
