import duckdb

def main():
    db_path = 'data/dbt_db.duckdb'
    duckdb.connect(db_path)

if __name__ == "__main__":
    main()