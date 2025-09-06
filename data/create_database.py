import duckdb

def create_database():
    db_path = 'data/local_db.duckdb'
    conn = duckdb.connect(db_path)

    transactions = conn.execute('select * from "data/transactions.csv"').fetchall()

    print(transactions)
    return db_path

if __name__ == "__main__":
    print("Creating database...")
    DB_PATH = create_database()
    print(f"Database ready at: {DB_PATH}")
