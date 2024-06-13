from db import get_db_connection

class Case:
    def __init__(self, id, title, description, lawyer_id, status, created_at):
        self._id = id
        self._title = title
        self._description = description
        self._lawyer_id = lawyer_id
        self._status = status
        self._created_at = created_at

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def lawyer_id(self):
        return self._lawyer_id

    @property
    def status(self):
        return self._status

    @property
    def created_at(self):
        return self._created_at

    @classmethod
    def create_case(cls, title, description, lawyer_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Cases (title, description, lawyer_id, status, created_at)
                VALUES (?, ?, ?, 'Pending', CURRENT_TIMESTAMP)
            """, (title, description, lawyer_id))
            case_id = cursor.lastrowid
            conn.commit()
            return case_id

    @classmethod
    def delete_case(cls, case_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Cases WHERE id = ?", (case_id,))
            conn.commit()

    @classmethod
    def get_all_cases(cls):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Cases")
            return cursor.fetchall()

    @classmethod
    def find_case_by_id(cls, case_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Cases WHERE id = ?", (case_id,))
            return cursor.fetchone()
