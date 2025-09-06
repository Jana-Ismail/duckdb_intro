import duckdb

conn = duckdb.connect('data/local_db.duckdb')

conn.execute(open('src/test.sql', 'r').read())

results = conn.fetchall()
print(results)
conn.close()

def main():
    pass

if __name__ == "__main__":
    main()