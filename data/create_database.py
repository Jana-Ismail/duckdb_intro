import duckdb

def create_database(db_path):
    conn = duckdb.connect(db_path)

    transactions = conn.execute('select * from "data/transactions.parquet"').fetchall()

    print(transactions)
    return db_path

def main():
    db_path = 'data/local_db.duckdb'
    create_database(db_path)

if __name__ == "__main__":
    main()
