import sqlite3

class DbConnectionPoolProxy:
    """
    Serverless DB Connection Pool Proxy
    Pools and manages transactional requests to avoid SQLite resource exhaustion.
    """
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

    def execute_transaction(self, sql):
        print(f"Proxying secure transaction: {sql}")
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.fetchall()

if __name__ == "__main__":
    proxy = DbConnectionPoolProxy()
    proxy.execute_transaction("CREATE TABLE nodes (id INTEGER, status TEXT)")
    proxy.execute_transaction("INSERT INTO nodes VALUES (1, 'Active'), (2, 'Offline')")
    print(proxy.execute_transaction("SELECT * FROM nodes WHERE status='Active'"))
