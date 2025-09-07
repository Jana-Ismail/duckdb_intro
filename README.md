1. Run data_setup.py script to create data/transactions.csv and data/transactions.parquet files with 50,000 rows of data each

2. Run create_database.py script to very quickly create .duckdb database and read in 50,000 rows to a newly created table

3. Step through src/main.py script
    - first block creates data/transactions_transformed.parquet
    - second block does similar thing and creates data/transactions_transformed_in_memory.parquet, but it doesn't persist (no .duckdb file with transformed tables or forensics exists) - only the output file

4. Compare times between :memory: and local_db.duckdb in nppes_data.py; Then run CREATE TABLE statement in DataGrip vs SELECT *
    - ~ 1 minute, 1 minute, 1 min 20 s for CREATE TABLE runs

    - 4s for select * directly on parquet file - preface to power/speed of the lakehouse 'ducklake' architecture that attaches a metadata catalog to point to parquet files that duckdb will directly read from

5. Afternoon task: spinup DuckDB (your choice of local or in-memory); take nppes dataset and play around with one of the stored procs that transformed some of the data with using DuckDB instead of Postgres

6. Warmup 07/10 AM - create .duckdb database, create a table, perform DuckDB CRUD operations

7. Introduction to Medallion Architecture with dbt
    - Initialize dbt project with duckdb
    - Point profiles.yml to absolute .duckdb database file, add extensions for httpfs and parquet
    - Perform silver staging transformations with dbt
    - Perform gold mart aggregations with dbt
    - Add some data validation with dbt test
    - Spin up dbt docs

8. Introduction to Jinja templating, sources.yml, dependency + dependency lineage, sources.yml vs. schema.yml validation and tests, mention of macros
    - {{ config() }}, {{ source() }}, {{ ref() }}
