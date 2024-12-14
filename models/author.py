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
    # Getter for ID
    @property
    def id(self):
        return self._id

    # Setter for ID
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    # Getter for name
    @property
    def name(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM authors WHERE id = ?", (self.id,))
        name = cursor.fetchone()["name"]
        conn.close()
        return name

    # Setter for name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after the author is instantiated.")
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (value, self.id))
        conn.commit()
        conn.close()
        self._name = value
