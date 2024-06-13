from db import get_db_connection

class Client:
    def init(self, id, name, contact_info, lawyer_id, created_at):
        self._id = id
        self._name = name
        self._contact_info = contact_info
        self._lawyer_id = lawyer_id
        self._created_at = created_at

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def contact_info(self):
        return self._contact_info
    
    @property
    def lawyer_id(self):
        return self._lawyer_id
    
    @property
    def created_at(self):
        return self._created_at
    
    @classmethod
    def create_client(cls, name, contact_info, lawyer_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Client (name, contact_info, lawyer_id, created_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)", (name, contact_info, lawyer_id))
            client_id = cursor.lastrowid
            conn.commit()
            return client_id
    
    @classmethod
    def delete_client(cls, client_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Client WHERE id = ?", (client_id,))
            conn.commit()
    
    @classmethod
    def get_all_clients(cls):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Client")
            return cursor.fetchall()
    
    @classmethod
    def find_client_by_id(cls, client_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Client WHERE id = ?", (client_id,))
            return cursor.fetchone()