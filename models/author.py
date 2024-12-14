from database.connection import get_db_connection
class Author:
    def __init__(self, id: int, name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into the database if ID is None, otherwise set the existing ID
        if id is None:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)",
                (name,)
            )
            self.id = cursor.lastrowid
        else:
            self.id = id

        conn.commit()
        conn.close()

        self.name = name

    def __repr__(self):
        return f"<Author {self.name}>"