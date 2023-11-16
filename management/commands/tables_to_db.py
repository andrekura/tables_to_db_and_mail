from pandas import DataFrame

from pathlib import Path
import sqlite3

from tables_read import read_excel_file

import ipdb

# PATH TO TABLE:
tables_path = Path("./table_itself/")


# PATH TO DB:
database_path = Path("./db/")
db = database_path.joinpath("db_sqlite3.db")

def insert_table_with_procx(db: Path, df: DataFrame) -> None:
    # Connect to SQLite3 database:
    with sqlite3.connect(db) as conn:
        table_name = "table_name"
        df.to_sql(table_name, conn, if_exists='replace', index=False)

# Read Excel file into Dataframe:
dataframe = read_excel_file(tables_path)
# ipdb.set_trace()

# Insert table to SQLite database:
insert_table_with_procx(db, dataframe)

