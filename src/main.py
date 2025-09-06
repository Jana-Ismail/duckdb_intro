import duckdb

# conn = duckdb.connect('data/local_db.duckdb')
# conn.execute("CREATE TABLE transactions AS SELECT * FROM 'data/transactions.parquet'")
# transactions_df = conn.execute("SELECT * FROM transactions").df()
# transactions_df['amount'] = transactions_df['amount'] * 1.1
# transactions_df.to_parquet('data/transactions_transformed.parquet', index=False)

memory_conn = duckdb.connect(':memory:')
memory_conn.execute("CREATE TABLE transactions AS SELECT * FROM 'data/transactions.parquet'")
mem_transactions_df = memory_conn.execute("SELECT * FROM transactions").df()
mem_transactions_df['amount'] = mem_transactions_df['amount'] * 1.1
mem_transactions_df.to_parquet('data/transactions_transformed_in_memory.parquet', index=False)
