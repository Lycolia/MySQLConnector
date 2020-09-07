import os
import mysql.connector


class MySqlConnector:
    def __init__(self):
        self.conn = mysql.connector.connect(
            option_files=os.path.join(os.path.dirname(__file__), 'mysql.conf')
        )
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()
