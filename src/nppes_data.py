import duckdb
import pandas as pd
import time

file_path = '~/Desktop/DE_2025/Project_2_Data/nppes_raw.parquet'

conn = duckdb.connect(':memory:')
conn2 = duckdb.connect('data/local_db.duckdb')

start_time = time.time()
conn.execute(f"CREATE TABLE nppes AS SELECT * FROM '{file_path}'")
end_time = time.time()
print(f"Time taken to create table in memory: {end_time - start_time} seconds")

start_time = time.time()
conn2.execute(f"CREATE TABLE nppes AS SELECT * FROM '{file_path}'")
end_time = time.time()
print(f"Time taken to create database file: {end_time - start_time} seconds")