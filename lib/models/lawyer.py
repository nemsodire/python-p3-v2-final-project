# lib/models/lawyer.py

from db import get_db_connection

class Lawyer:

    @classmethod
    def get_all_lawyers():
        """Retrieve all lawyers from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lawyer")
        lawyers = cursor.fetchall()
        conn.close()
        return lawyers
    
    @classmethod
    def create_lawyer(cls, name, specialty):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Lawyer (name, specialty, created_at) VALUES (?, ?, CURRENT_TIMESTAMP)", (name, specialty))
            lawyer_id = cursor.lastrowid  # Get the ID of the last inserted row
            conn.commit()
            return lawyer_id  # Return the ID of the newly created lawyer

    @classmethod
    def delete_lawyer(cls, lawyer_id):  # Update method name here
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Lawyer WHERE id = ?", (lawyer_id,))
            conn.commit()


    @classmethod
    def view_all(cls):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Lawyer")
            return cursor.fetchall()

    @classmethod
    def view_by_id(cls, lawyer_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Lawyer WHERE id = ?", (lawyer_id,))
            return cursor.fetchone()

    @classmethod
    def update(cls, lawyer_id, name, specialty):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Lawyer SET name = ?, specialty = ? WHERE id = ?", (name, specialty, lawyer_id))
            conn.commit()
